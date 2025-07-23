import os
from typing import List, Dict
import torch
from sentence_transformers import SentenceTransformer
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import numpy as np
from tqdm import tqdm

class MedicalDiagnosisRAG:
    def __init__(self):
        print("Loading models...")
        # Load free sentence transformer model for embeddings
        self.embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
        
        # Load free text generation model
        self.tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-small")
        self.generator = pipeline(
            "text2text-generation",
            model="google/flan-t5-small",
            tokenizer=self.tokenizer,
            max_length=20000
        )
        
        self.papers_embeddings = []
        self.papers_content = []
        self.papers_metadata = []  # Store paper titles and diseases
        
    def load_papers(self, papers_dir: str):
        """Load papers from local directory"""
        print(f"Loading papers from: {papers_dir}")
        papers = []
        
        # Disease name mapping for normalization
        disease_mapping = {
            "petussis": "pertussis",
            "tb": "tuberculosis",
            "covid": "covid-19"
        }
        
        try:
            for filename in os.listdir(papers_dir):
                if filename.endswith('.txt'):
                    with open(os.path.join(papers_dir, filename), 'r') as f:
                        content = f.read()
                        # Extract disease name from filename and normalize it
                        raw_disease = filename.split('_')[0].lower()
                        disease = disease_mapping.get(raw_disease, raw_disease)
                        papers.append({
                            "id": filename,
                            "content": content,
                            "disease": disease
                        })
            
            if not papers:
                raise ValueError(f"No .txt files found in {papers_dir}")
            
            print(f"Successfully loaded {len(papers)} papers")
            return papers
            
        except Exception as e:
            print(f"Error loading papers: {e}")
            return []

    def initialize_system(self, papers_dir: str):
        """Initialize the system with local papers"""
        if not os.path.exists(papers_dir):
            raise ValueError(f"Papers directory not found: {papers_dir}")
            
        papers = self.load_papers(papers_dir)
        if papers:
            self.create_embeddings(papers)
            print(f"System initialized with {len(papers)} papers")
            # Print loaded diseases for verification
            diseases = set(paper["disease"] for paper in papers)
            print(f"Loaded papers for diseases: {', '.join(diseases)}")
        else:
            raise ValueError("No papers were loaded. Please check your papers directory.")

    def create_embeddings(self, papers: List[Dict]):
        """Create embeddings from papers"""
        print("Creating embeddings...")
        
        for paper in tqdm(papers, desc="Processing papers"):
            # Create embedding for the paper content
            embedding = self.embedding_model.encode(paper["content"])
            self.papers_embeddings.append(embedding)
            self.papers_content.append(paper["content"])
            self.papers_metadata.append({
                "id": paper["id"],
                "disease": paper.get("disease", "unknown")
            })
            
        # Convert to numpy array for efficient similarity search
        self.papers_embeddings = np.array(self.papers_embeddings)
        print(f"Created embeddings for {len(papers)} papers")
    
    def get_relevant_contexts(self, query: str, k: int = 3) -> List[Dict]:
        """Get most relevant paper contents for the query"""
        # Create query embedding
        query_embedding = self.embedding_model.encode(query)
        
        # Calculate similarities
        similarities = np.dot(self.papers_embeddings, query_embedding)
        most_similar_indices = np.argsort(similarities)[-k:][::-1]
        
        # Return relevant contents with metadata
        return [{
            "content": self.papers_content[i],
            "metadata": self.papers_metadata[i],
            "similarity": similarities[i]
        } for i in most_similar_indices]

    def diagnose(self, symptoms: str) -> str:
        """Generate diagnosis based on symptoms"""
        # Get relevant medical contexts
        relevant_docs = self.get_relevant_contexts(symptoms)
        
        # Check for low similarity
        low_similarity = all(doc['similarity'] < 0.2 for doc in relevant_docs)
        disclaimer = ""
        if low_similarity:
            disclaimer = (
                "\n\n[Note: The provided symptoms do not closely match any medical literature in the database. "
                "The following analysis is based on the most similar available documents, but confidence is low. "
                "Please consult a healthcare professional for further evaluation.]\n"
            )
        
        # Truncate each context to manage length
        max_chars_per_context = 500  # Increased context length
        context_info = []
        
        for doc in relevant_docs:
            disease = doc["metadata"]["disease"].upper()
            similarity_score = int(doc["similarity"] * 100)
            content = doc["content"]

            # Simple extraction (customize as needed)
            # For demo, just use the first 2 sentences as diagnosis, next 1 as medicine
            sentences = content.split('.')
            diagnosis_text = '.'.join(sentences[:2]).strip() + '.'
            medicine_text = '.'.join(sentences[2:3]).strip() + '.'

            context_info.append(
                f"Disease: {disease}\n"
                f"Relevance Score: {similarity_score}/100\n"
                f"Available Diagnosis: {diagnosis_text}\n"
                f"Available Generic Medicine: {medicine_text}\n"
            )
        
        # Prepare prompt with more specific instructions
        medical_literature = '\n'.join(context_info)
        
        prompt = f"""{disclaimer}
You are an expert medical AI assistant analyzing patient symptoms.

Patient's Symptoms:
{symptoms}

Please provide a detailed structured response using the following section headers (each on a new line):

Diagnosis:
- Primary suspected conditions
- Alternative possibilities to consider
- Reasoning for each based on symptoms and literature

Symptom Analysis:
- Match between presented symptoms and disease patterns
- Key symptoms present or absent
- Typical progression patterns

Risk Assessment:
- Confidence level (High/Medium/Low) with detailed reasoning
- Risk factors identified
- Severity indicators

Critical Warning Signs:
- Red flags requiring immediate attention
- Specific symptoms to monitor
- Progression indicators

Recommended Actions:
- Immediate steps needed
- Testing recommendations
- When to seek emergency care
- Follow-up care suggestions

Important: This is AI-generated analysis based on available medical literature. It should not replace professional medical evaluation. Please consult healthcare providers for proper diagnosis and treatment.

Relevant Medical Literature:
{medical_literature}
"""
        
        # Robust fix: Ensure prompt is at most 512 tokens
        input_ids = self.tokenizer(prompt, return_tensors="pt").input_ids
        if input_ids.shape[1] > 512:
            input_ids = input_ids[:, :512]
            prompt = self.tokenizer.decode(input_ids[0], skip_special_tokens=True)
        
        # Generate diagnosis with improved parameters
        response = self.generator(
            prompt,
            max_length=512,
            num_return_sequences=1,
            temperature=0.7,
            do_sample=True,
            top_k=50,
            top_p=0.95,
            repetition_penalty=1.2
        )[0]['generated_text']
        
        return response

def main():
    print("Initializing medical diagnosis system...")
    diagnosis_system = MedicalDiagnosisRAG()
    
    # Get papers directory
    while True:
        papers_dir = input("Enter the path to your papers directory: ").strip()
        if os.path.exists(papers_dir):
            break
        print(f"Directory not found: {papers_dir}")
        print("Please enter a valid directory path.")
    
    try:
        diagnosis_system.initialize_system(papers_dir)
        
        # Interactive loop
        while True:
            print("\nEnter your symptoms (or 'quit' to exit):")
            symptoms = input().strip()
            
            if symptoms.lower() == 'quit':
                break
            
            # Recommend at least five symptoms
            if len(symptoms.split()) < 5:
                print("Warning: For best results, please enter at least five symptoms.")
            
            print("\nAnalyzing symptoms...")
            try:
                diagnosis = diagnosis_system.diagnose(symptoms)
                print("\nDiagnosis Results:")
                for line in diagnosis.splitlines():
                    print(line)
            except Exception as e:
                print(f"Error generating diagnosis: {e}")
                
            print("\n" + "="*50)
    
    except Exception as e:
        print(f"Error initializing the system: {e}")
        print("Please make sure your papers directory contains valid .txt files with proper disease names in the filenames.")

if __name__ == "__main__":
    main() 
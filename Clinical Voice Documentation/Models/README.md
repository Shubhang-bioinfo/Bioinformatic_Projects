# Clinical Voice Documentation System

This application converts voice input into structured clinical documentation using speech recognition and natural language processing.

## Features

- Voice input recording through microphone
- Speech-to-text conversion using Google Speech Recognition
- NLP processing of medical text using spaCy
- Automatic generation of structured clinical documentation in Word format
- Extraction of clinical entities (symptoms, medications, procedures, measurements)

## Setup

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Install the spaCy English language model:
```bash
python -m spacy download en_core_web_sm
```

3. For macOS users, you might need to install portaudio first:
```bash
brew install portaudio
```

## Usage

1. Run the application:
```bash
python clinical_voice_doc.py
```

2. Press Enter to start recording your voice input
3. Speak clearly into your microphone
4. The application will automatically:
   - Transcribe your speech to text
   - Process the text using NLP
   - Generate a structured Word document
   - Save the document with a timestamp

5. Press 'q' to quit the application

## Output

The application generates Word documents (.docx) with the following sections:
- Date and time of recording
- Transcribed notes (raw text)
- Structured clinical information:
  - Symptoms
  - Medications
  - Procedures
  - Measurements

## Requirements

- Python 3.7+
- Working microphone
- Internet connection (for Google Speech Recognition)
- macOS, Linux, or Windows

## Note

The accuracy of the clinical entity recognition depends on the quality of:
1. Audio input
2. Speech recognition
3. NLP model's ability to recognize medical terms

For best results:
- Speak clearly and at a moderate pace
- Use proper medical terminology
- Ensure a quiet recording environment

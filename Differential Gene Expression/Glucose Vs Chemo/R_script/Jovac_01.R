# Step_01; loading the library
library("tidyverse")
library("DESeq2")
library("ggpubr")

#loading data
Data = read.table('../Batch-Files/feature-count/counts.txt', sep='\t', header=TRUE)

#view data
View(Data)

# to view only first six lines of data
Data %>% head()
# %>% = pipe symbol, it will come it in console
# check rows and columns 
dim(Data)
# to get the column names
names(Data)
#providing the names to the data
names(Data)[7:12] = c("GLU1", "GLU2", "GLU3", "CHEM1", "CHEM2", "CHEM3")
# 'c' is a vector 
view(Data)

#create count file
gen_counts = Data[,7:12]
view(gen_counts)
#providing rownames  to count files
rownames(gen_counts) = Data$Geneid
#'$' to access column 
view(gen_counts)
# providing conditons names
conds = c("GLU", "GLU", "GLU", "CHEM", "CHEM", "CHEM")
#col = column data 
dds = DESeqDataSetFromMatrix(countData = as.matrix(gen_counts), colData = data.frame(conds=factor(conds)), design = formula(~conds))
View(dds)
dds
dds = DESeq(dds)
nrow(res)
# check the dds result
res = results(dds)
view(res)
#to remove the entries with gene count less than 5
dds = dds[ rowSums(counts(dds)) > 5, ]
nrow(dds)
res = results(dds)
view(res)
result = as.data.frame(res)
write.csv(result,"result.csv")

#plots
nsb = sum(rowMeans(counts(dds, normalized=TRUE)) > 5)
vsd = vst(dds, blind = TRUE, nsub = nsb)
plotDists = function (vsd.obj) {
  sampleDists <- dist(t(assay(vsd.obj)))
  sampleDistMatrix <- as.matrix( sampleDists )
  rownames(sampleDistMatrix) <- paste( vsd.obj$group )
  colors <- colorRampPalette( rev(RColorBrewer::brewer.pal(9, "Blues")) )(255)
  pheatmap::pheatmap(sampleDistMatrix,
                     clustering_distance_rows = sampleDists,
                     clustering_distance_cols = sampleDists,
                     col = colors)
}
plotDists(vsd)

plot_PCA = function (vsd.obj) {
  pcaData <- plotPCA(vsd.obj,  intgroup = c("conds"), returnData = T)
  percentVar <- round(100 * attr(pcaData, "percentVar"))
  ggplot(pcaData, aes(PC1, PC2, color=group)) +
    geom_point(size=3) +
    labs(x = paste0("PC1: ",percentVar[1],"% variance"),
         y = paste0("PC2: ",percentVar[2],"% variance"),
         title = "PCA Plot colored by group") +
    ggrepel::geom_text_repel(aes(label = name), color = "black")
}
plot_PCA(vsd)

ggmaplot(res, main = "Differential expression in Glucose vs Chemostat",
         fdr = 0.01, fc = 4, size = 3,
         palette = c("red", "blue", "darkgray"),
         legend = "top", top = 0)
ggsave("./DE/maplot.png")


# downloading significant genes
resSig = results(dds)
resSig = as.data.frame(subset(res,padj<0.5) )
resSig = resSig[order(resSig$log2FoldChange,decreasing=TRUE),]
head(resSig)
write.csv(resSig,"SigGenes.csv")
nrow(resSig)
ResSig = results(dds)
ResSig = as.data.frame(subset(res,padj<0.05) )
ResSig = ResSig[order(ResSig$log2FoldChange,decreasing=TRUE),]
nrow(ResSig)
write.csv(ResSig,"HighlySigGenes.csv")













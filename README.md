# Sentiment Classification

## 项目介绍

+ 本项目为情感分析，输入文本给出情感分类。
+ 所构造的模型为基于LSTM的情感分析模型，使用[这里](https://github.com/CLUEbenchmark/CLUEDatasetSearch#%E6%83%85%E6%84%9F%E5%88%86%E6%9E%90)提供的微博数据集进行模型训练。

## 项目流程

1. 分词([jieba](https://github.com/fxsjy/jieba))
2. 载入[预训练词向量](https://github.com/Embedding/Chinese-Word-Vectors)。对于预训练词向量中不存在的词，参考fasttext的方式解决oov (out of vocabulary) 问题：找到词的所有字符子串，将这些字符子串在预训练词向量中进行匹配，将匹配到的词向量的平均作为oov词的词向量。
3. 由LSTM模型预测
4. 模型集成。

## Demo




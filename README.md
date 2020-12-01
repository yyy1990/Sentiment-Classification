# Sentiment Classification

## 项目介绍

+ 本项目为情感分析，输入文本给出情感分类。
+ 所构造的模型为基于LSTM的情感分析模型，使用[这里](https://github.com/CLUEbenchmark/CLUEDatasetSearch#%E6%83%85%E6%84%9F%E5%88%86%E6%9E%90)提供的微博数据集进行模型训练。

## 项目流程

1. 分词([jieba](https://github.com/fxsjy/jieba))

2. 载入[预训练词向量](https://github.com/Embedding/Chinese-Word-Vectors)。对于预训练词向量中不存在的词，参考fasttext的方式解决oov (out of vocabulary) 问题：找到词的所有字符子串，将这些字符子串在预训练词向量中进行匹配，将匹配到的词向量的平均作为oov词的词向量。

3. 由LSTM模型预测。

   模型结构：输入预训练词向量->LSTM->线性层->sigmoid->round取整并判断是正面情感还是负面情感

4. 模型集成: 训练了三组不同的模型，三组模型在训练集-测试集的划分上不同，另外在LSTM->线性层之间的连接方式上略有不同。

   在做预测时，将一段文本输入并分别由三个模型打分，记录下simoid输出的未取整的分数，将三个分数的平均四舍五入取整并判断情感

## Demo

```python
import model
sentence1 = '阔别160年，马首铜像回归圆明园！'
result1 = model.get_sentiment(sentence1)
print(result1)
```

得到结果1.0，表示正面情感

```python
sentence2 = '世卫组织网站最新数据显示，截至欧洲中部时间30日15时37分(北京时间22时37分)，全球确诊病例较前一日增加496892例，达到62363527例；死亡病例增加7697例，达到1456687例。'
result2 = model.get_sentiment(sentence2)
print(result2)
```

得到结果0.0，表示负面情感
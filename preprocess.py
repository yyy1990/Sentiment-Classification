import re

import pandas as pd
from tqdm import tqdm

def todf(path, filename, save = True):
    '''
    将原始数据转换为csv
    数据来源：https://yunfeilongpoly.github.io/Team_resource.html
    path: 存储文件夹路径
    filename: 文件名
    save: 是否向硬盘保存
    '''
    f = open(path+filename, encoding = 'utf-8')
    data = f.readlines()
    f.close()
    
    pattern = '(\w+):(.*)' #原始文件数据模式为  情绪：句子 
    df = pd.DataFrame(columns = ['emotion', 'microblog'])
    for i in tqdm(range(len(data))):
        temp = re.findall(pattern, data[i])
        df.loc[i] = [temp[0][0], temp[0][1]]

    emotions = df['emotion'].unique()
    moods = {}
    for i, mood in enumerate(emotions):
        moods[mood] = i
    
    moods_series = df['emotion']
    label_series = [moods[mood] for mood in moods_series]
    df['label'] = label_series #转换为数字标签方便训练
    
    if save == True:
        df.to_csv(path+'microblog_data.csv', encoding = 'utf-8', index = False)
    return df

path = './data/'
data_filename = 'huati_filter_final_posts_no_sge.txt' 
df = todf(path, data_filename)
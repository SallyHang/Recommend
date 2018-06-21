# -*- coding: utf-8 -*-
""" 
Created on Tue Aug  8 13:27:08 2017 
 
@author: Jipon 
"""

from collections import defaultdict
from surprise import SVD
import os
from surprise import Dataset
from surprise import dataset
import pickle
import pprint


def get_top_n(predictions, n=10):
    '''''Return the top-N recommendation for each user from a set of predictions. 

    Args: 
        predictions(list of Prediction objects): The list of predictions, as 
            returned by the test method of an algorithm. 
        n(int): The number of recommendation to output for each user. Default 
            is 10. 

    Returns: 
    A dict where keys are user (raw) ids and values are lists of tuples: 
        [(raw item id, rating estimation), ...] of size n. 
    '''

    # First map the predictions to each user.，这句默认的list类型
    top_n = defaultdict(list)

    # uid为用户id，iid为项目id，true_r为真实的概率，est为分解后的估值
    for uid, iid, true_r, est, _ in predictions:
        top_n[uid].append((iid, est))

    # Then sort the predictions for each user and retrieve the k highest ones.
    for uid, user_ratings in top_n.items():
        #user_ratings=[('10980', 1.2274436453615198)]
        # 按照每个id的得分排序
        user_ratings.sort(key=lambda x: x[1], reverse=True)
        # [:n]数组切片 取前n个
        top_n[uid] = user_ratings[:n]

    return top_n


# 加载数据集

reader = dataset.Reader(line_format='user item rating', sep=' ')
data = Dataset.load_from_file('myrec.txt', reader)
trainset = data.build_full_trainset()

# 加载算法，训练数据

algo = SVD()
algo.train(trainset)

# 预测并保存结果至本地

testset = trainset.build_anti_testset()
predictions = algo.test(testset)

# Print the recommended items for each user

top_n = get_top_n(predictions)

# 将预测结果保存到文件中
if(os.path.exists('pres.txt')):
    os.remove('pres.txt')

for uid, user_ratings in top_n.items():
    #print(uid, [iid for (iid, _) in user_ratings])
    output = open('pres.txt', 'a')
    output.writelines(uid)
    output.write('[')
    for (iid, _) in user_ratings:
        output.write("'")
        output.writelines(iid)
        output.write("'")
        output.write(',')
    output.write(']')
    output.write('\n')
    output.close()

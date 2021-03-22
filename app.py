import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import keras
import csv
from keras.models import Sequential, load_model, save_model
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout

def denormalize(train):
    denorm = train.apply(lambda x: x*(np.max(traning_data.iloc[:,0])-np.min(traning_data.iloc[:,0]))+np.mean(traning_data.iloc[:,0]))
    return denorm

#data normalize
def normalize(train):
    train_norm = train.apply(lambda x: (x - np.mean(x)) / (np.max(x) - np.min(x)))
    return train_norm

#定義餵入的feature跟label序列
def train_1(norm_data, ref=150, predict=7):
    X_train, Y_train = [], []
    for i in range( norm_data.shape[0] - predict - ref + 1):
        X_train.append( np.array( norm_data.iloc[ i : i+ref, :1 ]))
        Y_train.append( np.array( norm_data.iloc[ i+ref : i + ref + predict , 0]))
    return np.array(X_train), np.array(Y_train)

if __name__ =='__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--training',
                        default='data',
                        help='input training data file name')
    parser.add_argument('--output',
                        default='submission.csv',
                        help='output file name')
    args = parser.parse_args()

    data_1 = pd.read_csv(args.training + '/20190101-20201031.csv')
    data_2 = pd.read_csv(args.training + '/20200101-20210131.csv')
    data_4 = pd.read_csv(args.training + '/20210101-20210321.csv')

    data_1.iloc[90:120, 3] *= 10        #三月的單位不一樣
    data_4.iloc[:,1] *= 10              #單位轉換
    y_1 = pd.DataFrame()
    y_2 = pd.DataFrame()
    y_3 = pd.DataFrame()
    y_1['備轉容量(MW)'] = data_1.loc[:364,'備轉容量(MW)']
    y_2['備轉容量(MW)'] = data_2.loc[:365,'備轉容量(MW)']  #whole 2020
    y_3['備轉容量(MW)'] = data_4.loc[:,'備轉容量(萬瓩)']
    traning_data = pd.concat([y_1, y_2, y_3], ignore_index=True) # 垂直合併
    
    np_test = np.array(traning_data).astype(int)  #shape = (811,1)
    np_test = np_test.reshape(811,)
    q = np.arange(811)
    # plt.bar(q,np_test)
    # plt.show()

    norm_data = normalize(traning_data)

    X_1,Y_1 = train_1(norm_data, 731, 8)
    train_x = X_1[:]
    train_y = Y_1[:]

    predict_x = norm_data[(norm_data.shape[0] - 731):].values
    predict_x = predict_x.reshape(1, 731, 1)

    reconstructed_model = keras.models.load_model("lstm_epochs30_dropout5_ref731_pre8.h5")    

    ans = reconstructed_model.predict(predict_x)
    ans = pd.DataFrame(ans)
    ans = denormalize(ans)

    # print(ans.values[0][1:])
    with open('submission.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['date','operating_reserve(MW)'])
        for i in range(7):
            writer.writerow(['2021/3/2' + str(i +3),str(ans.values[0][i])])

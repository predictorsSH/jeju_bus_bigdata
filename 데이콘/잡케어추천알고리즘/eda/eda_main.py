#Exploratory Data Analysis

import pandas as pd
from eda_functions import bar_chart

TRAIN_DATA_PATH = '../dataset/train.csv'
TEST_DATA_PATH = '../dataset/test.csv'

#데이터 불러오기
train = pd.read_csv(TRAIN_DATA_PATH)
test = pd.read_csv(TEST_DATA_PATH)

train.info()
test.info()

#feature별 분석

##d_l_match_yn
bar_chart(train['d_l_match_yn'])
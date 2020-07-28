import pandas as pd
import time
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

class Project_B:
    # 数据加载
    def get_data(self):
        data = pd.read_csv('./订单表.csv', encoding = 'gbk')
        return data

    def encode_units(self, x):
        if x <= 0:
            return 0
        if x >= 1:
            return 1
    # 采用mlxtend.frequent_patterns工具包

    def rule2(self):
        pd.options.display.max_columns=100
        start = time.time()
        data = self.get_data()
        hot_encoded_df=data.groupby(['客户ID','产品ID'])['产品ID'].count().unstack().reset_index().fillna(0).set_index('客户ID')
        hot_encoded_df = hot_encoded_df.applymap(self.encode_units)
        frequent_itemsets = apriori(hot_encoded_df, min_support=0.02, use_colnames=True)
        rules = association_rules(frequent_itemsets, metric="lift", min_threshold=0.5)
        print("频繁项集：", frequent_itemsets)
        print("关联规则：", rules[ (rules['lift'] >= 1) & (rules['confidence'] >= 0.5) ])
        #print(rules['confidence'])
        end = time.time()
        print("用时：", end-start)

    
if __name__ == "__main__":
    project = Project_B()
    project.rule2()

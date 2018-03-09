#逻辑回归，自动建模
import pandas as pd
#参数初始化
filename = './data/bankloan.xls'
data = pd.read_excel(filename)
x = data.iloc[:,:8].as_matrix()#截取0-8列作为X_Parameter
# print(x)
# x1 = data.iloc[:,:8].as_matrix()#截取0-7列作为X_Parameter
# print(x1)
y = data.iloc[:,8].as_matrix()#截取第8列作为Y_Parameter
data1 = data.drop(data.columns[[8]], axis=1)#删除第8列，下标从0开始
from sklearn.linear_model import LogisticRegression as LR#导入逻辑回归模型
from sklearn.linear_model import RandomizedLogisticRegression as RLR #选择合适的特征
rlr = RLR()#建立随机逻辑回归模型，筛选变量
rlr.fit(x, y)#训练模型
#print(rlr.get_support())#获取特征筛选结果，也可以通过.sources_方法作为获取各个特征的分数
print(u'通过随机逻辑回归模型筛选特征结束')
print(u'有效特征为：%s' % ','.join(data1.columns[rlr.get_support()]))#boolean值的数目应该与要提取的矩阵的列数相同
x  = data1[data1.columns[rlr.get_support()]].as_matrix()#筛选好特征

lr = LR()#建立逻辑回归模型
lr.fit(x, y)#用筛选好的特征数据来训练模型
print(u'逻辑回归模型训练结束')
print(u'模型的平均正确率为：%s' % lr.score(x,y))#给出本模型的平均正确率


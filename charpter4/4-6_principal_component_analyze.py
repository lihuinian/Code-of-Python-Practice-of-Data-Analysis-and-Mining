#主成分分析
import pandas as pd

#参数初始化
inputfile = './data/principal_component.xls'
outputfile = './tmp/dimention_reducted.xls'#降维后的数据
outputfile1 = './tmp/dimention_reducted1.xls'#降维后的数据

data = pd.read_excel(inputfile, header = None) #读入数据

from sklearn.decomposition import PCA

pca = PCA()
pca.fit(data)
#print(pca.components_) #返回模型的各个特征向量
print(pca.explained_variance_ratio_) #返回各个成分各自方差百分比
pca = PCA(3)
pca.fit(data)
low_d = pca.transform(data)#用它来降低维度
pd.DataFrame(low_d).to_excel(outputfile)#保存结果
pd.DataFrame(pca.inverse_transform(low_d)).to_excel(outputfile1)#必要时要用inverse_transform()函数来复原数据

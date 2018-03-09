import pandas as pd

#参数初始化
inputfile = './data/consumption_data.xls'#销量及其他属性数据
outputfile = './tmp/data_type.xls'#保存结果的文件名
k = 3#聚类的类别
iteration = 500#聚类最大循环次数
data = pd.read_excel(inputfile, index_col = 'Id')#读取数据
data_zs = 1.0*(data - data.mean())/data.std()#数据标准化

from sklearn.cluster import KMeans
model = KMeans(n_clusters = k, max_iter = iteration)#分为k类
model.fit(data_zs)#开始聚类

#简单打印结果
r1 = pd.Series(model.labels_).value_counts()#统计各个类别的数目
print(r1)
r2 = pd.DataFrame(model.cluster_centers_)#找出聚类中心
r = pd.concat([r2,r1], axis =1 )#横向连接（0是纵向）
r.columns = list(data.columns) + [u'类别数目']#重命名表头
print(r)

#详细输出原始数据及其类别
r = pd.concat([data, pd.Series(model.labels_, index = data.index)],axis =1)#详细输出每个样本对应的类别
r.columns = list(data.columns) + [u'聚类类别']#重命名表头
r.to_excel(outputfile)

# def density_plot(data):#自定义作图函数
#     import matplotlib.pyplot as plt
#     plt.rcParams['font.sans-serif'] = ['SimHei']#用来正常显示中文标签
#     plt.rcParams['axes.unicode_minus'] = False#用来正常显示负号
#     p = data.plot(kind = 'kde', linewidth = 2, subplots = True, sharex = False)
#     [p[i].set_ylabel(u'密度') for i in range(k)]
#     plt.legend()
#     return plt
#
# pic_output = './tmp/pd_'#概率密度图文件前缀
#
# for i in range(k):
#     density_plot(data[r[u'聚类类别']==i]).savefig(u'%s%s.png'%(pic_output, i))
#5-5
from sklearn.manifold import TSNE

tsne = TSNE()
tsne.fit_transform(data_zs)#进行数据降维
tsne = pd.DataFrame(tsne.embedding_, index = data_zs.index)#转换数据格式

import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']#用来正常显示中文符号
plt.rcParams['axes.unicode_minus'] = False#用来正常显示负号

#不同类别用不同颜色和样式绘图
d = tsne[r[u'聚类类别'] == 0]#提取聚类类别为0的x,y数据
plt.plot(d[0],d[1],'r.')
d = tsne[r[u'聚类类别'] == 1]
plt.plot(d[0],d[1],'go')
d = tsne[r[u'聚类类别'] == 2]
plt.plot(d[0],d[1],'b*')
plt.show()

#利用小波分析进行特征分析

#参数初始化
inputfile = './data/leleccum.mat'#提取自MATLAB的信号文件

from scipy.io import loadmat #mat是matlab专用格式，需要用loadmat读取它
mat = loadmat(inputfile)
#print(mat['leleccum'])#mat数据读取后，是一组list的list，[]里面还有[]
signal = mat['leleccum'][0]#提取list里面的第一个元素
#print(signal)
import pywt #导入pyWavelets
coeffs = pywt.wavedec(signal, 'bior3.7', level=5)
#返回结果为level+1个数字，第一个数组为逼近系数数组，后面的依次是细节系数数组
#print(coeffs)
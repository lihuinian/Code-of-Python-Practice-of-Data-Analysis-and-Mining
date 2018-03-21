# from nltk.tokenize import word_tokenize
# mytext = "Hello Adam, how are you? I hope everything is going well.Today is a good day, see you dude."
# print(word_tokenize(mytext))
import pandas as pd

inputfile = './data1/meidi_jd1.txt'#评论文件
outputfile = './data1/meidi_jd1_process_1.txt'#评论处理后保存路径
data = pd.read_csv(inputfile, encoding = 'utf-8', header = None)
l1 = len(data)
data = pd.DataFrame(data[0].unique())#去重
l2 = len(data)
data.to_csv(outputfile, index = False, header = False, encoding = 'utf-8' )
print(u'删除了%s条评论'%(l1-l2))
import pandas as pd
import matplotlib.pyplot as plt

def draw_from_dict(dicdata,RANGE, heng=0):
    ds = dicdata
    x = []
    y = []
    for d in ds:
        x.append(d[0])
        y.append(d[1])
    if heng == 0:
        plt.bar(x[0:RANGE], y[0:RANGE])
        plt.show()
        return 
    elif heng == 1:
        plt.barh(x[0:RANGE], y[0:RANGE])
        plt.show()
        return 
    else:
        return "heng的值仅为0或1！"

# data =pd.read_csv('tripadvisor-final .csv',header = 0,encoding = 'utf-8' ,dtype = str )
data =pd.read_csv('data.csv',header = 0,encoding = 'utf-8' ,dtype = str )
# index_col = ['Date ','Rate ','Topic ','Review ','Type ']

all_words = []
count = {}
nums = ['1','2','3','4','5']
bad = ['2','3']
# conditional selection and count

# for temp in data.iterrows():
#     if (temp[1]['Date '].startswith('2015')):
#         if temp[1]['Rate '] in nums:
#             count[temp[1]['Rate ']] = count.get(temp[1]['Rate '],0) +1

# key words count
# for temp in data.iterrows():
#     if temp[1]['Rate '] in bad :
#         words = temp[1]['Review '].split(' ')
#         all_words.append(words)

# types = ['business','solo','friends', 'family','couple']

# for temp in data.iterrows():
    # if(type(temp[1]['Type ']) == str):
    #     temp[1]['Type '] = temp[1]['Type '].replace(' ','')
    #     temp[1]['Type '] = temp[1]['Type '].lower()
    #     if temp[1]['Type '] == types[4]:
    #         # count[temp[1]['Type ']] = count.get(temp[1]['Type '],0) +1
    #         words = temp[1]['Review '].split(' ')
    #         all_words.append(words)
    # if(type(temp[1]['Type ']) != str):
    #     words = temp[1]['Review '].split(' ')
    #     all_words.append(words)


for content in data['Review ']:
    words = content.split(' ')
    all_words.append(words)
# print(all_words)

# create stop words 

f = open('stop_words.txt','r')
origin_stop_words = f.readlines()
stop_words = []
for word in origin_stop_words:
    temp = word.replace('\n','')
    stop_words.append(temp)

count = {}

error_list = ['risd','museum','providence','pvd']

for words in all_words:
    for word in words:
        word = word.lower()
        word = word.replace('-','')
        word = word.replace('.','')
        word = word.replace('!','')
        word = word.replace('?','')
        word = word.replace(',','')
        if word not in stop_words:
            if word not in error_list :
                count[word] =count.get(word,0) +1 

# show results
del count['&']
del count['']
sorted_result = sorted(count.items(),key=lambda x:x[1],reverse = False)
print (sorted_result)
sorted_result = sorted(count.items(),key=lambda x:x[1],reverse = True)
draw_from_dict(sorted_result,20)

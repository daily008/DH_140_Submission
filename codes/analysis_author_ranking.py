import pandas as pd
from compare_name import comparing
import matplotlib.pyplot as plot

input_data = pd.read_csv("data/different_author_information.csv")

author_information = []
tcount = 0
for i in range(1,1566):
    doi = input_data.iloc[i,0]
    dauthor_number = input_data.iloc[i,4]
    rauthor_number = input_data.iloc[i,5]
    dauthor = input_data.iloc[i,2]
    rauthor = input_data.iloc[i,3]

    m = dauthor[2:(len(dauthor)) - 2]  # 输入的是字符串形式的列表，以下几行的目的是把字符串形式的列表数据转换回字符串
    dauthor_list = m.split("', '")

    n = rauthor[2:(len(rauthor)) - 2]  # 输入的是字符串形式的列表，以下几行的目的是把字符串形式的列表数据转换回字符串
    rauthor_list = n.split("', '")

    p1 = int(dauthor_number * 0.3)
    p2 = int(dauthor_number * 0.6)
    q1 = int(rauthor_number * 0.3)
    q2 = int(rauthor_number * 0.6)

    for dranking in range(1, len(dauthor_list)+1):
        m = {}
        for rranking in range(1, len(rauthor_list)+1):
            if comparing(dauthor_list[dranking-1],rauthor_list[rranking-1]):
                m['doi'] = doi
                m['author'] = dauthor_list[dranking-1]

                if dranking == 1:
                    m['dranking'] = "first"
                    tcount +=1
                elif dranking == 2:
                    m['dranking'] = "second"
                else:
                    if dranking <= p1:
                        m['dranking'] = "30%"
                    elif dranking > p1 and dranking <= p2:
                        m['dranking'] = "60%"
                    else:
                        m['dranking'] = "last"

                if rranking == 1:
                    m['rranking'] = "first"
                elif rranking == 2:
                    m['rranking'] = "second"
                else:
                    if rranking <= q1:
                        m['rranking'] = "30%"
                    elif rranking > q1 and rranking <= q2:
                        m['rranking'] = "60%"
                    else:
                        m['rranking'] = "last"
                author_information.append(m)
                break
        if m == {}:
            if dranking == 1:
                m['dranking'] = "first"
                tcount +=1
            elif dranking == 2:
                m['dranking'] = "second"
            else:
                if dranking <= p1:
                    m['dranking'] = "30%"
                elif dranking > p1 and dranking <= p2:
                    m['dranking'] = "60%"
                else:
                    m['dranking'] = "last"
            m['rranking'] = "not found"
            author_information.append(m)

R = ['first','second', '30%', '60%','last', 'not found']
output = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]

for item in author_information:
    for dranks in range(0, len(R)):
        for rranks in range(0,len(R)):
            if item['dranking'] == R[dranks] and item['rranking'] == R[rranks]:
                output[dranks][rranks] += 1
                break


print(tcount)
print(output)






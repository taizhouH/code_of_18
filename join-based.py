from copy import deepcopy
import math
import re
def data_set():
    data=[]
    with open ("E:\python学习\撸撸撸\instance.txt") as file:
        for item in file:
            item=item.strip("\n")
            data.append(list(map(str,item.split("\t"))))
    file.close()
    return data
#生成二阶关系模式
def create_instance(data):
    dist=[["AB"],["AC"],["AD"],["BC"],["BD"],["CD"],]
    length=len(data)
    i = 0
    x=0
    for item in range(length-1):
        if data[item][1] is "A":
            for j in range(length):
                if data[item][1] is not data[j][1] and data[j][1] is "B":

                    dist[0].append(data[item][1]+data[item][0]+data[j][1]+data[j][0])
                    a=float(data[item][2])-float(data[j][2])
                    b=float(data[item][3])-float(data[j][3])
                    dist[0].append(math.sqrt(a**2+b**2))
                if data[item][1] is not data[j][1] and data[j][1] is "C":

                    dist[1].append(data[item][1]+data[item][0]+data[j][1]+data[j][0])
                    a=float(data[item][2])-float(data[j][2])
                    b=float(data[item][3])-float(data[j][3])
                    dist[1].append(math.sqrt(a**2+b**2))
                if data[item][1] is not data[j][1] and data[j][1] is "D":

                    dist[2].append(data[item][1] + data[item][0] + data[j][1] + data[j][0])
                    a = float(data[item][2]) - float(data[j][2])
                    b = float(data[item][3]) - float(data[j][3])
                    dist[2].append(math.sqrt(a ** 2 + b ** 2))
            i = i + 1
    for item in range(i,length - 1):
        if data[item][1] is "B":
            i = i + 1
            for j in range(length):
                if data[item][1] is not data[j][1] and data[j][1] is "C":

                    dist[3].append(data[item][1]+data[item][0]+data[j][1]+data[j][0])
                    a=float(data[item][2])-float(data[j][2])
                    b=float(data[item][3])-float(data[j][3])
                    dist[3].append(math.sqrt(a**2+b**2))
                if data[item][1] is not data[j][1] and data[j][1] is "D":

                    dist[4].append(data[item][1]+data[item][0]+data[j][1]+data[j][0])
                    a=float(data[item][2])-float(data[j][2])
                    b=float(data[item][3])-float(data[j][3])
                    dist[4].append(math.sqrt(a**2+b**2))
    for item in range(i,length - 1):
        if data[item][1] is "C":
            i = i + 1
            for j in range(length):
                if data[item][1] is not data[j][1] and data[j][1] is"D":

                    dist[5].append(data[item][1]+data[item][0]+data[j][1]+data[j][0])
                    a=float(data[item][2])-float(data[j][2])
                    b=float(data[item][3])-float(data[j][3])
                    dist[5].append(math.sqrt(a**2+b**2))
    #this = len(dist[2])
    return dist
def is_apriori(dist):
    near_relation=4
    length=len(dist)
    length2=[]
    near={}
    for item in range(length):
        #length2.append(dist[item][0])
        length2.append(len(dist[item]))
    for item in range(length):
        for i in range(length2[item]):
            if isinstance(dist[item][i],(float)) and dist[item][i] > near_relation:
                dist[item][i] =None
                dist[item][i-1] =None
        #遍历拷贝dist，避免index错误
        for ite in dist[item][:]:
            if ite is None:
                dist[item].remove(ite)

    return dist

def colocation(dist):
    length=len(dist)
    j=0
    for item in range(length):
        length2=len(dist[item])

        for i in range(length2):

            if isinstance(dist[item][i],(str)):
                j=j+1
                #print("测试点")

    return j

data1=data_set()
data2=create_instance(data1)
data3=is_apriori(data2)
data4=colocation(data3)
print(data4)





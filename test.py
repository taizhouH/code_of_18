test=["AB","A1B3","A1B3","A2B4","AC"]
def data_set():
    data=[]
    with open ("E:\python学习\撸撸撸\instance.txt") as file:
        for item in file:
            item=item.strip("\n")
            data.append(list(map(str,item.split("\t"))))
    file.close()
    return data
#for i in range(len(test)):
    #if test[i] is str:

#实例计数
def count_instance(data):
    length = len(data)
    count=[]
    i=0
    for item in data:
        for ie in item:
            if ie is "A":
                i=i+1
            else:
                count.append(i)
                i=0
    return count
data=data_set()
count=count_instance(data)
print(count)



test6=[]
op=0
for item in range(len(data)):
    for i in range(len(data[item])-1):
        if data[item][i]==data[item][i+1]:
            op = op + 1
            test6.append(op)
        else:
            op = op + 1
#print(data)
test2=[]
t=0
test3=set()
test4=set(test[0])
test5=list(set(test))
test5.sort(key=test.index)
#test6=test5.sort()
for item in test:

    if isinstance(item,str):
        test3 = set(item)
        for i in test3:
            for j in range(len(test4)):
                if i in list(test4)[j]:
                    test2.append(item)
                    t = t + 1
                    tt = t / 7
                    print(tt)
print(list(test4)[1])
print(test5)
print(test2)
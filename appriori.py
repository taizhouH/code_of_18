def data_set():
    data=[]
    with open ("E:\python学习\撸撸撸\chouyang.txt") as file:
        for item in file:
            item=item.strip("\n")
            data.append(list(map(str,item.split(","))))
    file.close()
    return data

# 获取原数据，1项集
def create_Cand1(data_set):
    # 存在集合中
    Cand1 = set()
    for t in data_set:
        for item in t:
            # 把list中元素赋给不可变集合，再赋给set()
            item_set = frozenset([item])
            Cand1.add(item_set)
    return Cand1


# k项集
def create_Candk(Lksub1, k):
    Ck = set()
    len_Lksub1 = len(Lksub1)
    list_Lksub1 = list(Lksub1)
    for i in range(len_Lksub1):
        for j in range(1, len_Lksub1):
            l1 = list(list_Lksub1[i])
            l2 = list(list_Lksub1[j])
            l1.sort()
            l2.sort()
            # 排序后，判断k-2项集是否相同
            if l1[0:k - 2] == l2[0:k - 2]:
                Ck_item = list_Lksub1[i] | list_Lksub1[j]

                if is_apriori(Ck_item, Lksub1):
                    Ck.add(Ck_item)
    return Ck


# 产生频繁K项集
def generate_Lk(data_set, Candk, min_support, support_data):
    Lk = set()
    # 字典存储支持度计数
    item_count = {}
    # 计算支持度计数
    for t in data_set:
        for item in Candk:
            if item.issubset(t):
                if item not in item_count:
                    item_count[item] = 1
                else:
                    item_count[item] += 1
    t_num = float(len(data_set))
    # 判断是否满足最小支持度
    for item in item_count:
        if (item_count[item] / t_num) >= min_support:
            Lk.add(item)
            support_data[item] = item_count[item] / t_num
    return Lk


# 先验剪枝
def is_apriori(Ck_item, Lksub1):
    for item in Ck_item:
        sub_Ck = Ck_item - frozenset([item])
        if sub_Ck not in Lksub1:
            return False
    return True


# 生成频繁项集和支持度
def generate_L(data_set, k, min_support):
    support_data = {}
    C1 = create_Cand1(data_set)
    L1 = generate_Lk(data_set, C1, min_support, support_data)
    Lksub1 = L1.copy()
    L = []
    L.append(Lksub1)
    for i in range(2, k + 1):
        Ci = create_Candk(Lksub1, i)
        Li = generate_Lk(data_set, Ci, min_support, support_data)
        Lksub1 = Li.copy()
        L.append(Lksub1)
    return L, support_data


# 规则生成
def generate_connected_rules(L, support_data, min_conf):
    connected_rule = []
    sub_set_list = []
    # 判断是否满足最小置信度阈值
    for i in range(0, len(L)):
        for freq_set in L[i]:
            for sub_set in sub_set_list:
                if sub_set.issubset(freq_set):
                    conf = support_data[freq_set] / support_data[freq_set - sub_set]
                    big_rule = (freq_set - sub_set, sub_set, conf)
                    if conf >= min_conf and big_rule not in connected_rule:
                        connected_rule.append(big_rule)
            sub_set_list.append(freq_set)
    return connected_rule



if __name__ == "__main__":
    data_set = data_set()
    L, support_data = generate_L(data_set, k=2, min_support=0.01)
    connected_rule = generate_connected_rules(L, support_data, min_conf=0.5)
    for Lk in L:

        print("-"*50)
        print("频繁" + str(len(list(Lk)[0])) + "-项集\t支持度")
        print("-"*50)
        for freq_set in Lk:
            print(freq_set, support_data[freq_set])
    print('')
    print("关联规则生成")
    for item in connected_rule:
        print(item[0], "->", item[1], "置信度: ", item[2])

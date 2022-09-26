import sys, os
sys.path.append(os.curdir)

num = 100
silo = 4
attr_num = 1
for i in range(silo):
    with open("./data/anti_{}_{}_{}-P{}-0".format(num, silo, attr_num, i), "r") as f:
    # with open("./data/example/test_s{}".format(i), "r") as f:    
        with open("./Player-Data/Input-P{}-0".format(i), "w") as fq:
            a = f.readlines()
            # print(map(int, a))
            # 把a中的每个元素转化为int型
            a = list(map(int, a))
            # print(a)
            l = len(a)
            # l = 5
            print(l)
            cnt = 0
            # 得到了a[i] 与 a[j]两两比较的结果
            for i in range(l):
                for j in range(i + 1, l):
                    cond1 = 1 if a[i] < a[j] else 0
                    cond2 = 1 if a[i] > a[j] else 0
                    fq.write("{} {}\n".format(cond1, cond2,))
                    cond1 = 1 if a[j] < a[i] else 0
                    cond2 = 1 if a[j] > a[i] else 0
                    fq.write("{} {}\n".format(cond1, cond2))
                    cnt += 2


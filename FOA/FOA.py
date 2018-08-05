import numpy as np
import matplotlib.pyplot as plt

def Fitness(x):
    return x**2 - 5

def FOA(maxgen,sizepop):
    # 随机初始果蝇位置
    X_axis = 10 * np.random.rand()
    Y_axis = 10 * np.random.rand()

    # 果蝇寻优开始，利用嗅觉寻找食物
    X = []
    Y = []
    D = []
    S = []
    Smell = []
    for i in range(sizepop):
        # 赋予果蝇个体利用嗅觉搜寻食物之随机方向与距离
        X.append(X_axis + 2 * np.random.rand() - 1)
        Y.append(Y_axis + 2 * np.random.rand() - 1)

        # 由于无法得知食物位置，因此先估计与原点的距离（Dist），再计算味道浓度判定值（S），此值为距离的倒数
        D.append((X[i]**2 + Y[i]**2)**0.5)
        S.append(1 / D[i])

        # 味道浓度判定值（S）代入味道浓度判定函数（或称为Fitness function），以求出该果蝇个体位置的味道浓度（Smell(i))
        Smell.append(Fitness(S[i]))

    # 找出此果蝇群里中味道浓度最低的果蝇（求极小值）
    bestSmell, bestindex = min(Smell),Smell.index(min(Smell))

    # 保留最佳味道浓度值与x，y的坐标，此时果蝇群里利用视觉往该位置飞去
    X_axis = X[bestindex]
    Y_axis = Y[bestindex]
    Smellbest = bestSmell

    # 果蝇迭代寻优开始
    yy = []
    Xbest = []
    Ybest = []
    for g in range(maxgen):
        # 赋予果蝇个体利用嗅觉搜寻食物的随机方向和距离
        for i in range(sizepop):
            # 赋予果蝇个体利用嗅觉搜寻食物之随机方向与距离
            X[i] = X_axis + 2 * np.random.rand() - 1
            Y[i] = Y_axis + 2 * np.random.rand() - 1

            # 由于无法得知食物位置，因此先估计与原点的距离（Dist），再计算味道浓度判定值（S），此值为距离的倒数
            D[i] = (X[i]**2 + Y[i]**2)**0.5
            S[i] = 1 / D[i]

            # 味道浓度判定值（S）代入味道浓度判定函数（或称为Fitness function），以求出该果蝇个体位置的味道浓度（Smell(i))
            Smell[i] = Fitness(S[i])

        # 找出此果蝇群里中味道浓度最低的果蝇（求极小值）
        bestSmell, bestindex = min(Smell),Smell.index(min(Smell))

        # 判断味道浓度是否优于前一次迭代味道浓度，若是则保留最佳味道浓度值与x，y的坐标，此时果蝇群体利用视觉往该位置飞去
        if bestSmell < Smellbest:
            X_axis = X[bestindex]
            Y_axis = Y[bestindex]
            Smellbest = bestSmell

        # 每次最优Semll值记录到yy数组中，并记录最优迭代坐标
        yy.append(Smellbest)
        Xbest.append(X_axis)
        Ybest.append(Y_axis)

    return yy, Xbest, Ybest

maxgen = 200
sizepop = 50
yy, Xbest, Ybest = FOA(maxgen,sizepop)
ax1 = plt.subplot(121)
ax1.plot(yy)
ax1.set(xlabel = 'Iteration Number',ylabel = 'Smell',title = 'Optimization process')
ax2 = plt.subplot(122)
ax2.plot(Xbest,Ybest)
ax2.set(xlabel = 'X-axis',ylabel = 'Y-axis',title = 'Fruit fly flying route')
plt.show()


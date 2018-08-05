from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(0)

def FF(X):
    # return (4-2.1*(X[0]**2)+(X[0]**4)/3)*(X[0]**2)+X[0]*X[1]+(-4+4*(X[1]**2))*(X[1]**2)
    return (X[0])**2 + X[1]**2
def MFOA(kmax,M,Popsize,dim,a,b,phi):
    """
    多群果蝇搜索算法
    kmax：最大迭代次数
    M：子种群数量
    Popsize：子群人口
    dim：搜索空间的维度
    a,b：每个搜索维度的上下区间，这里首先设置成每个维度都是一样的
    phi：算法中迭代参数
    """

    X = np.empty((M,Popsize,dim),dtype='float32')# 每只果蝇的在空间的位置
    Smell = np.empty((M,Popsize),dtype='float32')# 每只果蝇在空间中嗅探的气味
    bestSmellm = np.empty(M,dtype='float32')# 某次迭代每个种群最好的气味
    bestIndexm = np.empty(M,dtype='int')# 某次迭代每个种群最好的气味在该种群中的索引
    Smellbestm = np.empty(M,dtype='float32')# 当前迭代所有种群中最好的气味
    X_axism = np.empty((M,dim),dtype='float32')# 当前迭代所有种群中最好的气味的位置
    Smellbest = np.empty(1,dtype='float32')
    X_axis = np.empty(dim,dtype='float32')
    # 循环迭代
    for k in range(kmax):
        R = ((b-a)/2)*(((kmax-k)/kmax)**phi)
        # 种群间循环
        for m in range(M):
            # 个体间循环
            for i in range(Popsize):
                X[m,i] = X_axism[m] + R * np.random.rand(dim)
                Smell[m,i] = FF(X[m,i])
            bestSmellm[m], bestIndexm[m] = np.min(Smell[m]),np.argmin(Smell[m])# np.argmin()只返回第一次出现的最大值的索引
            Smellbestm[m] = bestSmellm[m]
            X_axism[m] = X[m,bestIndexm[m]]
            if Smellbestm[m] < Smellbest:
                Smellbest = Smellbestm[m]
                X_axis = X_axism[m]
            X_new = np.mean(X_axism,axis=0)
            if FF(X_new) < Smellbest:
                Smellbest = FF(X_new)
                X_axis = X_new

    return Smellbest,X_axis,X_axism

Smellbest, X_axis,X_axism = MFOA(1000,2,30,2,20,-20,6)
print(Smellbest)
print(X_axis)
print(X_axism)

# x = np.linspace(-2,2,100)
# y = np.linspace(-2,2,100)
# X,Y = np.meshgrid(x,y)
# Z = F1(X,Y)
#
# fig = plt.figure()
# ax =plt.axes(projection='3d')
# ax.plot_wireframe(X,Y,Z)
# plt.show()
# maxgen = 200
# sizepop = 50
# yy, Xbest, Ybest = FOA(maxgen,sizepop)
# ax1 = plt.subplot(121)
# ax1.plot(yy)
# ax1.set(xlabel = 'Iteration Number',ylabel = 'Smell',title = 'Optimization process')
# ax2 = plt.subplot(122)
# ax2.plot(Xbest,Ybest)
# ax2.set(xlabel = 'X-axis',ylabel = 'Y-axis',title = 'Fruit fly flying route')
# plt.show()


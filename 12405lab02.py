import matplotlib
import numpy as np
import matplotlib.pyplot as plt


class RandomWalk :
    def __init__(self,position):
        self.pos=position

    def walk(self):
        if np.random.randint(0,2)==1 :
            self.pos=self.pos+1
        else:
            self.pos = self.pos - 1
        return self.pos
    def steps(self,step_size):
        a =np.zeros(step_size)
        for i in range(0,step_size):
            a[i]=self.walk()
        return a




matplotlib.rc('xtick', labelsize=30)
matplotlib.rc('ytick', labelsize=30)
matplotlib.rc('axes', titlesize=30)
matplotlib.rc('legend', fontsize=10)

fig=plt.figure(figsize=(10,10))
fig.subplots_adjust(hspace=.5)
man1 = RandomWalk(np.random.randint(1,11))
man2 = RandomWalk(np.random.randint(1,11))
axes1 = plt.subplot(3,1,1)
axes2 = plt.subplot(3,1,2)
axes3 = plt.subplot(3,1,3)
x = np.linspace(0,500,500)
y1=man1.steps(500)
y2=man2.steps(500)
axes1.plot(x,y1, color='r')
axes2.hist(y1,bins=20,color='r')
axes3.scatter(y1,y2,color="green",alpha=0.3,edgecolors="grey")
plt.show()

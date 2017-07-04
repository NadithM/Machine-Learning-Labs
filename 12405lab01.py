import numpy as np
class MatMan :
    def __init__(self,matrix):
        self.mat=matrix

    def getcov(self):
        return np.sqrt(np.sum(np.power((self.mat-(np.tile(np.mean(self.mat,0),self.mat.shape[0])).reshape(self.mat.shape[0],self.mat.shape[1])),2),0)/(self.mat.shape[0]-1))



if __name__ == "__main__":
    matman_object= MatMan(np.genfromtxt('labExercise01.csv', delimiter=','))
    print 'Sn = ',matman_object.getcov()



import numpy as np
from matplotlib import pyplot as plt
from sympy import *

"""
my E number =e12405
which turn out my function is just a y=mx
 f(x)=-4
 
So i took some random function since theres no point of doing lab to above function
f(x)=0.2 x^3 + x^2 + x + 8

Ex.2 

        Actually selecting a initial value directly depend on the behaviour of the function.before selecting a a intial value we must
        have some idea of of the behaviour of the function to choose a good initial value.
        depend on the grad value and learning rate, it will be decided how many iterataion will it take to come to minima.
        so, if its a function where u have a grad values close to 0.0 its is batter to choose a intial value close to minima of function or...use a high learning rate
        
         
Ex.3
        we see that we make an update to the parameters by taking gradient of the parameters. And multiplying it by a learning rate, 
        which is essentially a constant number suggesting how fast we want to go the minimum. Learning rate is a hyper-parameter and
        should be treated with care when choosing value of learning rate wether its a realtively high value a low value according to the function behaviour
         
         
Ex. 4
        parameters are set like below
        function = 0.2 * x ** 3 + x ** 2 + x + 8
        learning_rate = 0.01
        precision = 1.0 / 10000
        current_x= 1
        ('value of current_x (minima):', -0.612596509584458)
        
        the function I got have minima some where around -0.61
        
        its clear that when u choose high learning rate like 10.0 (figure two) in the graph.sometimes you will be unble to find a minima if there is a one.
        so choosing a good learning rate is also important

 
"""
x = Symbol('x')

def GDA(function,current_x,learning_rate,iterationsMax,precision,maxDivergence):
        yprime = function.diff(x)
        iterations = 0
        check = 0
        while True:
                next_x = current_x - learning_rate * N(yprime.subs(x, current_x)).evalf()
                iterations += 1
                if iterations > iterationsMax:
                        print("Maximum iterations is reached.")
                        return next_x
                if current_x < next_x:
                        check += 1
                        if check > maxDivergence:
                                print("The value of current_x is diverging")
                                print("Please choose a smaller learning_rate and check that the function behavior first")
                                return next_x
                if abs(current_x - next_x) < precision:
                        break

                current_x = next_x
        return current_x

if __name__ == "__main__":

        plt.subplots_adjust(hspace=0.57)
        axes1 = plt.subplot(2,1, 1)
        axes2 = plt.subplot(2,1, 2)
        # Function
        function = 0.2 * x ** 3 + x ** 2 + x + 8
        learning_rate = 1
        iterationsMax = 10000
        precision = 1.0 / 10000
        maxDivergence = 500
        current_x= 1

        print("Calculating minima for leaning rate=0.01...")
        minima = GDA(function,current_x,learning_rate,iterationsMax,precision,maxDivergence)
        print("Calculation is finished")
        if minima == nan :
                print "\n"
        else:
                print("value of current_x (minima):", minima)
                domain = np.linspace(-2, 2, 1000)
                codomain = np.array([N(function.subs(x, value)) for value in domain])
                axes1.plot(domain, codomain, color='r',label='f(x)')
                axes1.set_title("Behavior of f(x)=0.2 x^3 + x^2 + x + 8\n Learning rate = 0.01")
                domain = [minima]
                codomain = np.array([N(function.subs(x, value)) for value in domain])
                axes1.plot(domain, codomain, color='g', marker="*",label='Minima of f(x)')

        print("Calculating minima for leaning rate=10.0   .......")
        learning_rate = 10.0
        minima = GDA(function, current_x, learning_rate, iterationsMax, precision, maxDivergence)
        print("Calculation is finished")
        if minima == nan :
                print "\n"
        else:
                print("value of current_x (minima):", minima)
                domain = np.linspace(-2, 2, 1000)
                codomain = np.array([N(function.subs(x, value)) for value in domain])
                axes2.plot(domain, codomain, color='r',label='f(x)')
                axes2.set_title("Behavior of f(x)=0.2 x^3 + x^2 + x + 8\n Learning rate = 10.0")
                domain = [minima]
                codomain = np.array([N(function.subs(x, value)) for value in domain])
                axes2.plot(domain, codomain, color='g', marker="*",label='Minima of f(x)')

        plt.show()
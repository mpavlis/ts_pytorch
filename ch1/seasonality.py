import matplotlib.pyplot as plt
import random
from math import sin

def generate_random_walk(length=100, mu=0, sig=1):
    ts=[]
    for i in range(length):
        e = random.gauss(mu, sig)
        if i == 0:
            ts.append(e)
        else:
            ts.append(ts[i-1]+e)
    return ts

if __name__ == '__main__':
    random.seed(10)
    length=100
    A=50
    B=-0.05
    C=1
    S=3
    trend=[A+B*i for i in range(length)]
    seasons = [S*sin(i/5) for i in range(length)]
    noise=[C*random.gauss(0,1) for _ in range(length)]
    ts=[trend[i] + noise[i] + seasons[i] for i in range(length)]
    #random_walk = generate_random_walk(100)
    plt.plot(ts)
    plt.plot(trend)
    #plt.plot(random_walk)
    plt.show()
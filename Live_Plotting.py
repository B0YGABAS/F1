import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

x=[0]
y=[random.randrange(200)]

def animate(m):
    x.append(x[-1]+1)
    y.append(random.randrange(200))
    plt.cla()
    plt.plot(x,y)
    #pass

ani = animation.FuncAnimation(plt.gcf(), animate, interval=100)
plt.show()
#print(y)
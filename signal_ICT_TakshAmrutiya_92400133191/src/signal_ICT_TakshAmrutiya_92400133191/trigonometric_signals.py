import matplotlib.pyplot as plt 
import numpy as np

def sine_wave(A,f,phi,t) :
    x = np.arange(-t,t+1,1/50)
    y = A*np.sin(2*np.pi*f*x + phi)
    signal = np.column_stack((x,y)) 
    plt.title('sine_wave')
    plt.plot(x,y)
    plt.show()
    return signal

def cosine_wave(A,f,phi,t) :
    x = np.arange(-t,t+1,1/50)
    y = A*np.cos(2*np.pi*f*x + phi)
    signal = np.column_stack((x,y)) 
    plt.title('cosine_wave')
    plt.plot(x,y)
    plt.show()
    return signal

def exponential_signal(A,a,t) :
    x = np.arange(0,t+1,1/50)
    y = A*np.exp(a*x)
    plt.title('exponential_signal')
    signal = np.column_stack((x,y)) 
    plt.plot(x,y)
    plt.show()
    return signal




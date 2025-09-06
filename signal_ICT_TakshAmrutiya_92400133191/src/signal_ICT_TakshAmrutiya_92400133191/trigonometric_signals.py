import matplotlib.pyplot as plt
import numpy as np
from numpy import *

#Logic of sinWave:
#how we can create sinwave?
#Ans:The general formula is y=A*sin(wt+phi),where w=omega=2*pi*f,phi is basically 
# phase shift it is denoted in radin.
def sinWave(A,f,phi,t):
    #here t is 1D array
    y=A*sin((2*pi*f*t)+phi)
    # in output y is also an array
    plt.plot(t, y)
    plt.title(f"Sine Wave: A={A}, f={f}Hz, φ={phi} rad")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    return y
    
#Logic of coswave is same as sinwave
def cosWave(A,f,phi,t):
    #here t is 1D array
    y=A*cos((2*pi*f*t)+phi)
    # in output y is also an array
    plt.plot(t, y)
    plt.title(f"Sine Wave: A={A}, f={f}Hz, φ={phi} rad")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    return y


#Logic of exponential_signal
#How to create exponential_signal?
#Ans:using this formula we can create y=A*e^at,where A is amplitude,a=constant,t=time
def exponentialSignal(A,a,t):
    #here t is a 1D array
    y=A*exp(a*t)
    #o/p y is also an array
    plt.plot(t, y)
    plt.title("Exponential_signal")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    return y
import matplotlib.pyplot as plt
import numpy as np

#Logic of timeshifting
#according to k value signal will move on right side or left side
def timeShift(signal,n,k):
        new=n+k#here we are shifting
        plt.stem(new, signal)
        plt.title("Shifted Signal")
        plt.show()
        plt.xlabel("n")
        plt.ylabel("x[n]")
        plt.grid(True)
        plt.show()
        return signal
        
        
#Logic of timescaling
def time_scale(signal, n, k):
    new = k*n#here we are shifting
    plt.stem(new, signal)
    plt.title("Time-Scaled Signal")
    plt.xlabel("n")
    plt.ylabel("x[n]")
    plt.grid(True)
    plt.show()
    return signal


#Logic of signal addition
def signal_addition(signal1, signal2,n):
    if(len(signal1) != len(signal2)):
        print("Not valid!")  
    add= signal1 + signal2  # here we are doing addition
    plt.stem(n,add)
    plt.title("Added Signal")
    plt.xlabel("n")
    plt.ylabel("x1[n] + x2[n]")
    plt.grid(True)
    plt.show()
    return add

#Logic of signal multiplication 
def signal_multiplication(signal1, signal2,n):
    if(len(signal1) != len(signal2)):
        print("Not valid!")  
    multi= signal1 * signal2  # here we are doing addition
    plt.stem(n,multi)
    plt.title("multiplied Signal")
    plt.xlabel("n")
    plt.ylabel("x1[n] * x2[n]")
    plt.grid(True)
    plt.show()
    return multi

        
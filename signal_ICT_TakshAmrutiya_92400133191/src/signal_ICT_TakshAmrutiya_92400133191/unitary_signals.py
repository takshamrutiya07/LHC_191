import matplotlib.pyplot as plt 
import numpy as np

def unit_step(n) :
    x = np.arange(-n,n+1)#arranging -n to +n for x axis
    # print(x)
    step_func = []
    for i in x :
        if i>=0 :
            step_func.append(1)
        else :
            step_func.append(0)
    step_func = np.array(step_func)
    y = step_func
    signal = np.column_stack((x,y)) 
    plt.title('UnitStep Function')
    plt.stem(x,y)
    plt.show()
    # print(step_func)
    return signal

def unit_impulse(n) : 
    x = np.arange(-n,n+1)#arranging -n to +n for x axis
    impulse_func = []
    for i in x :
        if i==0 :
            impulse_func.append(1)
        else : 
            impulse_func.append(0)
    impulse_func = np.array(impulse_func)
    y = impulse_func
    signal = np.column_stack((x,y)) 
    plt.title('UnitImpulse Function')
    plt.stem(x,y)
    plt.show()
    return signal

def ramp_signal(n) :
    x = np.arange(-n,n+1)#arranging -n to +n for x axis
    ramp_func = []
    for i in x :
        if i<=0 :
            ramp_func.append(0)
        else :
            ramp_func.append(i)
    ramp_func = np.array(ramp_func)
    y = ramp_func
    signal = np.column_stack((x,y)) 
    # print(ramp_func)
    plt.title('Ramp Function')
    plt.stem(x,y)
    plt.show()
    return signal

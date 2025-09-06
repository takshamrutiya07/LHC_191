import matplotlib.pyplot as plt
import numpy as np

#here is the logic of the unitStep function
#What is the work of unitStep function?
#Ans:The unitstep function give amplitude value 1, when the input value is >=0,else it give 
#amplitude value 0,And the unitstep signal is a descrete time signal.
def unitStep(n):
    result=[]
    #this for loop will tells us when the o/p should be 1 or 0.
    for value in n:
        if(value<0):
            result.append(0)
        else:
            result.append(1)
    plt.plot()
    #The unitStep signal is a descrete time signal so we have to generate descrete plot
    #for that reason we use stem function.
    plt.stem(n,result)
    plt.title("Unit Step Signal")
    plt.xlabel('n')
    plt.ylabel('u[n]')
    plt.show()
    return result


#Logic of unitImpulse Function.
#What is unitImpulse Function?
#Ans:The unit Impulse Function Give amplitude 1 when the i/p is 0,else it give amplitude 0.
def unitImpulse(n):
    result=[]
    for i in n:
        if(i==0):
            result.append(1)
        else:
            result.append(0)
    plt.plot()
    #unitImpulse signal is descrete time signal.
    plt.stem(n,result)
    plt.title("Unit Impulse Function")
    plt.xlabel('n')
    plt.ylabel('impulse[n]')
    plt.show()
    return result
    
   
#Logic of Ramp signal
#What is ramp signal?
#Ans:ramp signal gives output when the time>=0 by this formula:r[t]=a*t,else it give 0.
def rampSignal(t,a):
    result=[]
    for i in t:
        if(i<0):
            result.append(0)
        else:
            result.append(a*i)
    plt.plot(t,result)
    plt.show()
    return result
            

    

    
    

#This program shows the steps of the collatz-algorithm with the number z
def collatz(z):
    print("The number to calculate is",z)
    i=0
    while z!=1:
        #the collatz algorithm is executed and the number of steps is indicated by "i"
        if z%2 ==0:
            z=z//2
            i=i+1
            print("step",i,"even number")
            print(z)
            
        else:
            z=z*3+1
            i=i+1
            print("step",i,"uneven number")
            print(z)
    return i
A=collatz(17)
print("The number of steps the algorithm needs with number 17 is", A)

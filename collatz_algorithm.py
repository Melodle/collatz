#This program shows the steps of the collatz-algorithm with the number z
def collatz(z):
    i=0
    while z!=1:    
        #the collatz algorithm is executed and the number of steps is indicated by "i"
        if z%2 ==0:
            z=z//2
            i=i+1
        else:
            z=z*3+1
            i=i+1
    return i

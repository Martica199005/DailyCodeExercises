
# Given a list of numbers and a number k
# return whether any 2 numbers
#from the list add up to k

a=[10,15,3,7]
k=17

def sum1K(a, c):  #it is an easier case
    for i in range(1,len(a)):
        if a[0]+a[i]==c:
            return str(a[0])+"+"+str(a[i])+"="+str(c)
        else:
            i=i+1
    return False

def sumK(a, c):    #this is the exercise
    for j in range(0,len(a)-1):
        for i in range(1,len(a)):
            if a[j]+a[i]==c:
                 return str(a[j])+"+"+str(a[i])+"="+str(c)
            else:
                i=i+1
        j=j+1
    return False
        

print(sum1K(a,k))
print(sumK(a,18))
print(sumK(a,14))
print(sumK(a,10))






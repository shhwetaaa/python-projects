
def calc_mean(a,b):
    mean = (a*b)/(a+b)
    print(mean)
    
    
    
def isgreater(a,b):
    if a>b:
        print("first number is greater")
    else:
        print("second one is greater")  
    
a=5
b=5
calc_mean(a,b)   
isgreater(a,b) 





c=10
d=10
isgreater(c,d) 
calc_mean(c,d)    
def islesser(a,b):
   pass



# add two number
def add(numone , numtwo):
    return numone + numtwo
    
print(add(5,5)) 
    
    
    
    
    
    
    # for area and circumference of a circle
def calc_cir(r):
    areea = r*r*3.14      
    circum = 2*3.14*r
    return(areea , circum)
    
r = 10
print(calc_cir(r))   







# default parameter value
def greet(gr):
    n = len(gr)
    if n > 0 :
        print("good morning " ,gr)
    else:
        gr = "shweta"   
        print("good morning" , gr) 
        
        
gr = input("enter your name")   
greet(gr)     
 

 
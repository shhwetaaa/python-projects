def cc_coder(num):
     def actual(x):
         return x ** num
     return actual
 
f = cc_coder(2)
g = cc_coder(3)

print(f)
print(g)

print(f(5))
print(g(6))



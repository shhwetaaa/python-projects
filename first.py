print("shweta,shwey,shwet")
print("first  last middle end")

#datatypes and conversion
 

#string
f_name = "ABC"
f_name = 'ABC_'
print(f_name)


#string slicing
print(f_name[1:-1])

#reversing the string
print(f_name[::-1])

#reverse by using  built in methods
f_name = "".join(reversed(f_name))
print(f_name)

n = [1,2,3]
m = [1,2,3]
print(m==n)
print(m is n)
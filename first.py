print("shweta,shwey,shwet")
print("first  last middle end")

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


#deleting and updating of a string

String1 = "hello devils!"
print(String1)

 String2 = "S"
 String3 = String1[0:6] + String2 + String1[7:]
 print(String3)
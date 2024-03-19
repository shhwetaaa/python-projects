# weight converter in python

weight = float(input("enter your weight"))
unit = print("kindly enter your preferable mass unit")

if unit == "kg" :
    weight = weight*2.20462
    print(weight + "pounds")
elif unit== "pounds":
    weight = weight * 0.453592
    print(weight + "pounds")
        

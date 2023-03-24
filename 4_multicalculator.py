import math
x1= input("enter x1: ")
x2= input("enter x2: ")
x3= input("enter x3: ")

while True:
    mean= (int(x1) + int(x2) + int(x3))/3
    t1 = int(x1)-mean
    t2 = int(x2)-mean
    t3 = int(x3)-mean
    t= (int(t1)**2)+(int(t2)**2)+(int(t3)**2)
    d= int(t)/3
    sd= math.sqrt(d)
#3. output
    print (f"sd: {sd}")
    res = input("Continue? (Y/N) ")
    if res.upper()[0] == "N":
        break;
print("hello world")

def mySum(a,b):
    if isinstance(a,int) and isinstance(b,int):
        return a+b
print(mySum(1,3))


def mySub(a,b):
    if isinstance(a,int) and isinstance(b,int):
        return a-b
print(mySub(1,3))


def myMulti(a,b):
    if isinstance(a,int) and isinstance(b,int):
        return a*b
print(myMulti(1,3))


def myDivide(a,b):
    try:
        if isinstance(a,int) and isinstance(b,int):
            return a/b 
        else:
            print("valed sisestatud numbrid")
    except ZeroDivisionError:
        print("ei saa jagada nulliga")
print(myDivide(1,3))

de          a = int(input("sisesta number 1:"))
            b = int(input("sisesta number 2:"))
            result=mySub(a,b)
            print("Vastus: ",a, "-",b,"=",result)
        elif valik == "3":
            a = int(input("sisesta number 1:"))
            b = int(input("sisesta number 2:"))
            result=myMulti(a,b)
            print("Vastus: ",a, "*",b,"=",result)
        elif valik == "4":
            a = int(input("sisesta number 1:"))
            b = int(input("sisesta number 2:"))
            result=myDivide(a,b)
            print("Vastus: ",a, "/",b,"=",result)
        elif valik == "5":
            break
        else:
            print("seda valikut pole")

main()

def DisplayInfo():
    print("kokku oli:", sum(myArr))
    print("liitmine toimis:",myArr[0], "korda")
    print("lahutamine toimis:",myArr[1], "korda")
    print("korrutamine toimis:",myArr[2], "korda")
    print("jagamine toimis:",myArr[3], "korda")
       
myArr=[0,0,0,0]
DisplayInfo()
    f main():
    while True:
        valik = input("mida sa tahad? kui tahad liita vali 1, kui lahutada vali 2,  kui tahad korrutada vali 3 ning kui tahad jagada vali 4")
        if valik == "1":
            a = int(input("sisesta number 1:"))
            b = int(input("sisesta number 2:"))
            result=mySum(a,b)
            print("Vastus: ",a, "+",b,"=",result)
        elif valik == "2":
            a = int(input("sisesta number 1:"))
            b = int(input("sisesta number 2:"))
            result=mySub(a,b)
            print("Vastus: ",a, "-",b,"=",result)
        elif valik == "3":
            a = int(input("sisesta number 1:"))
            b = int(input("sisesta number 2:"))
            result=myMulti(a,b)
            print("Vastus: ",a, "*",b,"=",result)
        elif valik == "4":
            a = int(input("sisesta number 1:"))
            b = int(input("sisesta number 2:"))
            result=myDivide(a,b)
            print("Vastus: ",a, "/",b,"=",result)
        elif valik == "5":
            break
        else:
            print("seda valikut pole")

main()

def DisplayInfo():
    print("kokku oli:", sum(myArr))
    print("liitmine toimis:",myArr[0], "korda")
    print("lahutamine toimis:",myArr[1], "korda")
    print("korrutamine toimis:",myArr[2], "korda")
    print("jagamine toimis:",myArr[3], "korda")
       
myArr=[0,0,0,0]
DisplayInfo()
    

    
    
    
    
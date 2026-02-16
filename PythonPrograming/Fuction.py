def printdata():
   print("Hello World")

printdata()

def printdata2(name):
   print("hello",name)


printdata2("arun")
printdata2("sarthak")
printdata2("piyush")

def sq(num):
   return num**2

print("square: ",sq(5))


def pallindrom(String):
    dupl = String[::-1]   # reverse the string

    if String == dupl:
        print("palindrom")
    else:
        print("not palindrom")


pallindrom("racecar")

# function calling a another function

def areaofrect(len, width):
    return len * width


def areaofsq(side):
    return side * side


value = areaofrect(4, 6)
sq = areaofsq(value)

print(sq)

def limit(num):
    even=list(range(2,num+1,2))
    print(even)

limit(10)

def cal(a,b):
    return a+b,a-b,a*b,round(b/a,2)

add,sub,mul,div = cal(3,4)
print(add)
print(sub)
print(mul)
print(div)
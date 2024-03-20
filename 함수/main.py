def add(a, b): 
    return a + b

def say(): 
    return 'Hi' 

def add_no_return(a, b): 
    print("%d, %d의 합은 %d입니다." % (a, b, a+b))
    
    
add_no_return(1,3)


a=input("아무말이나 입력하세요\n")
b=input("또 아무말이나 입력하세요\n")
c=add(a,b)
print(c)
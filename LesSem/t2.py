enter= int(input("Enter your number:"))

def f(n):
    if n-1==0:
        return 0
    elif n-1 in (1,2):
        return 1
    return f(n-1)+f(n-2)

res=f(enter)
print(res)
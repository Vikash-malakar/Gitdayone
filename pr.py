from functools import reduce
nums = [1,2,3,4,5]
ans= list(map(lambda x:x**3,nums))
print(ans)

letters = ['a','b','c','d']
ans=list(map( lambda x:x.upper(),letters))
print(ans)

names = ['vikas','rahul','aman']
ans=list(map(lambda x: x.title(),names))
print(ans)



tem=[25,30,35,40]
# F = (C * 9/5) + 32
ans=list(map(lambda x: (x* 9/5)+32,tem))
print(ans)

# Number generator from 1 to 5
def gen():
    for i in range(1,6):
        yield i

for x in gen():
    print(x)






def outer(func):
    def inner():
        print("Before function")
        func()
        print("After function")
    return inner

@outer
def say():
    print("Hello World")

say()










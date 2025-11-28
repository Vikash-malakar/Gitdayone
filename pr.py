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


















# PS C:\Users\Dell\OneDrive\Desktop\GitHUb> git init .
# Initialized empty Git repository in C:/Users/Dell/OneDrive/Desktop/GitHUb/.git/
# PS C:\Users\Dell\OneDrive\Desktop\GitHUb> git add .
# PS C:\Users\Dell\OneDrive\Desktop\GitHUb> git commit --m "day1"
# [master (root-commit) 051dec5] day1       
#  1 file changed, 54 insertions(+)
#  create mode 100644 pr.py
# PS C:\Users\Dell\OneDrive\Desktop\GitHUb> git remote add origin https://github.com/Vikash-malakar/Gitdayone.git
# PS C:\Users\Dell\OneDrive\Desktop\GitHUb> git push origin main
# error: src refspec main does not match any
# error: failed to push some refs to 'https://github.com/Vikash-malakar/Gitdayone.git'
# PS C:\Users\Dell\OneDrive\Desktop\GitHUb> git remote add origin https://github.com/Vikash-malakar/Gitdayone.git
# error: remote origin already exists.
# PS C:\Users\Dell\OneDrive\Desktop\GitHUb> git push origin HEAD
# Enumerating objects: 3, done.
# Counting objects: 100% (3/3), done.
# Delta compression using up to 4 threads
# Compressing objects: 100% (2/2), done.
# Writing objects: 100% (3/3), 553 bytes | 276.00 KiB/s, done. 
# Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
# To https://github.com/Vikash-malakar/Gitdayone.git
#  * [new branch]      HEAD -> master
# PS C:\Users\Dell\OneDrive\Desktop\GitHUb> 










# MRO - Method Resolution Order
class A:
    num = 100
    
class B(A):
    num = 10

class C(A):
    num = 1

class D(B, C):
    pass

print(D.num)
print(D.mro())

# Depth First Search
# https://www.srikanthtechnologies.com/blog/python/mro.aspx

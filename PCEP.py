def func(x,y):
    if x==y:
        return x
    else:
        print("This is value of y \t:",y-1)
        return func(x,y-1)
print(func(0,3))

##def fun(x):
##    if x%2==0:
##        return 1
##    else:
##        return 2
##print(fun(2))
##print(fun(fun(2)))

##dd={"1":"0","0":"1"}
##for x in dd.vals():
##    print(x,end="")

##my_list=[1,2]
##for v in range(2):
##    my_list.insert(-1,my_list[v])
##print(my_list)

##value=input("Enter value\t:")
##print(int(value)/len(value))

##a=1
##b=0
##a=a^b
##print(a)
##b=a^b
##print(b)
##a=a^b
##print(a,b)

##l=[[x for x in range(3)] for y in range(3)]
##print(l)
##for r in range(3):
##    print("The r is\t:",end="")
##    print(r)
##    for c in range(3):
##        print("The c is \t:",end="")
##        print(c)
##        print("The list element is\t:",end="")
##        print(l[r][c])
##        if l[r][c]%2!=0:
##            print('#')

##tup=(1,2,4,8)
##tup=tup[-2:-1]
##tup=tup[-1]
##print(tup)

##d={'one':'two','three':'one','two':'three'}
##v=d['three']
##for k in range(len(d)):
##    v=d[v]
##print(v)

##nums=[1,2,3]
##vals=nums
##print(vals)
##print(nums)

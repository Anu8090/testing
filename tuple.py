#create simple tuple with multiple integer
a=(4,8,6,5,4)
print(a)
print(type(a))


#create simple tuple with multiple string values
a=("hello","python","tuple")
print(a)
print(type(a))

#create simple tuple with multiple float values
a=(3.6,4.6,7.4)
print(a)
print(type(a))


#create simple tuple with single integer
a=(4,)
print(a)
print(type(a))


#create simple list with single integer
a=[4]
print(a)
print(type(a))

#create empty tuple
a=()
print(a)
print(type(a))

#create tuple with multiple data type
x=(19,"joy",92.6)
print(x)
print(type(x))
print("age ",x[0])
print("name ",x[1])
print("pass percentage ",x[2])

#here x defines index no or subscript no
#list always starts with paranthesis
#tuple starts with square brackets

#create tuple with tuple element inside tuple
x=(1,2,3,(10,20))
print(x)
print(x[0])
print(x[1])
print(x[2])
print(x[3])
print(x[3][0])
print(x[3][1])

#create tuple with list element inside tuple
x=(1,2,3,[10,20])
print(x)
print(x[0])
print(x[1])
print(x[2])
print(x[3])
print(x[3][0])
print(x[3][1])

#list is mutable tuple is immutable it cannot be changed 
a=(10,20,30,40)
print(a)
print(type(a))
print(a[1])
#a[1]=100
#print("after change new list ",a)
#a.append(94)
#print("after addition new list ",a)
del a[3]
print("after deletion a[3] new list ",a)















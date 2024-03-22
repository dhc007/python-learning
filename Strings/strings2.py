#string slicing and operations on string
names="Dhruv,Shawn"
print(names[0:5])
print(len(names))

name="Dhruv"
len1=len(name)
print("Dhruv has", len1,"characters in his name")

print(name[:4]) #including 0 but not 4 D h r u
print(name[1:4])#including 1 but not 4 h r u
print(name[3:])#from 3 u v
print(name[0:-3])# from 0 to 5-3=2 not including 2 D h
print(name[:len(name)-2])#from 0 to 5-2=3 not including 3 D h r
print(name[-1:2]) # not possible as it is starting at 4 and ending at 2
print(name[-3:-1])# from 2 to 4 not including 4



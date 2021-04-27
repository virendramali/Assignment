#tuples(ordered,unchageable,(.....))
t1=("virendra","rushi","sandip","aditya")
print(type(t1))
print(t1[1])
print(t1[-2])
print(t1[1:3])
print(t1[-4:-1])
print(t1[::-1])
l1=list(t1)
print(l1)
l1.append(1.2)
print(l1)
l1.insert(4,1.2)
l1.extend('abc')
print(l1)
t1=tuple(l1)
print(t1)
for x in t1:
	print(x)
if "vicky" in t1:
	print("present")
else:
	print("not present")

print(len(t1))
print(t1[-1:])

t2=(1,)
print(type(t2))
del t2


l2=[1,2]
l3=[[66,77]]
l2.extend(l3)
print(l2)

print(t1[0:8:3])
print(t1.index('a'))
print(t1.count(1.2))
print(t1)

#python_collections(arrays)
#list(ordered,changeable,allows duplicate members,[......])
l1=[1,2,3,"abc","pqr",1.9]
print(l1)
print(type(l1))
print(l1[2])
print(l1[-0])
print(l1[1:3])
print(l1[2:-1])
print(l1[2:])
print(l1[-4:-2])
print(l1[::-1])
print(len(l1))
l2=[5,6,7]
l1.extend(l2)
print(l1)
l1.append(l2)
print(l1)
l1.append("xyz")
print(l1)
l2.insert(3,8)
print(l2)
l1.remove("pqr")
print(l1)
l1.insert(3,3)
print(l1)
l1.pop()
print(l1)
l1.pop(9)
print(l1)
del l1[3]
print(l1)
l2.clear()
print(l2)

l3=['a','b','c','d']
l4=l3.copy()
print(l4)
l4=list(l3)
print(l4)

l5=['e','f','g','h']
l6=[5,4,7,6,2]
l6.sort()
print(l6)
s1=(9,8,7,6)
print(type(s1))
l5.append(s1)
print(l5)
l7=l5+l6
print(l7)
l5.append(l6)
print(l5)
for x in l6:
	l5.append(x)
print(l5)
l5.extend(l6)
print(l5)

l5[5][2]=5
print(l5)
l5.reverse()
print(l5)

l7=list(s1)
print(l7)
l7.append(5)
print(l7)
l7.insert(2,('a','b','c'))
print(l7)
s1=tuple(l7)
print(s1)
print(type(s1))


l9=[11,12,13,1,15,16]
l9.reverse()
print(l9)
#set(unordered,unindexed,{.....})
s1={1,2,3,4,5,'a','b'}
print(type(s1))
print(len(s1))
l1=list(s1)
print(l1)
l1.append('c')
print(l1)
s1=set(l1)
print(s1)
for x in s1:
	print(x)
if 6 in s1:
	print("yes present")
else:
	print("not present")

s1.add('d')
print(s1)
s1.add(6)
print(s1)
s1.update('a','e')
print(s1)

s1.remove('e')
print(s1)
s1.discard(6)
print(s1)
s1.discard('f')
print(s1)
s1.pop()
print(s1)
s1.pop()
print(s1)
a=s1.pop()
print(a)
print(s1)
b=s1.pop()
print(b)
print(s1)



s2={11,12,13,14,15,15}
s3={'abc','pqr','xyz'}
s4=s2.union(s3)
print(s4)

s5={2.4,3.6,'vicky'}
s4.update(s5)
print(s4)
s6=s5.copy()
print(s6)

s6=set((4,5,7,'e','e','a'))
print(s6)

l1=list((1,2,3,4,4,'s','w'))
print(l1)

t1=tuple((4,5,7,8,'dfg','rty'))
print(t1)
print(type(t1))



s7={1,2,3,4,5,'a','f'}
s8={3,4,5}
s9=s7.union(s8)
print(s9)
s10=s7.symmetric_difference(s8)
print(s10)
s11=s7.intersection(s8)
print(s11)
s12=s7.symmetric_difference_update(s8)
print(s12)
s13=s7.difference(s8)
print(s13)
#dictionary(unordered,changeable,indexed,keys and values,{......})
d1={"name":"virendra","age":24,"place":"savlaj"}
d3=dict(d1)
print(d3)
#print(d1)
print(type(d1))
print(d1["name"])
print(d1.get("age"))
d1["name"]="vicky"
print(d1)

for x in d1:
	print(x)

for x in d1:
	print(d1[x])

for x in d1.values():
	print(x)

for x,y in d1.items():
	print(x,y)

if 24 in d1:
	print("present")
else:
	print("not present")

print(len(d1))

d1["number"]=7756087396
print(d1)

d1.pop("number")
print(d1)

d1.popitem()
print(d1)

del d1["age"]
print(d1)

d2={"name":"abc","subject":"xyz"}
'''del d2
print(d2)'''

d4=dict(d2)
print(d4)
d2=d4
d4["marks"]=45
print(d4)
print(d2)

d5=d4.copy()
print(d5)

d6={
	"d1":d1,
	"d2":d2,
	"d5":d5
	}
print(d6)
d6["d2"]["abc"]=123
print(d6)
print(d6['d5']["subject"])
d6.pop('d5')
print(d6)
print(d2.clear())
print(d2)




s1={"name":"virendra","subject":"maths","marks":80}
s2={"name":"rushi","subject":"maths","marks":100}
s3={"name":"sandip","subject":"maths","marks":90}
s4={"name":"aditya","subject":"maths","marks":98}
s5={"name":"sagar","subject":"maths","marks":85}
s6={"student_1":s1,
	"student_2":s2,
	"student_3":s3,
	"student_4":s4,
	"student_5":s5}
print(s6)
print(type(s6))

for x,y in s6.items():
	print(x,y)
	


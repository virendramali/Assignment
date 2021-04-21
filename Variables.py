a="Hello World!!"
print(a)
print(type(a))

x=[1,2,3,4,5,6]
print(len(x))
print(x.pop())

a_b="vicky"
print(a_b)

#string
message="Hello Python"
print(message)

name="Virendra Mali"
print(name)
print(type(a))

x="I told my friend, 'Python' is my favourite language"
print(x)




print("Sublime text")
print("\tSublime text")						#add_tab_to_text
print("Languages:\nPython\nJavascript\nC")	#add_newline_to_string

print("Languages:\n\tPython\n\tJavascript\n\tC")	#combine_tab_and_newline


#Assignment
print("\tAlbert Einstein once said, \"A person who never made a mistake never tried anything new.\"")

#string_slicing
a="Hello World"
print(a[1:5])
print(a[:7])
print(a[1:-2])
print(a[:-4])
print(a[::-1])		#reverse_string
print(len(a))		#length_of_string
print(a[-1])


#string_methods
x=" virendra, mali "
print(x.strip())						#removes_whitespace
print(x.title())						#titlecase
print(x.lower())						#lowercase
print(x.upper())						#uppercase
print(x.replace("virendra","Vicky"))	#replace_string
print(x.split(","))						#splits_string_into_substring


#string_check(in/not_in)
txt="I am Virendra Vinayak Mali."
print("am" in txt)
print("Mali" not in txt)


#string_concatenation(combine)
first_name='virendra'
last_name='mali'
full_name=first_name +" "+ last_name
print(full_name)							
print("Hello,"+" "+full_name.title()+'.')
message="Hello,"+" "+full_name.title()+"."
print(message)


#string_format
age=24
txt="I am Vicky and I am {} years old." 
print(txt.format(age))

name='Vicky'
age=24
place='Savlaj'
txt="I am {}. I am {} years old and I live in {}."
print(txt.format(name, age, place))


#escape_character(\"......\")
message="We cannot use \"double quote\" inside string that is surrounded by double quote."
print(message)

print("Hello \rworld")
print("\tVirendra\n\tMali")
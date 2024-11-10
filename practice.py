num_integer = 20
print(num_integer)
num_float = 4.23
print(num_float)

num_complex = 5j
print(num_complex)

string_hello = "Hello welcome"
print(string_hello)
another_string = 'Hey there'
print(another_string)
triple_string = '''Hello Everyone! I'm learning python'''
print(triple_string)

list = [1, 2, 3, 5]
tuples = (1, 3, 6)
dictionary = {"Name": "Cobbina", "Age": 24}
print(list)
print(tuples)
print(dictionary)
list.append(10)
print(list)
list.insert(2, 20)
print(list)

print(tuples[1])
print(dictionary['Name'])

print(type(num_integer))
print(type(num_float))
print(type(num_complex))

print(type(list))
print(type(tuples))
print(type(dictionary))


list2 = [1, 2, [3,5,6], 3, 7, [9]]
print(list2[2][2])

age = 75
if(age > 40  and age <60):
    print("You are an adult")
elif(age <= 60):
    print("You are getting older")
else:
    print("You are a senior citizen")

for i in range(10):
    print(i)


counter = 0
while(counter < 10):
    print(counter)
    counter = counter+1

print("I successfuly pushed my codes to github")
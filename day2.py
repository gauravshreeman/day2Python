#string slicing in python
# indexing[] and slice()
# [start : stop : step] for indexing
# (start,stop,step) for slicing
# Thy can also have negative index

name = "GauravKumarTiwari"
first_name = name[0:6]
last_name = name[11:]
cool_name = name [0:17:4]

print(cool_name)
print(first_name)
print (last_name)
reversed_name = name[::-1]
print(reversed_name)

website = "http://google.com"
website2 = "http://wikipedia.com"
slice = slice(7,-4)
print (website[slice])
print(website2[slice])

#if, elif and else statement in python
age = int(input("What is your age?"))
print(age)
if age == 100:
    print("You are a century old")
elif age >= 18:
    print("You are elligible to vote.")
elif age < 0:
    print("You haven't been born yet.")
else:
    print("You are not an adult. You cannot vote.")

#logical operators in python. (and, or, not). The not function reverse the output. True becomes false and false becomes true.
temp = int(input("What is the temperature outside?"))
if not(temp <= 0 and temp >=35):
    print("You can go outside!")
elif not(temp > 0 or temp < 35):
    print("The weather is bad today!")

while loop. It is a statement that will execute the block of code as long as the condition remains true.
while 1==1:
    print("I am stuck in a loop. Help!")

name = ""
while len(name) == 0:
    name = input("What is your name?")

print("Hello " + name)

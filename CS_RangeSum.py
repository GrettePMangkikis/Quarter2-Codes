age = int(input("Hi there! Please enter your age: "))

sum = 0

for number in range(1, age + 1):
    sum += number 

print("The sum of all numbers from 1 to", age, "is:", sum)

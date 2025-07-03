# Operators

# Assignment Operator
# = - assign the value from right to left
name = "Arpit"

# == -> Compare operator ( bool)

v1 = (1 == True)
v2 = (0 == False)
print(v1)
print(v2)

age = +65 # Unary Operator + ( Pycharm +_ -> Remove, Self exp.
num = -1
print(age)
print(num)
r = age+num # BODMAS - Math
print(r)

# Not Operator (Boolean)
is_married = True
print(not is_married)

# Is Operator - Identity Operator - Return bool
# List
a = 5
b = 6
c= False

print(a is b)

my_list = [1, 2, 3]
my_list2 = [1, 2, 3]
print(my_list is my_list2)

# is - How? - Conditions

# Arithmetic Operators
# +,-,*,/, %
a = 180
b = 90
print(a + b)
print(a - b)
print(a * b)
print(a / b)  # Float - Why Python is smart - div

print(a % b)
print(10 ** 2)
r = pow(10, 2)
print(r)

# Modulus - Operator -> Reminder
# 90 | 180 | 2
#    | 180 |
#    |   0 |
#
print(87 % 10)
print(87 // 10) # Q

print(10 / 10)

# Logical Operator - bool
x = 10
y = 20
print(x > y)
print(x < y)

a = 10
b = 10
print(a >= b)  # 10 > 10 or 10 = 10
print(a == b)  # 10 > 10 or 10 = 10
print(not a)
# Or Gate

f = False
t = True
print(f and t)
print(f or t) # Truth Table of or

x = 10
y = 20

result = (x != y) # 10 not equal 20 -> True
print(result)

# Ternary Operator
pramod_marks = 90
amit_marks = 97

#   x > y -> do something - print("pramod")
# y > x -> do something else -> print("amit)
print("Arpit is winner" if Arpit_marks > amit_marks else "ankit is winner")


if pramod_marks > amit_marks:
    print("Arpit is the winner")
else:
    print("Ankit is the winner")
#ifelse.py
# score = int(input("점수를 입력:"))

# if 90 <= score <= 100:
#     grade = "A"
# elif 80 <=score < 90:
#     grade = "B"
# elif 70 <=score < 80:
#     grade = "C"
# else:
#     grade = "D"

# print("등급은", grade)

value = 5
while value > 0:
    print(value)
    value -= 1

print("---break---")
lst = [1,2,3,4,5,6,7,8,9,10]
for i in lst:
    if i > 5:
        break  n 
    print("Item:{0}".format(i))

print("---continue---")
lst = [1,2,3,4,5,6,7,8,9,10]
for i in lst:
    if i > 5:
        break
    print("Item:{0}".format(i))

print("---range()---")
print(list(range(10)))
print(list(range(2000,2024)))
print(list(range(1,32)))

lst = list(range(1,11))
print([i**2 for i in lst if i >5])
tp = ("apple", "orange", "kiwi")
print([v.upper()for v in tp])

print("---필터링---")

def getBiggerThan20(i):
    return i > 20

iter = filter(getBiggerThan20, lst)
for item in iterL:
    print(item)
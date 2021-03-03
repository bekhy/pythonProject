# 1

if input("Введите что-то: "):
    print("OK")

# 2
number = int(input("Введите число: "))
if number > 0:
    print("1")
elif number <= 0:
    print("-1")

# 3
a = [2, 4, 6, 8, 12, 4245, 546, 40, 3234, 67, 45, 23]
check = int(input("Введите число: "))
if check in a:
    print("Это число есть в массиве!")
else:
    print("Этого числа нет в массиве!")

# 4
dict = {"12":"A", "13":"B", "14":"C", "15":"D", "22":"E", "30":"F"}
sear = input("Введите ключ по которому найти: ")
if sear in dict:
    print("Это ключ есть в словаре!")
else:
    print("Этого ключа нет в словаре!")

# 1(1)
paired = []
unpaired = []
other = []
list_a = [1, 3, 4, 5, 6, 8, 9, 12, 14, 15, 18, 22, 25, 28, 30]
for i in list_a:
    if i % 2 == 0:
        paired.append(i)
    if i % 3 == 0:
        unpaired.append(i)
    elif i % 2 != 0 and i % 3 != 0:
        other.append(i)
print(paired)
print(unpaired)
print(other)


# 2(2)
str_a = input("Введите строку: ")
sym_b = input("Введите символ: ")
if sym_b in str_a:
    print("Этот символ есть в строке!")
else:
    print("Этого символа нет в строке!")

# 3(3)
b = 1
list_c = [1, 23, 3, 54, 8, 17, 34, 21, 9, 13, 19, 20, 30]
for i in list_c:
    b *= i
print("Результат перемножения чисел: " + str(b))

4(4)
int_a = 1
str_a = ""
dict_a = {}
list_z = []
list_az = [1, 4, "3", "8", {"121":121}, {"12":12}, [1, 3, 6, 9, 12], [2, 8, 16, 32, 48]]
for i in list_az:
    if i in list_az == int:
        int_a.append(i)
    # if i in list_az == "":
    #     str_a == ""
    # if i in list_az == {}:
    #     dict_a == {}
    # if i in list_az == []:
    #     list_z.append(i)
print(i)
number = int(input("Type a number: "))

number_dict = {}
for i in range(1, number+1):
    number_dict[i] = i*i

print(number_dict)

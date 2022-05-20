vdfvgsdfgdfg = "Какой то текс"
int_text = 10 
float_data = 14.4

numbers = "one,two,three,four"

number = "two"

numbers_list = numbers.split(",")

for x in numbers_list:
    if x == number:
        print("мы нашли совпадение")
    else:
        print(f"нужного {number} нет")
vdfvgsdfgdfg = "Какой то текс"
int_text = 10 
float_data = 14.4

numbers = "one,two,three,four,two"

liked_numbers = ["one", "two"]

numbers_list = numbers.split(",")

count = 0
for number in numbers_list:

    # Проверяем, находится ли значение nuber в списке liked_numbers
    if number in liked_numbers:
        # count = count + 1
        count += 1
        # print("мы нашли совпадение")
    else:
        # print(f"нужного {number} нет")
        pass

# print(count)

# # ((0, 1, 2), (3, 4, 5))
# hard_list = ( (0,1,2) , (3,4,5) )
# simple_list = ("one","two","three",4,5,6)

# # print(simple_list[1])
# print(hard_list[1][1])

# print("asds"[2])
# for i in "asdf":
#     print(i)

simple_dict = {
    "key_one" : {
        "inner_key_one" : "inner_value_one"
    },
    "key_two" : ["inner_value_1", "inner_value_2" ],
    "key_three" : "text_value",
}

# print(simple_dict["key_one"]["inner_key_one"])
# print(simple_dict["key_two"][1])
# print(simple_dict["key_three"].upper())

for i in simple_dict:
    print(i, simple_dict[i])

numbers_dict = {
    "from_one_to_three" : {
        "one" : 1,
        "two" : 2,
        "three" : 3,
    },
    "from_four_to_five" : {
        "four" : 4,
        "five" : 5,
    },
}

for i in numbers_dict:
    # 1st it = from_one_to_three from_four_to_five
    for x in numbers_dict[i]:
        # one two three four five
        # 1 ["from_one_to_three"]["one"]
        # 2 ["from_one_to_three"]["two"] 
        # 3 ["from_one_to_three"]["three"] 
        # 4 ["from_four_to_five"]["four"]
        # 5 ["from_four_to_five"]["five"]
        # print(numbers_dict[i][x])
        pass

# for key, value in simple_dict.items():
#     print(key)
#     print(value)
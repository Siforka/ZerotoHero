import requests
import simplel_lib

url = "https://api.coindesk.com/v1/bpi/currentprice.json"

# # 1 Поулчить данные по значению url 
# # 2 Трансформировать данные в структуру данных python
# # 3 Получить значение rate для валюты my_current
# # 4 Мы хотим узнать, сколько стоит в выборанной валюте 10 биткоинов (btc_count)

# # Мы вызываем метод get из библиотеки requests
res = requests.get(url)

# # print(type(res))
# #  text     - поле объекта Response тело http овтета
# #  json()   - метод объекта Response парсинг строки json в структуру данных python
# print(res.json())

api_data = res.json()

# str_float_data = "1,138.34"
# # replace("то что мы хотим заменить", "то на что мы хотим это заменить")
# print(10 * float(str_float_data.replace(",","")))

my_current = ("EUR", "USD")
btc_count = 10
for i in api_data["bpi"]:

    if i in my_current:
        print(f"мы нашли нужную валюту {i}")
        rate_str = api_data["bpi"][i]["rate"]
        rate_float = float(rate_str.replace(",", ""))
        print(rate_float*btc_count)

# {
#     "USD" : { 
#         'code': 'USD', 
#         'symbol': '&#36;', 
#         'rate': '30,019.3901', 
#         'description': 'United States Dollar', 
#         'rate_float': 30019.3901
#     }
# }
# my_simple_obj = simplel_lib.SimpleLib()

# my_simple_obj.print_text()

# my_simple_obj.print_outer_text("123123")

# print(my_simple_obj.text_data)



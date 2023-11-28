import json
from functools import reduce
from functools import partial
file = 'countries.json'
file_2 = 'countries-data.json'

#Чтение файла
def read(data_file: json) -> dict:
    with open(data_file, 'r', encoding = 'utf-8') as file:
        try:
            data = json.load(file)
        except:
            data = {

            }
        return(data)
    
# Запись файла json
def write(data_file: json, dat: dict) -> json:
    with open(data_file, 'w', encoding='utf-8') as file:
        json.dump(dat, file) 

# Функция преобразования записи прописными буквами
def up_let(slovo: str) -> str:
    slovo = slovo.upper()
    return slovo

# Функция фильтрации по содержанию "land"
def fil_land(slovo: str) -> str:
    if 'land' in slovo:
        return True
    else:
        return False

# Функция фильтрации по содержанию только 6 букв
def fil_six(slovo: str) -> str:
    if len(slovo) == 6:
        return True
    else:
        return False

# Функция фильтрации по содержанию 6 букв и более
def fil_mothesix(slovo: str) -> str:
    if len(slovo) <= 6:
        return True
    else:
        return False

#Функция фильтрации по названиям начинающихся с "Е"
def fil_E(slovo: str) -> str:
    if slovo[0] == "E":
        return True
    else:
        return False

data = read(file)

#7 Объеденить и получить один элемент с помощью reduse()
new_data = reduce(lambda x, y: x+y, data)
#print(new_data)

#8 Объеденить 2 функции высшего порядка
new_data = map(up_let, reduce(lambda x, y: x+y, data))
#print(list(new_data))
new_data = reduce(lambda x, y: x+y, map(up_let, data))
#print(new_data)
#Формирование нового списка с только прописными буквами
#new_data = map(up_let, data)
#print(list(new_data))

#Фильтрация по содержанию "land"
#new_data = filter(fil_land, data)
#print(list(new_data))

#Фильтрация по содержанию только 6 букв
#new_data = filter(fil_six, data)
#print(list(new_data))

#Фильтрация по содержанию 6 и более букв
#new_data = filter(fil_mothesix, data)
#print(list(new_data))

#Фильтрация по названиям начинающихся с "Е"
#new_data = filter(fil_E, data)
#print(list(new_data))


# 9 задание, замыкание
def categorize_countries(data):
    def like_in(like):
        datas = []
        for i in data:
            if (like in i):
                datas.append(i)
        return datas
    return like_in
# 9 задание, каррирование
def like_in2(like,data):
    datas = []
    for i in data:
        if (like in i):
            datas.append(i)
    return datas
list_data2 = lambda like: lambda data:like_in2(like,data)

#10. Функциональное программирование
#Загрузка данных файла
data = read(file_2)

#10.1 Функтор для выбора 
class sortFun:
    def __init__(self, fil_cat: str):
        self.fil_cat = fil_cat
    def __call__(self, data: json):
    
        data.sort(key = lambda x: x[self.fil_cat])
        return data


#10.1.1
sort_data = sortFun("name")
new_data = sort_data(data)
#print(new_data)
#10.1.2
sort_capit = sortFun("capital")
new_data = sort_capit(data)
#print(new_data)
#10.1.3
sort_popu = sortFun("population")
new_data = sort_popu(data)
#print(new_data)



#10.2, 10.3
class sortFunNum:
    def __init__(self, fil_num: str):
        self.fil_num = fil_num
    def __call__(self, data: json):
        language = {}
        a = data[0]['languages']
        for i in data:
            for j in i['languages']:
                if j not in language:
                    
                    language.update({j: [i['name']]})
                else:
                    language[j].append(i["name"])
        return sorted(language.items(), key = lambda item: len(item[1]), reverse=True)[0:self.fil_num]
    def sort_by_population(self, data: json):
        data.sort(key = lambda x: x["population"],reverse=True)
        return data[0:self.fil_num]
dict1 = {}
print(dir(dict1))
data = read(file_2)
sort_10 = sortFunNum(10)
new_data = sort_10.sort_by_population(data)
print(new_data)
import random

def get_keys_by_value(dict_of_elements, value):
  list_of_keys = []
  for key, item in dict_of_elements.items():
    if item == value:
      list_of_keys.append(key)
  return list_of_keys

def generate_random_string(length):
  symbols = "qwertyuiopasdfghjklzxcvbnm0123456789"
  random_str = ""
  for i in range(length):
    random_str += symbols[random.randrange(len(symbols))]

  return random_str

def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k


def zd1():
    list = [random.randint(1,100) for i in range(1,10)]
    print (list,"\n",list[::-1] )


def zd2():
    list1 = [random.randint(1,100) for i in range(1,10)]
    list2 = [random.randint(1,100) for i in range(1,10)]
    list3 =[]
    for i in range(0,len(list1)):
        if (i%2==0):
            list3.append(list1[i])
        else:
            list3.append(list2[i])
    print (list1,"\n",list2,"\n",list3 )

def zd3():
        # Генерируем список из 10 произвольных элементов
    list1 = [random.randint(-10, 10) for i in range(10)]
    list2 = ["1", "1","2","4"]

    # Объединяем два списка
    list3 = list1+list2

    # Выводим исходный список
    print(list3, "\n", set(list3))


def zd4():
    dict_of_elements = {
        generate_random_string(5): random.randint(0,10) for _ in range(random.randint(10, 30))
    }
    values = []
    for key in dict_of_elements:
        values.append(dict_of_elements[key])
        print(key, dict_of_elements[key])
    list22 = []
    for i in set(values):
       
       list = get_keys_by_value(dict_of_elements,i)
       kort = (i, list)
       list22.append(kort)
    print(list22)



def zd5():
    dict_of_elements1 = {
        generate_random_string(5): random.randint(0,20) for i in range(random.randint(10, 30))
    }
    dict_of_elements2 = {
        generate_random_string(5): random.randint(0,20) for i in range(random.randint(10, 30))
    }
    values1 = []
    for key in dict_of_elements1:
        values1.append(dict_of_elements1[key])
        print(key, dict_of_elements1[key])
    print("########################")
    values2 = []
    for key in dict_of_elements2:
            values2.append(dict_of_elements2[key])
            print(key, dict_of_elements2[key])
    
    intersect = list(set(values1) & set(values2))
    print("значения первого списка: ", values1, "\n","значения второго списка: ", values2 )
    print ("пересечение: ",intersect)
    ndict = {}
    for i in intersect:
        
        ndict[get_key(dict_of_elements1,i)] = i
    print("########################")
    for key in ndict:
        print(key, ndict[key])
    

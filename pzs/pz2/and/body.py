import typer
import json

app = typer.Typer()

f = 'basa.json'

#Чтение файла
def read(data_file: json) -> dict:
    with open(data_file, 'r', encoding = 'utf-8') as file:
        try:
            data = json.load(file)
        except:
            data = {
                'Category_base':{},
                'Spend_list':{}
            }
        return(data)

# Запись файла json
def write(data_file: json, dat: dict) -> json:
    with open(data_file, 'w', encoding='utf-8') as file:
        json.dump(dat, file, indent=9) 

# Вычисление остатка по лимиту
@app.command(short_help="how about that limit")
def wht_limit(category: str) -> int:
     data = read(f)
     limit = data['Category_base'][category]['Limit']
     spends = data['Category_base'][category]['Spending']
     ost = limit - spends
     return(ost)

# Добавление категории трат в бюджте
@app.command(short_help='add category of budget')
def add_cat(category: str, limit: int):
    category = category.lower()
    typer.echo(f'adding category {category} with {limit} limit')
    data = read(f)
    data['Category_base'][category] = {
        'Limit': limit,
        'Spending': 0
    }
    write(f,data)

# Добавление трат в базу
@app.command(short_help='add spend or income')
def add_spend():
    category = input(f'What category is:')
    comment = input(f'Spend comment:')
    while True:
        mark = input(f'Spend or income (s/i):')
        if mark == 's' or mark == 'i':
             break
    sum = int(input(f'How much:'))
    typer.echo(f'Adding {comment} with {sum}')
    data = read(f)
    data['Spend_list'][comment] = {
        'Category': category,
        'Mark': mark,
        'Cost': sum
    }
 
    if mark == 's':
        data['Category_base'][category]['Spending'] += data['Spend_list'][comment]['Cost']
    if mark == 'i':
        data['Category_base'][category]['Spending'] -= data['Spend_list'][comment]['Cost']
    print(f'Now your limit in', category, 'is:', wht_limit(category))
    write(f, data)



# Вывод всего списка категорий
@app.command(short_help = 'show category list')
def show():
    typer.echo(f'Category list')
    data = read(f)
    for key in data['Category_base']:
            print(key)

# Вывод всего списка трат
@app.command(short_help = 'show spend list')
def show_spend():
    typer.echo(f'Spend list')
    data = read(f)
    for key in data['Spending']:
            print(key)

if __name__ == "__main__":
    app()

#print('ajfhsajdfhaldf')
def read_cookbook():
    cook_book = {}
    
    with open('recipes.txt', 'r', encoding='utf-8') as f:
        for line in f:
            dish_name = line.strip()
            count = int(f.readline())
            ing_list = list()
            for item in range(count):
                ingrs = {}
                ingr = f.readline().strip()
                ingrs['ingredient_name'], ingrs['quantity'], ingrs['measure'] = ingr.split('|')
                ingrs['quantity'] = int(ingrs['quantity'])
                ing_list.append(ingrs)
            f.readline()
            cook_book[dish_name] = ing_list
    return cook_book

def get_shop_list_by_dishes(dishes, person_count):
    ingr_list = {}

    for dish_name in dishes:  # итерируем список полученных блюд
        if dish_name in cook_book:
            for ings in cook_book[dish_name]:  # итерируем ингридиенты в блюде
                mq_list = dict()
                if ings['ingredient_name'] not in ingr_list:
                    mq_list['measure'] = ings['measure']
                    mq_list['quantity'] = ings['quantity'] * person_count
                    ingr_list[ings['ingredient_name']] = mq_list
                else:
                    ingr_list[ings['ingredient_name']]['quantity'] = ingr_list[ings['ingredient_name']]['quantity'] + \
                                                                     ings['quantity'] * person_count
            
    return ingr_list

if __name__ == '__main__':
    cook_book = read_cookbook()
    print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))

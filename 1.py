#-*-coding: utf-8 -*-
def get_shop_list_by_dishes(dishes , person_count):
    with open ('input.txt') as file:
        cook_book = {}
        for item in file:
            ingredients_name = item.strip()
            ingredients_quantity = int(file.readline())
            unit = []
            for i in range(ingredients_quantity):
                food = file.readline().strip()
                ingredient_name, quantity, measure = food.split(' | ')
                unit.append({ 'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure })
            file.readline()
            cook_book[ingredients_name] = unit
            
        print(f'cook_book = {cook_book}')
        
    print()
    
    shop_list_by_dishes = {}
    for dish in dishes:
        if dish in cook_book.keys():
            for ingredient in cook_book[dish]:
                key = ingredient['ingredient_name']
                if key in shop_list_by_dishes.keys():
                    shop_list_by_dishes[key]['quantity'] += int(ingredient['quantity'] * person_count)
                else:
                    measures = ingredient['measure']
                    shop_list_by_dishes[key] = {'measure': measures, 'quantity': int(ingredient['quantity']) * person_count}
    return shop_list_by_dishes

print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
                           
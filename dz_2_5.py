import datetime
#
#
# start = datetime.datetime.now()
#
# with open('cookbook.txt', encoding='utf8') as file:
#     recipe_list = file.read()
# print(recipe_list)
# end = datetime.datetime.now()
# print(start, end, (end - start), sep='\n')



print('Программа деления одного целого числа на другое, с открытием файла и записи в него результата')
with open('test.txt', 'w', encoding='utf-8') as file:
    start = datetime.datetime.now()
    num1 = int(input('Введите первое положительное целое число: '))
    num2 = int(input('Введите второе положительное целое число: '))
    result = str(str(num1) + ' / ' + str(num2) + ' = ' + str(num1 / num2))
    print(result)
    file.write(result)
    end = datetime.datetime.now()
print(start, end, (end - start), sep='\n')


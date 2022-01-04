# 1. Вычислить средний возраст выживших женщин из кабин 1 класса (pclass = 1)
# 2. Вычислить, сколько выжило детей из пассажиров 3 класса (pclass = 3)
# 3. Вычислить разницу между средними расходами (fare) умерших пассажиров 1 и 2 классов.
# 4. Удалить столбцы типа object, в которых пропущены данные
# 5. Создать датасет, состоящий из двух столбцов - возраст и транспортные расходы (age и fare).  При этом в датасете должны остаться только те пассажиры, которые являются женщинами и которые выжили. После чего посчитать среднее по получившимся столбцам (за одну команду)
# 6. Сделать факторизацию столбца пол (sex) с помощью функции map
# 7. Сделать факторизацию столбца пол (who) с помощью функции replace
# 8. Сделать факторизацию остальных категориальных столбцов
# 9. Посчитать средний возраст и средние транспортные расходы (age и fare) каждой категории пассажиров (дети, взрослые и женщины)
# 10. Посчитать средний возраст и средние транспортные расходы (age и fare) каждой категории пассажиров, учитывая класс каюты (pclass) (дети, взрослые и женщины)


import pandas as pd
import numpy as np
#
data=pd.read_csv('titanic.csv')
#
pd.set_option('display.width', 1000)
pd.set_option('display.max_columns', data.shape[1])
#
#print(data.head())

# 1. Вычислить средний возраст выживших женщин из кабин 1 класса (pclass = 1)
dataset = data[(data['sex'] == 'female') & (data['pclass'] == 1) & (data['survived'] == 1)]
answer_1 = dataset['age'].mean()
print(dataset.head())
print('\n Средний возраст выживших пассажиров-женщин из 1-го класса:\t ' + str(answer_1) + '\n')

# 2. Вычислить, сколько выжило детей из пассажиров 3 класса (pclass = 3)
dataset = data[(data['who'] == 'child') & (data['pclass'] == 3)]
answer_2 = dataset['age'].mean()
print(dataset.head())
print('\n Количество выживших пассажиров-детей из 3-го класса:\t ' + str(answer_2) + '\n')


# 3. Вычислить разницу между средними расходами (fare) умерших пассажиров 1 и 2 классов.

dataset_1 = data[(data['survived'] == 0) & (data['pclass'] == 1)]
dataset_2 = data[(data['survived'] == 0) & (data['pclass'] == 2)]
answer_3 = dataset_1['fare'].mean() - dataset_2['fare'].mean()
print('\n Разность между средними расходами погибших пассажиров из 1-го и 2-го классов:\t ' + str(answer_3) + '\n')


# 4. Удалить столбцы типа object, в которых пропущены данные

columns = data.describe(include = ['object'])
dataset=data
for line in columns:
    print(line)
    print('\t' + str(sum(data[line].value_counts())))
    if sum(data[line].value_counts()) != data.shape[0]:
       # print(line + ' - delete ' + str(sum(data[line].value_counts())))
        dataset=dataset.drop([line], axis=1)
print(dataset.info())
print()
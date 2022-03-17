def telephon_info(telephon_number, codes):
    line = telephon_number.split()
    flag = False
    city_number = ''
    city_name = ''
    if (line[0] == '+7'):
        flag = True
    city_number = line[1][1] + line[1][2] + line[1][3]
    for key in codes:
        if codes[key].count(city_number) == 1:
            city_name = key
    # надеюсь, что телефон без кода означает тефелон без +7 и без кода города)
    number_without_code = line[2] + line[3] + line[4]
    return tuple([flag, city_name, number_without_code])

codes = {
    'Абакан': ['39022'],
    'Архангельск': ['8182', '818'],
    'Астрахань': ['8512'],
    'Барнаул': ['3852'],
    'Белгород': ['4722'],
    'Благовещенск': ['4162'],
    'Брянск': ['4832'],
    'Владивосток': ['4232'],
    'Владикавказ': ['8672'],
    'Владимир': ['492'],
    'Волгоград': ['8442'],
    'Вологда': ['8172'],
    'Воркута': ['82151'],
    'Воронеж': ['4732'],
    'Грозный': ['8712'],
    'Санкт-Петербург': ['812'],
    'Москва': ['495', '499']
    }

# проверим работу программы:
print("Введите номер телефона: ")
number = input()
print(telephon_info(number, codes))
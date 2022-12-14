import re
# . - любой символ кароме \n
#\d - любая цифра
#\D - любая не цифра
#\s - любой пробельный символ
#\S - любой не пробельный символ
#\w - любой символ слова
#\W - любой символ не слова


# with open('text.txt', 'r') as file:
    # test_info = []
    # for line in file:
    #     test_info.append(line.strip())

# Регулярные выражения #1: литералы и символьный класс+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

test_info = 'еда, (еда), победа, беда'
# r'\(еда\)' - найдёт вхождение (еда)
# r'еда' - найдёт четыре вхождения ['еда', 'еда', 'еда', 'еда']
result = re.findall(r'\bеда\b', test_info)

# r'[Ее]д[ау]' - задаёт набор символов 'Е' или 'е', а в конце слова 'а' или 'у'
# r'[а-иА-И]д[а-уА-У]' - задаёт диапозон символов в алфавитном порядке
# r'[^а-яА-Я]' - будем искать не буквы русс.алфовита
test_info = 'еда, еду, Еда, Еду'
result = re.findall(r'[Ее]д[ау]', test_info)


# Регулярные выражения #2: квантификаторы {m,n}, +, * , ?+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# r'o{2,5}' - означает что данная комбинация может повторяться от 2 до 5 раз (МАЖОРНЫЙ)
# r'o{2,5}?' - означает что данная комбинация может повторяться от 2 до 5 раз (МИНОРНЫЙ)
# Краткая запись {m}, {m,}, {,m}?
# ? - от 0 до 1, * - от 0 до бесконечности, + - от 1 до бесконечности
test_info = 'Google, Gooogle, Goooooogle'
result = re.findall(r'o{2,5}', test_info)

test_info = '375292257168'
result = re.findall(r'37529\d{7}', test_info)


test_info = 'стеклянный, стекляный'
result = re.findall(r'стеклянн?ый', test_info) # ? - от 0 до 1, либо 0 'н', либо 1 'н' и того в слове либо 1 либо 2 "н"


test_info = "author=Пушкин А.С.; title = Евгений Онегин; price =200; year= 2001"
# result = re.findall(r'\w+\s*=\s*[^;]+', test_info)
result = re.findall(r'(\w+)\s*=\s*([^;]+)', test_info)


test_info = "Картинка <img alt='bg.jpg' src='bg.jpg'> в тексте</p>"
result = re.findall(r'<img\s+\w+\s*=\s*[^>]+', test_info)



# Регулярные выражения #3: сохраняющие скобки и группировка++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# | - or
# (?:key) - Не сохраняемая скобка, (key) - сохраняемая скобка, сохраняет ключи(второй уровень сохранения)
test_info = "lat = 5, lon=7, len = 43"
result = re.findall(r'(?:lat|lon)\s*=\s*\d+', test_info) # ->['lat = 5', 'lon=7'] сохраняем ключ и значение
result = re.findall(r'((lat|lon)\s*=\s*\d+)', test_info) # ->[('lat = 5', 'lat'), ('lon=7', 'lon')] сохраняем ключ и значение и ключ
result = re.findall(r'(lat|lon)\s*=\s*(\d+)', test_info) # ->[('lat', '5'), ('lon', '7')] отдельно сохраняем ключ и значение


test_info = "Картинка <img src='bg.jpg'> в тексте</p>"
result = re.findall(r"<img\s+[^>]*src=(?P<p>[\"'])(.+?)(?P=p)", test_info) # (?P<name>...)....(?P=name) создание и вызов именовоной сохран.скобки



with open('text.xml', 'r') as file:
    lat = []
    lon = []  
    for line in file:      #  <point lon="40.8482" lat="52.6274" />
        result = re.search(r'<point\s+[^>]*?lon=([\"\'])(?P<lon>[0-9.,]+)\1\s+[^>]*lat=([\"\'])(?P<lat>[0-9.,]+)\1' ,line)
        if result:
            dic = result.groupdict()
            lon.append(dic['lon'])
            lat.append(dic['lat'])
# print(lat, lon, sep='\n')



# Регулярные выражения #4: флаги и проверки++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


test_info = """<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=windows-1251">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Уроки по Python</title>
</head>
<body>
<script type="text/javascript">
let o = document.getElementById('id_div');
console.log(obj);
</script>
</body>
</html>"""
result = re.findall(r"([-\w]+)[ \t]*=[ \t]*[\"'](.+?)(?<![ \t])[\"']", test_info, re.MULTILINE)



    

print(result)
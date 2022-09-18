s = input() + ' запретил букву'
a = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
col_1 = 0
while col_1 != 32:
    if a[col_1] in s:
        print(s, a[col_1])
        s.replace(a[col_1],'')

        col_1 += 1
    else:
        col_1 += 1
        continue
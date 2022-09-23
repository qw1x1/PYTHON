import timeit
class Point:
    min_coord = 1
    max_coord = 1000
    
    def __new__(cls, *args, **kwargs):
        print(super(cls))
        return super().__new__(cls)

    
    def __validate(self, value):
        return self.max_coord >= value >= self.min_coord

    def __init__(self, x = 0, y = 0, z = 0, p = 0):
        self.__x = self.__y = 0
        self.z = z #public
        self.p = p #public
        if self.__validate(x) and self.__validate(y):
            self.__x = x #privat
            self.__y = y #privat

    # Метод ктоторый не взаимодействует с 'cls' и 'self', метод вспомогательный .....
    @staticmethod
    def lev(*args):
        return list(map(lambda x: int(x) if str(x).isdigit() else 0, args))

    # Метод доступа для изменения атрибутов объекта
    def set_coard(self, *args):
        x, y = args
        if self.__validate(x) and self.__validate(y):
            self.__x = x
            self.__y = y

    @classmethod    
    def set_baund(cls, left_baund):
        cls.min_coord = left_baund
        #cls.max_coord = right_baunn  = cls.min_coord , right_baunn = cls.max_coord

    def get_coard(self):
        return self.__x, self.__y, self.z, self.p 

    # __getattribute__ - позволяет управлять обращением к атрибутам
    def __getattribute__(self, name):  
        if name == 'p':
            print('PRIVAT attribute')
        else:
            return object.__getattribute__(self, name)   

    # __setattr__ - позволяет управлять созданием атрибутов
    def __setattr__(self, name, value):
        if name == 'gg' and value == 3:
            raise AttributeError('GOVNO NE DELAJ')
        else:
            object.__setattr__(self, name, value)

#pt1 = Point(1, 2, 3, 4)
#print(pt1.get_coard())
#pt1.set_coard(4,3)
#print(pt1.get_coard())
#c = pt1.z
#cc = pt1.p
#print(c)
#pt1.gg = 3
#print(cc)


"""++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"""



"""
Имена методов для сет и гет должны быть одинаковы
первым пищем гет и оборачиваем в @property
затем писем геt с таимже именем как и у гет
и оборачиваем в @name.setter
где name = имя геттера, а .setter = мия декоратора в @property
"""
#per1 = Person("Dimka", 22)
 





class Person:
    def __init__(self, fio, old, ps, weight):
        # не прописываем varify т.к он есть в setter
        self.fio = fio
        self.old = old
        self.passport = ps
        self.weight = weight

    @classmethod
    def varify_fio(cls, fio):
        if type(fio) != str:
            raise TypeError('ФИО - это строка!')
        if len(fio.split()) != 3:
            raise TypeError('Не верный формат записи')
        if False in [word.isalpha() for word in fio.split()]:
            raise TypeError('В ФИО дожны быть только буквенные символы')

    @classmethod
    def varify_old(cls, old):
        if type(old) != int or old < 14 or old > 120:
            raise TypeError('Ворост - это целое число в диапозоне [14: 120]')

    @classmethod
    def varify_weight(cls, weight):
        if type(weight) != float or weight < 20:
            raise TypeError('Ворост - это вещественное число в диапозоне не меньше 20')

    @classmethod
    def varify_ps(cls, ps):
        if type(ps) != str:
            raise TypeError('Пасспорт должен быть строкой!')
        if len(ps.split()) != 2 or len(ps.split()[0]) != 4 or len(ps.split()[1]) != 6:
            raise TabError('Неверный формат пасспортных данных')
        if False in [word.isdigit() for word in ps.split()]:
            raise TypeError('Серия и нопер паспорта должны быть числами')

    @property
    def fio(self):
        return ' '.join(self.__fio)

    @fio.setter
    def fio(self, fio):
        self.varify_fio(fio)
        self.__fio = fio.split()

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.varify_old(old)
        self.__old = old

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.varify_weight(weight)
        self.__weight = weight  

    @property
    def passport(self):
        return self.__passport

    @passport.setter
    def passport(self, ps):
        self.varify_ps(ps)
        self.__passport = ps
    


#p = Person('Бычковский Владислав Александрович', 22, '1234 564489', 75.40)

#print(p.__dict__)

#p.old = 100
#p.weight = 88.567
#p.passport = '1234 000000'

#print(p.old)
#print(p.fio)
#print(p.weight)
#print(p.passport)



#ДИСКРИПТОРЫ - вместо сетерров и гетерров, если проверка для всех атрибутов одинаковая!
class Integer:
    '''
        instance - ссылка на обект класса для которого вызывается дискриптор
        owner - ссылка на сам класс для объекта которого вызывается дискриптор

        instance - экземпляр (экземпляр класса)
        owner - владелец ( класс, от которого был создан экземпляр)
    '''
    @classmethod
    def verify(cls, coord):
        if type(coord) != int:
            raise TypeError('Координата дожна быть INTEGER')

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.verify(value)
        setattr(instance, self.name, value)

    def __delete__(self, instance):
        delattr(instance, self.name)
    
class Point3D:
    x = Integer()
    y = Integer()
    z = Integer()

    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

#p = Point3D(1, 2, 3)
#print(p.x)
#p.x = 4
#print(p.x)
#del p.x
#print(p.__dict__)

#########################################################################################################################
#__DUNDER-METOD__
#########################################################################################################################
'''
Метод __call__ - позволяет вызвать объект класса как функцию
передавая все аргументы через ссылку на объект self.

При этом т.к обект класса будет работать как функция. 
то и использовать мы его можем как функцию
например создадим класс который будет работать как декоратор
'''
import math
class Derivate:
    def __init__(self, funk):
        self.__fn = funk
    
    def __call__(self, x, dx = 0.0001, *args, **kwargs):
        return (self.__fn(x + dx) - self.__fn(x)) / dx

# Экривалентно @Derivate = Derivate(df_sin)
@Derivate
def df_sin(x):
    return math.sin(x)

#print(df_sin(math.pi/4)) # просто функция 

#df_sin = Derivate(df_sin) # Декорированая функция через объект класса Derivate/ Функция это объект класса
#print(df_sin(math.pi/3))

class Test:
    def __init__(self, name):
        self.name = name
    
    #Метод переопределяющий вывод инфы, ТОЛЬКО ДЛЯ ОТЛАДКИ!!!
    def __repr__(self):
        return f'{self.__class__} : {self.name}'

    #Метод переопределяющий вывод инфы, ДЛЯ ПОЛЬЗОВАТЕЛЯ!!!
    def __str__(self):
        return f'{self.name}'

#print(Test('NAME'))

class Point1:
    def __init__(self, *args):
        self.__coords = args

    #к объекту класса мы не можем присенить функцию len(), для этого определяем метод __len__
    def __len__(self):
        return len(self.__coords)

    #к объекту класса мы не можем присенить функцию abs(), для этого определяем метод __len__
    def __abs__(self):
        return list(map(abs, self.__coords))

#p = Point1(1, -2, -5)
#print(len(p))5
#print(abs(p))

#14 Магические методы __add__, __sub__, __mul__, __truediv__ +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class Clock:
    __DAY = 86400

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError('Секунды должны быть int')
        self.seconds = seconds % self.__DAY

    @classmethod
    def varify(cls, x):
        if not isinstance(x, (int, Clock)):
            raise TypeError('Секунды должны быть int or Clock')
        sc = x
        if isinstance(sc, Clock):
            sc = x.seconds
        return sc
    
    def get_time(self):
        s = self.seconds % 60
        m = (self.seconds // 60) % 60
        h = (self.seconds // 3600) % 24
        return f"{self.__get_formatted(h)}:{self.__get_formatted(m)}:{self.__get_formatted(s)}"

    @classmethod
    def __get_formatted(cls, x):
        return str(x).rjust(2, '0')
    #======================================ADD==================================================#
    def __add__(self, other):
        return self.__class__((self.seconds + self.varify(other)))

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        self.seconds += self.varify(other)
        return self
    #=======================================SUB==================================================#
    def __sub__(self, other):
        return self.__class__((self.seconds - self.varify(other)))

    def __rsub__(self, other):
        return self - other

    def __isub__(self, other):
        self.seconds -= self.varify(other)
        return self

    def __eq__(self, other):
        return self.seconds == other.seconds

    def __hash__(self):
        return hash(self.seconds)


# c1 = Clock(2000)
# c2 = Clock(2000)
#c1 = c1 + 110
#c1 -= 110
# print(hash(c1), hash(c2), sep='\n')

#print(c1.get_time())
#print(c1.get_time())
#print(c4.get_time())

#15. Методы сравнений __eq__, __ne__, __lt__, __gt__ +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class Clock2:
    __DAY = 86400

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError('Секунды должны быть int')
        self.seconds = seconds % self.__DAY

    @classmethod
    def varify(cls, x):
        if not isinstance(x, (int, Clock2)):
            raise TypeError('Секунды должны быть int or Clock2')
        sc = x
        if isinstance(sc, Clock):
            sc = x.seconds
        return sc
    
    def get_time(self):
        s = self.seconds % 60
        m = (self.seconds // 60) % 60
        h = (self.seconds // 3600) % 24
        return f"{self.__get_formatted(h)}:{self.__get_formatted(m)}:{self.__get_formatted(s)}"
    
    @classmethod
    def __get_formatted(cls, x):
        return str(x).rjust(2, '0')

    #======================================eq=ne=lt=gt===========================================#
    # == and !=
    def __eq__(self, other):
        if self.seconds == self.varify(other):
            return True
        return False
        # < and >
        def __lt__(self, other):
            if self.seconds > self.varify(other):
                return True
            return False

        # < and >
        def __le__(self, other):
            if self.seconds >= self.varify(other):
                return True
            return False


# c1 = Clock2(1000)
# c2 = Clock2(1000)
# print(c1 <= c2)


#16. Магические методы __eq__ и __hash__ +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class Point2:

    def __init__(self, x, y):
        self.x = x
        self.y = y

# Для того чтобы у двух объектов с одинаковыми значениями атрибутов был одинаковый хеш 
# Переопределяем метод магичкский метод __hash__, без его переопределения хеши двух обьектов 
# С одинаковыми значениями будут разными

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

# Если создать словарь после преопределения методов то если в качестве ключей взять объект класса с одинаковыми
#p1 = Point2(1, 2); p2 = Point2(1, 2) # Хеши будут равны если методы __eq__ и __hash__ переопределены
# d = {}
# d[p1] = 1
# d[p2] = 2
# Output = {<__main__.Point2 object at 0x7f2184ab9f90>: 2}
# Мы просто перезапишим значения т.к ключ будет только один

# Но если не переопределять методы __eq__ и __hash__, то мы создадим две записи в словаре 
# d = {}
# d[p1] = 1
# d[p2] = 2
# print(d)
# Output = {<__main__.Point2 object at 0x7f411a999f60>: 1, <__main__.Point2 object at 0x7f411a999fc0>: 2}


#17. Магический метод __bool__ определения правдивости объектов +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


class Point3:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __bool__(self):
        return self.x == self.y

# p1 = Point3(10, 1)

# if p1:
#     print('Объект p1 возвращает True')
# else:
#     print('Объект p1 возвращает False')

#18. Магические методы __getitem__, __setitem__ и __delitem__ +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class Student:
    def __init__(self, name: str, marks: list):
        self.name = name
        self.marks = list(marks)

    def varify(self, item):
        if 0 <= item <= len(self.marks):
            return item
        else:
            raise IndexError('Не вeрный индекс')

    def __getitem__(self, item):
            return self.marks[self.varify(item)]
        
    def __setitem__(self, item, value):
        if item >= len(self.marks):
            off = (item + 1) - len(self.marks)
            self.marks.extend([0]*off)
        self.marks[self.varify(item)] = value

    def __delitem__(self, item):
        del self.marks[self.varify(item)]


# s1 = Student('Sergy', [8, 4, 6, 2, 7])
# s1[2] == s1.marks[2]
# s1[15] = 20
# print(*s1)
# del s1[3]
# print(*s1)


#19. Магические методы __iter__ и __next__++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Создание итерируемых обьектов+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class FRange:
    def __init__(self, start = 0, stop = 0, step = 1):
        self.start = start
        self.stop = stop
        self.step = step
        

    def __next__(self):
        if self.value + self.step < self.stop:
            self.value += self.step
            return self.value
        else:
            raise StopIteration

    # Итератор
    def __iter__(self):
        self.value = self.start - self.step
        return self


class FRange2:
    def __init__(self, start = 0, stop = 0, step = 1, rows = 5):
        self.rows = rows
        self.fr = FRange(start, stop, step)

    def __next__(self):
        if self.value < self.rows:
            self.value += 1
            return iter(self.fr)
        else:
            raise StopIteration

    # Итератор
    def __iter__(self):
        self.value = 0
        return self

    
# f = FRange(0, 5)

# ff = list(map(float, f))
# print(ff)

# fr = FRange2(0 , 5, 1, 5)

# for row in fr:
#     for i in row:
#         print(i, end=' ')
#     print()

#20. Наследование в объектно-ориентированном программировании++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class Geom:
    name = 'Geom'
    # В родительском классе при вызове методов из обектов дочерних классов, пораметр self, ссылается на обекты дочерних классов
    def __init__(self, x1, x2, y1, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def Perim(self):
        print(self.x1 + self.x2 + self.y1 + self.y2)
    

# Два этих класса унаследовали методы и атрибуты родительского класса Geom
# В данных дочерних классах можно переопределить методы родительского класса
# Иерархия поиска методов и атрибутов начинается с класса от которого создан обект, если метода или атрибута в нём нет 
# тогда поиск переходит в родительский класс!

class Line(Geom):
    def drow(self):
        print('Drow line', self.x1, self.x2, self.y1, self.y2)

class Rect(Geom):
    def drow(self):
        print('Drow rect', self.x1, self.x2, self.y1, self.y2)

# l = Line(1, 2, 3, 4)
# r = Rect(2, 1, 4, 5)

# l.drow()
# r.drow()

# l.Perim()
# r.Perim()
# print(r.name)

# Объект класса Line наследуется от класса Geom
# print(isinstance(l, Geom)) -> True
# Класс Line наследуется от класса Geom
# print(issubclass(Line, Geom)) -> True


#22. Наследование. Функция super() и делегирование ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


class Geom2:
    name = 'Geom2'

    def __init__(self, x1, x2, y1, y2):
        print(f'call {self.__class__}')
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
    

class Line2(Geom2):

    def drow(self):
        print('Drow line')

class Rect2(Geom2):

    def __init__(self, x1, x2, y1, y2, fill = None):
        # Делегированный вызов (дополнение функционала базового класса)
        # через super() вызываем __init__ базового класса, и передаем агрументы, затем дополняем 
        # super() - возвращает обект базового класса
        super().__init__(x1, x2, y1, y2) 
        self.fill = fill

    def drow(self):
        print('Drow rect', self.x1, self.x2, self.y1, self.y2)

# l = Line2(1, 2, 3, 4)
# r = Rect2(2, 1, 4, 5)

# print(r.__dict__) ->{'x1': 2, 'x2': 1, 'y1': 4, 'y2': 5, 'fill': None}
# print(l.__dict__) ->{'x1': 1, 'x2': 2, 'y1': 3, 'y2': 4}


#23. Наследование. Атрибуты private и protected+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class Geom3:
    name = 'Geom3'

    def __init__(self, x1, x2, y1, y2):
        #__varify_coord - приватный метод только для класса в котором он определён, доступ в дочернем классе запрещен
        self.__varify_coord(x1)
        self.__x1 = x1 
        # __x1 Приватный атрибут, только для класса Geom3, не можем обратиться из дочернего класса, 
        # Только одя импользования в коассе в котором данный атрибут определен
        self._x2 = x2
        # _x2 и _y1 атрибуты защищенные из вне, испотзуются только внутри класса и во всех его дочерних классах
        #  Не нужно обращаться из вне, для работы в классах
        self._y1 = y1
        # Публичнай арибут 
        self.y2 = y2

    def __varify_coord(self, coord):
        return 0 <= coord

class Rect3(Geom3):

    def __init__(self, x1, x2, y1, y2, fill = None):
        super().__init__(x1, x2, y1, y2) 
        self.fill = fill

# r = Rect3(2, 1, 4, 5, 'red')
# print(r.__dict__) -> {'_Geom3__x1': 2, '_x2': 1, '_y1': 4, 'y2': 5, 'fill': 'red'}
# _Geom3__x1': 2 - защищённый атрибут базового класса, нет доступа из дочепнего класса


#24. Полиморфизм и абстрактные методы++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#Единый интерфейс для разных объектов

# Создадим базовый класс для того чтобы у каждого дочепнего класса был метод get_pr
# Методы которые обязательно должны быть переопределены и не имеют собственной реализации называются абстрактные 
# такие как абстрактные
 

class Geom4:
    def get_pr(self):
        raise NotImplementedError('В дочернем классе должен быть преопределённый метод get_pr')

class Rectangle(Geom4):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def get_pr(self):
        return 2*(self.h + self.w)

    
class Square(Geom4):
    def __init__(self, a):
        self.a = a
    
    def get_pr(self):
        return 4 * self.a

class Triangle(Geom4):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def get_pr(self):
        return self.a + self.b + self.c


# ob_list = [Rectangle(1, 2), Rectangle(10, 20), Square(1), Square(2), Triangle(1, 2, 3), Triangle(10, 20, 30)]

# У всех классов есть метод с одинаковым именем, вот и весь секрет

# [print(ob.get_pr()) for ob in ob_list]


#25. Множественное наследование++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Лучше избешать множественного наследования, а лучше знать но не юзать

class Goods():
    def __init__(self, name, weight, price):
        super().__init__() #Для вызова метода __init__ из второго по иерархии базового класса
        self.name = name
        self.weight = weight
        self.price = price

    def print_info(self):
        print(f"{self.name}, {self.weight}, {self.price}")

class WixinLog:
    ID = 0
    # Принято во втором и далее базовых классах по иерархии наследования 
    # определять пустой инициализатор
    def __init__(self):
        WixinLog.ID += 1
        self.id = WixinLog.ID

    def save_sell_log(self):
        print(f'{self.id} : товар был продан')
    

class NoteBook(Goods, WixinLog):
    # В начале по иерархии идет класс Goods, если метода нет в наследнике но есть в первом базовом классе то мы 
    # этот метод возьмём из первого базового класса, а если этого метода нету и в первом базовом клссе,
    # мы данный метод будем искать в следующем по иерархии наследования, т.е в классе WixinLog
    pass

# n = NoteBook('DEAL', 0.890, 1000) 
# n.print_info()#-> DEAL, 0.89, 1000
# n.save_sell_log()# -> 1 : товар был продан
# n = NoteBook('Aser', 1.4, 900)
# n.print_info()#-> 'Aser', 1.4, 900 
# n.save_sell_log()# -> 2 : товар был продан
# # Иерархия наследования -> print(NoteBook.__mro__)
# print(NoteBook.__mro__)#-> (<class '__main__.NoteBook'>, <class '__main__.Goods'>, <class '__main__.WixinLog'>, <class 'object'>)


#26. Коллекция __slots__+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Ограничение создаваемых локальных св-тв ++++++++++++++++
# Уменьшение занимаемой памяти +++++++++++++++++++++++++++
# Ускорение работы с локальными св-тв ++++++++++++++++++++

class Point4:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    #test time metod
    def calc(self):
        self.x += 1
        del self.y
        self.y = 0

class Point4D:
    # Колекция __slots__ ограничевает количество и имя аргументов, при ее объявлении не создаётся колекция __dict__
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

    #test time metod
    def calc(self):
        self.x += 1
        del self.y
        self.y = 0

# p1 = Point4(10, 20)
# p2 = Point4D(10, 20)
# t1 = timeit.timeit(p1.calc)# -> 1.4474129036000304
# t2 = timeit.timeit(p2.calc)# -> 1.2391529519995856
# print(t1, t2, sep='\n')



# 27. Как работает __slots__ с property и при наследовании ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



class Point5D:
    # Колекция __slots__ ограничевает количество и имя аргументов, при ее объявлении не создаётся колекция __dict__
    __slots__ = ('x', 'y')
    # При объявлении локальных свойств (методов), колекция __slots__ на них действовать не будет

    def __init__(self, x, y):
        self.x = x
        self.y = y

class Point6D(Point5D):
    # Если в дочернем классе определить __slots__ то он не переопределяет __slots__ в базовом классе, а дополняет его 
    # при этом если мы определим в дочернем классе __slots__, то у дочернего класса не будет колекшии __dict__
    # И в дочернем классе мы не сможем добовлять локальные свойства, 
    # которых нет в колекции __slots__ ни в базовом ни в дочернем клссах 
    # При этом если переопределить метод __init__, то в __dict__ дочернего класса будут присудствовать все 
    # определённые в нем локальные свойства, что логично, но на всякий напишу
    pass
# Мы можем создавать локальные св-ва которые не входят в колекцию __slots__ базового класса 
# p = Point6D(1, 2)
# p.z = 3
# Выведет только {'z': 3}, т.к у базового класса нет коллекции __dict__, т.к. в нем оределена колекция __slots__
# print(p.__dict__)# -> {'z': 3}
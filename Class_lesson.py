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
затем писем геи с таимже именем как и у гет
и оборачиваем в @old.setter
где old = имя геттера, а .setter = мия декоратора в @property
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
    


#p = Person('Бычковский Владислав Александрович', 22, '1234 564489', 65.40)

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

#14 Магические методы __add__, __sub__, __mul__, __truediv__ 

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


#c1 = Clock(2000)
#c2 = Clock(1000)
#c1 = c1 + 110
#c1 -= 110


#print(c1.get_time())
#print(c1.get_time())
#print(c4.get_time())

#15. Методы сравнений __eq__, __ne__, __lt__, __gt__ 

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

#c1 = Clock2(1000)
#c2 = Clock2(1000)
#print(c1 <= c2)

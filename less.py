import requests
from bs4 import BeautifulSoup as bs
import sys

def main():
    a = ['a', 'b', 'c']
    b = ['good']
    print(searh_str('ab d bad'.split(), a, b))

def searh_str(text, a, b):
    for word in text:
        if word not in a and word in b:
            return 'Проверка  пройдена'
    return 'Проверка no пройдкна'


if __name__ == '__main__':
    main()

import re

class Test1:
    
    # def method_re_decorator(func):
    #     def wrapper(self, *args, **kwargs):
    #         text, word = args
    #         words = f'//b{word}//b'
    #         result = func(text, words)
    #         print(text, words)
    #         return result
    #     return wrapper

    # @method_re_decorator
    def serch_word(self, text: str, word: str):
        return re.findall(word, text)

with open('text.txt', 'r') as file:
    test_info = []
    for line in file:
        test_info.append(line.strip())

t = Test1()
print(t.serch_word(test_info[1], 'не'))
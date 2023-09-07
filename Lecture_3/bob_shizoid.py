import string

numbers: str = string.digits
##print(numbers)

word: str = "hel11lo bo01b yo2u ar3e shi13zoid"

##for number in numbers:
##    word = word.replace(number, '')
##print(word.replace(numbers, ''))

_word: str = ''
##_sum: int = 0 запомнить
##_prod: float = 1.0
##_list: list = []
##_set: set = set([])
##_dict: dict = {}

for ch in word:
    if ch in numbers:
        continue
    else:
        _word += ch
word = _word
del _word
print(word)


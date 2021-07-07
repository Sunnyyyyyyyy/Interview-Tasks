import re
from collections import Counter


# Відділити тільки букви з тексту (в список)
text = re.findall(r'\w', input().lower())
# Загальна кількість букв
length = len(text)
# Counter рахує кількість всіх елементів в списку (наслідується від dict, тому працює метод items)
for item, value in Counter(text).items():
    print(f'{item} - {value}')
    print(f'{item} - {value/length}')
    print("--------------------------")

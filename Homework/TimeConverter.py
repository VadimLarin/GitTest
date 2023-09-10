sec = int(input('введите время в секундах, чтобы сконвертировать в часы и минуты --> '))
hour: int = 0
min: int = 0

if sec / 3600 > 0:
    hour = sec // 3600
    if sec / 60 > 0 and hour == 0:
        min = sec // 60
else: 
    hour, min = 0, 0

print(hour, 'час(а/ов) и', min, 'минут(а/ы)')
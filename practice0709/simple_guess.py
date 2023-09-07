
number = int(input('введите число -->  '))

x = -1

def guess(number):
    global x ## долго ломал голову, как же быть с переменными, так как доступ к локальной ограничен, нашел полезное для себя решение по этой ссылке https://thecode.media/unboundlocalerror/ 
##    if number == 1:
##        return number
##    else:
    for i in range(-1, number):
        x = x + 1
        if i * i == number:
            y = i
##                x = x + 1
##                print(x)
            return y
        elif i * i != number & x == i:
##                print(x)
##                print(i)
            c = "слишком сложно, не могу"
            return c
                
##            elif d == number :
##                print("такого корня нет")
##            else:
##                y: str = 'такого корня нет'
##                return y

                    
                                          
w = str(guess(number))

print(w.lstrip("-"))
                

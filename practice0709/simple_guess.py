
number = int(input('введите число -->  '))

x = -1

def guess(number):
    global x
    if number == 1:
        return number
    else:
        for i in range(number):
            x = x + 1
            if i * i == number:
                y = i
##                x = x + 1
##                print(x)
                return y
            elif i * i != number & x == i:
##                print(x)
##                print(i)
                c = "Трудно, не могу вычислить корень"
                return c
                
##            elif d == number :
##                print("такого корня нет")
##            else:
##                y: str = 'такого корня нет'
##                return y

                    
                                          
w = guess(number)
print(w)
                
            
import colorama


def funck_1():
    pass

class Human:
    pass

cr=colorama
fun=funck_1
nick=Human

print(colorama.__name__)
print(cr.__name__)
print(fun.__name__)
print(funck_1.__name__)
print(Human.__name__)
print(nick.__name__)
print(__name__)

#Ми дослідили справжні імена об'єктів

print(type(2))
print(type(2.9))
print(type(2==2))
print(type('ihohohoi'))
print(type(list))

#Ми дізнались типи данних

intro_list=[]
for method in dir(intro_list):
    print(method)

#Ми дізались всі атрибути і методи,
#найголовніші для мене-remove reverse
#remove-видаляє revers-реверсує



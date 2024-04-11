global var1
var1 = 'глобальная'


def my_func():
    global var1
    global var2
    var1 = "синяя"
    var2 = 'вторая'
    print(var1)


print(var1)
my_func()
print(var2)
var2 = 'var2 теперь глобальная'
print(var2)
# глобальная, синяя, вторая, вторая, var2 теперь глобальная
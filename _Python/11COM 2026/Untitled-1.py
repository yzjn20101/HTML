class Person:
    def __init__(self, first, last):
        self.first_name = first
        self.last_name = last

    def full_name(self):
        return self.first_name + ' ' + self.last_name
    
    def say_hello(self, to):
        print(f'hello, {to}! My name is {self.full_name()}')

mr_mcleod = Person('Mr', 'Mcleod')
print( mr_mcleod.last_name )
print( mr_mcleod.last_name )
print( mr_mcleod.full_name() )


mr_mcleod.say_hello('World')

Junan = Person('Junan', 'Yu')


class Student(Person):
    def __init__(self, first, last, whanau):
        super().__init__(first, last)
        self.whanau = whanau

    def study(self):
        print('I am studying! ')

    def say_hello(self, to):
        super().say_hello(to)
        print(f'My whanau is {self.whanau}')

Junan = Student('Junan', 'Yu', 'po')
Junan.say_hello('est')
Junan.study()
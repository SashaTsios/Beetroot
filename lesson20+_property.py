class Person:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return f'{self.first_name.title()} {self.last_name.title()}'

    @property
    def email(self):
        return f'{self.first_name.lower()}.{self.last_name.lower()}@email.com'

    @full_name.setter
    def full_name(self, name):
        first, last = name.split('')
        self.first_name = first
        self.last_name = last


alex = Person('alex', 'tsios')
print(alex.first_name)
print(alex.last_name)
print(alex.email)
print(alex.full_name)
alex.first_name = 'bob'
print(alex.first_name)
print(alex.last_name)
print(alex.email)
print(alex.full_name)
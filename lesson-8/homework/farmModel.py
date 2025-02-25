class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def walking(self):
        print('walking')
    def eating(self):
        print('eating')
    def running(self):
        print('running')
    def sleeping(self):
        print('sleeping')
class Lion(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
    def roaring(self):
        print('roaring')
class Dog(Animal):
    def __init__(self, name, age):
        super.__init__(name, age)
    def barking(self):
        print('barking')
class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
    def meaowing(self):
        print('meowing')
lion = Lion('Simba',12)
dog = Dog('Dog',13)
cat = Cat('Cat',14)
lion.walking()
dog.running()
cat.eating()
lion.roaring()
cat.meaowing()
dog.barking()



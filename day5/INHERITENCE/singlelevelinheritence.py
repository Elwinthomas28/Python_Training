class dog:
    def sound():
        print('BOW BOW')
    def eat(self):
        print("dog is eating")
class cat(dog):
    def sound():
        print("MEOW MEOW")
d=cat()
d.eat()
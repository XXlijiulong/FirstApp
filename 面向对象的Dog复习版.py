class Dog:
    def __init__(self,color,age,weight,type,name):
        self.color=color
        self.age=age
        self.weight=weight
        self.type=type
        self.name=name
    def eat(self):
        print("{} is eating".format(self.name))
    def run(self):
        print("{} is running".format(self.name))
    def sleep(self):
        print("{} is sleeping".format(self.name))
if __name__ == '__main__':
    jeff=Dog("black",3,2,"a","jeff")
    jeff.eat()
    jeff.run()
    jeff.sleep()
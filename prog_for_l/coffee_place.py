class Coffee:
    def __init__(self, country, roast, taste):
        self.country = country
        self.roast = roast
        self.taste = taste
    def taste_coffee(self):
        return self.country + ' tastes ' + self.taste
    def roast_coffee(self):
        return self.country + ' is roasted ' + self.roast

class Barista(Coffee):
    def __init__(self, name, method, country, roast, taste):
        self.name = name
        self.method = method
        super(Barista, self).__init__(country, roast, taste)
    def say_hello(self):
        print('Hello, my name is ' + self.name + ', I am your barista today')
    def cook_coffee(self, coffee):
        print('I will cook you ' + coffee.country + ' using ' + self.method)
    def describe_coffee(self, coffee):
        tst = coffee.taste_coffee()
        rst = coffee.roast_coffee()
        print(tst + ', ' + rst)

class Admin(Barista):
    def __init__(self, name, method, country, roast, taste, workers):
        self.workers = workers
        super(Admin, self).__init__(name, method, country, roast, taste)
    def hire(self, barista):
        return self.workers.append(barista.name)
    def provide_coffee(self, coffee):
        print('Today I will roast the ' + coffee.country + ' coffee ' + coffee.roast)

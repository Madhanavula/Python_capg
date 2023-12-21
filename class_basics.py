class student():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greet(self):
        print(f"hi {self.name}")




s1=student("hello",45)
s1.greet()
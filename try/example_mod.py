def world():
    print("hello world")

name = "vidy"

class Elephant:
    def __init__(self, name, color) -> None:
        self.name = name
        self.color = color

    def describe_me(self):
        print(f"This elephant is {self.color}.")
        print(f"{self.name} is the elephant's name.") 
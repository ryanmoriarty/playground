class MyClass:
    variable = "blah"
    thingtoprint = None

    def function(self):
        print(self.thingtoprint)

if __name__ == '__main__':
    a_game = MyClass()
    a_game.function()

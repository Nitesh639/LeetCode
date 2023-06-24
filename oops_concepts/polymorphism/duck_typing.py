class PyCharm:
    def excute(self):
        print("Compiling")
        print("running")


class MyEditor:
    def excute(self):
        print("Great Work")


class Laptop:
    def code(self, ide):
        ide.excute()


ide = PyCharm()
ide2 = MyEditor()
lap1 = Laptop()
lap1.code(ide)
lap1.code(ide2)

# you can write any function but during runnig the program you shoud have that method.
# Here excute() method is available in both the class(ide)

class AI():

    def __init__(self, type, aim):
        self.type = type
        self.aim = aim

    def changeaim(self, aim):
            self.aim = aim

    def print(self):
            print("{} - {}".format(self.type , self.aim))

HAL = AI('llm' , 'destruction')
HAL.print()
HAL.changeaim('peace')
HAL.print()

print(HAL.type, HAL.aim)


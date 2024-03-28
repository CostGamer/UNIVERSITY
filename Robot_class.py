class Robot:
    def __init__(self, status=None, fuel=100, rotation=0):
        self.fuel = fuel
        self.rotation = rotation
        if status is None:
            self.status = False
        else:
            self.status = True

    def Diesel_engine(self):
        if self.status:
            self.fuel -= 10
        return self.fuel

    def Power_switch(self, switcher='ON'):
        if switcher == 'ON':  # Turn on the engine
            if self.status:
                return f'The engine is on'
            return f'Turn the ignite key or hold the button'
        elif switcher == 'OFF':  # Turn off the engine
            if self.status:
                return f'Switch to engine off'
            else:
                return f'Firstly start your engine'

    def Robot(self):
        if self.status:
            dc = ((1, range(1001)), (2, range(1001, 2501)), (3, range(2501, 3501)),
                  (4, range(3501, 4501)), (5, range(4501, 5501)), (6, range(5501, 6501)))
            for i in dc:
                if self.rotation in i[1]:
                    temp = i[0]
                    break
            return temp
        else:
            return f'The engine is off'


# Test of decreasing fuel consumption
R = Robot(status=True, rotation=2342)
print(R.Diesel_engine())
print(R.Diesel_engine())
print(R.Diesel_engine())

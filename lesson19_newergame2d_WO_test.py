class Car:

    def __init__(self, brand='Chery', model='Amulet', color='Grey', speed=1, position=[0, 0]):
        if not brand:
            self.brand = 'Chery' 
        else:
            self.brand = brand
        if not model:
            self.model = 'Amulet'
        else:
            self.model = model
        if not color:
            self.color = 'Grey'
        else:
            self.color = color
        if not speed:
            self.speed = 1
        else:
            self.speed = speed
        if not speed:
            self.position = [0, 0]
        else:
            self.position = position
        print(f'Your {self.color} car {self.brand} {self.model} is ready to start!\n')

    def change_speed(self, speed):
        self.speed = speed
        print(f'Your current speed is {self.speed}')
        return self.speed

    def default_position(self):
        self.position = [0, 0]
        print(f'Your current position is {self.position}')
        return self.position

    def current_position(self):
        print(f'Your current position is {self.position}')
        return self.position

    def info(self):
        print(f'Your current speed is {self.speed} and your are located in {self.position}')

    def move_left(self, steps=1, speed=''):
        if not speed:
            self.speed = self.speed
        else:
            self.speed = speed
        self.steps = steps
        self.position[0] -= (int(self.steps) * int(self.speed))
        print(f'You moved {self.steps} steps left with speed of {self.speed} to the position of {self.position}')
        return self.position

    def move_right(self, steps=1, speed=''):
        if not speed:
            self.speed = self.speed
        else:
            self.speed = speed
        self.steps = steps
        self.position[0] += (int(self.steps) * int(self.speed))
        print(f'You moved {self.steps} steps right with speed of {self.speed} to the position of {self.position}')
        return self.position

    def move_down(self, steps=1, speed=''):
        if not speed:
            self.speed = self.speed
        else:
            self.speed = speed
        self.steps = steps
        self.position[1] -= (int(self.steps) * int(self.speed))
        print(f'You moved {self.steps} steps down with speed of {self.speed} to the position of {self.position}')
        return self.position

    def move_up(self, steps=1, speed=''):
        if not speed:
            self.speed = self.speed
        else:
            self.speed = speed
        self.steps = steps
        self.position[1] += (int(self.steps) * int(self.speed))
        print(f'You moved {self.steps} steps up with speed of {self.speed} to the position of {self.position}')
        return self.position


# car1 = Car('Chery', 'Amulet', 'grey', 4)
# car1.info()
# car1.move_left(5, 2)
# car1.info()
# car1.move_left(6)
# car1.move_up(10)
# car1.move_right(1, 10)
# car1.move_up(10)
# car1.default_position()
# car1.info()
# car1.change_speed(3)
# car1.move_left(6)
# car1.move_left(6, 1)
# car1.info()
# car1.current_position()

def main(car1):
    new_round = True
    while new_round:
        user_direction = input('Please enter your action (i for Info), (w a s d to move), (o to change position to 0, 0), (q to Quit): ')
        if user_direction.lower() == 'i':
            car1.info()
        elif user_direction.lower() == 'o':
            car1.default_position()
        elif user_direction.lower() == 'q':
            new_round = False
        else:
            step = int(input('Please enter a distance to move: '))
            user_speed = int(input('Please enter speed per move: '))
            allowed_actions = ('w', 'a', 's', 'd', 'q', 'i')

            while True:
                if user_direction.lower() in allowed_actions:
                    if user_direction.lower() == 'w':
                        car1.move_up(step, user_speed)
                        break
                    if user_direction.lower() == 'a':
                        car1.move_left(step, user_speed)
                        break
                    if user_direction.lower() == 's':
                        car1.move_down(step, user_speed)
                        break
                    if user_direction.lower() == 'd':
                        car1.move_right(step, user_speed)
                        break
                    if user_direction.lower() == 'q':
                        new_round = False
                        break
                    if user_direction.lower() == 'i':
                        new_round = False
                        car1.info()
                        break
    print('Bye')

if __name__ == '__main__':
    car_brand = input('Enter car brand: ')
    car_model = input('Enter car model: ')
    car_color = input('Enter car color: ')
    car_x = Car(car_brand, car_model, car_color)    
    main(car_x)


    #     allowed_actions_dict = {'d': car1.move_right(step, user_speed), 'a': car1.move_left(step, user_speed)}
    #     return allowed_actions_dict[user_direction]
    # else:
    #     print('Wrong input')
# start = True
# while start:
#     pass  'w': car1.move_up(step, user_speed), 's': car1.move_down(step, user_speed), 
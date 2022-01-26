class CoffeMachine:
    # ингридиентов в кофеварке
    def __init__(self):
        self.money = 550
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9

    # CustomError(собственный) - пользовательское исключение
    # Exception(встроенный) - заканчиваются полностью системные исключения  и начинаются обыкновенные, с которыми можно работать.

    # кол-во каждого ингридиента в машине
    def print_state(self):
        print("The coffee machine has:")
        print(self.water, "of water")
        print(self.milk, "of milk")
        print(self.beans, "of coffee beans")
        print(self.cups, "of disposable cups")
        print(f"$ {self.money} of money")

    # выбор действия
    def select_action(self):
        done = False
        while not done:
            print("ATTENCION!!! Here you must write words no numbers!")
            action = input('Write action:\n 1-buy\n 2-fill\n 3-take\n 4-remaining\n 5-exit\n:')
            if action == "buy":
                CoffeMachine.buy(self)
            elif action == "fill":
                CoffeMachine.fill(self)
            elif action == "take":
                CoffeMachine.take(self)
            elif action == "remaining":
                CoffeMachine.select_coffe(self)
            elif action == "exit":
                done = True
            else:
                print("invalid choice")

    # выбор 1 из 3 вариантов кофе
    def select_coffe(self):
        print()
        move = input('What do you want to buy?'
                     ' 1 - espresso,'
                     ' 2 - latte,'
                     ' 3 - cappuccino,'
                     ' 4 - back to main menu: ')
        if move == '4':
            return 0
        return int(move)

    # проверка ,на ,достаточно ли ингр. в машине
    def is_enough(self, needed_water, needed_milk, needed_coffee):
        if self.water < needed_water:
            print('Sorry, not enough water!')
            return False
        if self.milk < needed_milk:
            print('Sorry, not enough milk!')
            return False
        if self.beans < needed_coffee:
            print('Sorry, not enough beans!')
            return False
        if self.cups < 1:
            print('Sorry, not enough cups\n')
            return False
        print('I have enough resources, making you a coffee!\n')
        return True

    # функция, для покупки кофе(1-ecпрессо,2-латте,3-капучино)
    def buy(self):
        drink = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        if drink == "back":

            return
        elif drink == '1':
            if CoffeMachine.is_enough(self, 250, 0, 16):
                self.water -= 250
                self.beans -= 16
                self.money += 4
                self.cups -= 1
        elif drink == '2':
            if CoffeMachine.is_enough(self, 350, 75, 20):
                self.water -= 350
                self.milk -= 75
                self.beans -= 20
                self.money += 7
                self.cups -= 1
        elif drink == '3':
            if CoffeMachine.is_enough(self, 200, 100, 12):
                self.water -= 200
                self.milk -= 100
                self.beans -= 12
                self.money += 6
                self.cups -= 1
        else:
            print('invalid choice')
            return CoffeMachine.buy(self)

    # функция,для наполнения кофемашины
    def fill(self):
        self.water += int(input('Write how many ml of water do you want to add: '))
        self.milk += int(input('Write how many ml of milk do you want to add: '))
        self.beans += int(input('Write how many grams of coffee beans'
                                ' do you want to add: '))
        self.cups += int(input('Write how many disposable cups of coffee'
                               ' do you want to add: '))

    #  функция, для изьятия денег из машины
    def take(self):

        print()
        print(f'I gave you {self.money} griven')
        self.money = 0


if __name__=="__main__":
    coffe = CoffeMachine()
    coffe.buy()

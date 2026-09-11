class Player:
    def __init__(self, name, element):
        self.__name = name
        self.__element = element
        self.__health = 100

    def get_name(self):
        return self.__name
    def get_element(self):
        return self.__element
    def get_health(self):
        return self.__health

# SPELLS
# fire
def fire_attack():
    print("fire ow hot")

# water
def water_attack():
    print("water oh no drown")

# ice
def frost_bite():
    print("oh no too cold")

# earth
def hulk_smash():
    print("hulk smash")



print("Welcome to Wizard Duels")

#player 1 creation
player1_name = input("Enter player 1 name: ")
player1_element = input("Enter player 1 element type: ")
player1 = Player(player1_name, player1_element)
player1_health = player1.get_health()

#player 2 creation
player2_name = input("Enter player 2 name: ")
player2_element = input("Enter player 2 element type: ")
player2 = Player(player2_name, player2_element)
player2_health = player2.get_health()

while player1_health > 0 and player2_health > 0:
    print(player1_name, " pick an attack")
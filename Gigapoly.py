# Author: Aleksandra Kaznowska
# Gigapoly - Simplified Monopoly Console Game in Python

import random
import time

STARTING_MONEY = 1500
BOARD_SIZE = 16
PASS_START_REWARD = 200

COMPONENT_CATEGORIES = {
    "Graphics Card": 2,
    "Processor": 2,
    "Hard Drive": 2,
    "RAM": 2,
    "Network Card": 2,
    "Komputronik": 2
}

SPECIAL_FIELDS = ["Start", "Chance", "Risk", "Neostrada"]

class Player:
    def __init__(self, name):
        self.name = name
        self.money = STARTING_MONEY
        self.position = 0
        self.owned = []

    def move(self, steps):
        prev_position = self.position
        self.position = (self.position + steps) % BOARD_SIZE
        if self.position < prev_position:
            self.money += PASS_START_REWARD
            print(f"{self.name} passed Start and received ${PASS_START_REWARD}!")

    def pay(self, amount, recipient=None):
        if self.money >= amount:
            self.money -= amount
            if recipient:
                recipient.money += amount
        else:
            self.money = 0  # Bankrupt

    def is_bankrupt(self):
        return self.money <= 0

    def owns_all_category(self, category):
        count = sum(1 for field in self.owned if field.category == category)
        return count == COMPONENT_CATEGORIES[category]

class Field:
    def __init__(self, name, category=None, price=0, rent=0):
        self.name = name
        self.category = category
        self.price = price
        self.rent = rent
        self.owner = None

    def landed_on(self, player, players):
        if self.category is None:
            if self.name == "Chance":
                chance_deck.draw(player)
            elif self.name == "Risk":
                risk_deck.draw(player)
            elif self.name == "Neostrada":
                self.neostrada_teleport(player)
        else:
            if self.owner is None:
                self.buy_property(player)
            elif self.owner != player:
                rent_due = self.rent * (2 if self.owner.owns_all_category(self.category) else 1)
                print(f"{player.name} landed on {self.name} owned by {self.owner.name} and owes ${rent_due}")
                player.pay(rent_due, self.owner)

    def buy_property(self, player):
        choice = input(f"{player.name}, do you want to buy {self.name} for ${self.price}? (y/n): ")
        if choice.lower() == 'y' and player.money >= self.price:
            player.money -= self.price
            player.owned.append(self)
            self.owner = player
            print(f"{player.name} bought {self.name}!")
        elif choice.lower() == 'y':
            print("Not enough money to buy this property.")

    def neostrada_teleport(self, player):
        destination = int(input(f"{player.name}, choose a position to teleport to (0-{BOARD_SIZE - 1}): "))
        player.position = destination
        print(f"{player.name} teleported to position {destination}.")

class Deck:
    def __init__(self, cards):
        self.cards = cards[:]
        self.used = []
        random.shuffle(self.cards)

    def draw(self, player):
        if not self.cards:
            self.cards = self.used[:]
            self.used = []
            random.shuffle(self.cards)
        card = self.cards.pop()
        self.used.append(card)
        card(player)


def gain_bonus(player):
    bonus = random.randint(50, 200)
    player.money += bonus
    print(f"{player.name} gains a bonus of ${bonus}!")

def move_forward(player):
    steps = random.randint(1, 6)
    player.move(steps)
    print(f"{player.name} moves forward {steps} spaces.")

def extra_turn(player):
    print(f"{player.name} gets an extra turn!")
    play_turn(player)

def lose_random_property(player):
    if player.owned:
        lost = random.choice(player.owned)
        player.owned.remove(lost)
        lost.owner = None
        print(f"{player.name} lost ownership of {lost.name}!")

def no_effect(player):
    print(f"{player.name} was unaffected this time.")

chance_cards = [gain_bonus, move_forward, extra_turn]
risk_cards = [gain_bonus, lose_random_property, no_effect]
chance_deck = Deck(chance_cards)
risk_deck = Deck(risk_cards)

def create_board():
    board = [Field("Start")]
    for cat, count in COMPONENT_CATEGORIES.items():
        for i in range(count):
            board.append(Field(f"{cat} {i+1}", cat, price=100 + i*50, rent=50 + i*25))
    board.append(Field("Chance"))
    board.append(Field("Risk"))
    board.append(Field("Neostrada"))
    while len(board) < BOARD_SIZE:
        board.insert(random.randint(1, len(board)-1), Field("Chance" if len([f for f in board if f.name == "Chance"]) < 2 else "Risk"))
    return board[:BOARD_SIZE]

def play_turn(player):
    input(f"{player.name}, press Enter to roll the dice...")
    roll = random.randint(1, 6)
    print(f"{player.name} rolled a {roll}.")
    player.move(roll)
    print(f"{player.name} is now at position {player.position}.")
    field = board[player.position]
    print(f"You landed on {field.name}.")
    field.landed_on(player, players)
    print(f"{player.name}'s money: ${player.money}")
    time.sleep(1)

def check_win_conditions(player):
    if player.is_bankrupt():
        print(f"{player.name} has gone bankrupt. Game over!")
        return True
    categories_owned = set(field.category for field in player.owned if field.category)
    if len(categories_owned) == len(COMPONENT_CATEGORIES):
        print(f"{player.name} has built a complete computer! {player.name} wins!")
        return True
    return False

if __name__ == "__main__":
    print("Welcome to Gigapoly!")
    players = [Player(input("Enter name for Player 1: ")), Player(input("Enter name for Player 2: "))]
    board = create_board()

    game_over = False
    while not game_over:
        for player in players:
            play_turn(player)
            if check_win_conditions(player):
                game_over = True
                break

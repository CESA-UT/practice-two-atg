from card import PlantCard

class UI:
    def __init__(self):
        self.cards = [
            PlantCard("Peashooter", 100, 5),
            PlantCard("Sunflower", 50, 3),
            PlantCard("Wall-nut", 50, 15)
        ]

    def display_ui(self):
        print("=== GAME UI ===")
        print("Available Plant Cards:")
        for index, card in enumerate(self.cards):
            status = "Ready" if card.is_ready else "Recharging"
            print(f"{index + 1}. {card.plant_name} - Cost: {card.cost} [{status}]")

    def get_card(self, index):
        if 0 <= index < len(self.cards):
            return self.cards[index]
        return None

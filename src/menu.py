class Menu:
    def __init__(self):
        self.options = ["Start Game", "Instructions", "Exit"]
        self.current_selection = 0

    def display_menu(self):
        print("=== PLANTS VS ZOMBIES MENU ===")
        for index, option in enumerate(self.options):
            prefix = "-> " if index == self.current_selection else "   "
            print(f"{prefix}{index + 1}. {option}")

    def next_option(self):
        self.current_selection = (self.current_selection + 1) % len(self.options)

    def select_option(self):
        selected = self.options[self.current_selection]
        print(f"Selected: {selected}")
        return selected
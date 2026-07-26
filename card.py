class PlantCard:
    def __init__(self, plant_name, cost, recharge_time):
        self.plant_name = plant_name
        self.cost = cost
        self.recharge_time = recharge_time
        self.is_ready = True

    def can_afford(self, current_suns):
        return current_suns >= self.cost

    def use_card(self, sun_manager):
        if self.is_ready and self.can_afford(sun_manager.suns):
            sun_manager.spend_sun(self.cost)
            self.is_ready = False  # نیاز به زمان شارژ مجدد
            return True
        return False
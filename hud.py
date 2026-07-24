class HUD:
    def __init__(self, sun_manager, wave_number=1):
        self.sun_manager = sun_manager
        self.wave_number = wave_number

    def display_hud(self):
        print("+----------------------------------------+")
        print(f"| Suns: {self.sun_manager.suns:<15} Wave: {self.wave_number:<10} |")
        print("+----------------------------------------+")

    def update_wave(self, new_wave):
        self.wave_number = new_wav
import random
from zombies.normal_zombie import NormalZombie

class WaveManager:
    def __init__(self, spawn_x=900, row_y_positions=None):
        """
        spawn_x: نقطه شروع اسپاون زامبی در سمت راست (X)
        row_y_positions: لیست مختصات Y مرکز ۵ ردیف بازی [y0, y1, y2, y3, y4]
        """
        self.spawn_x = spawn_x
        self.row_y_positions = row_y_positions or [120, 200, 280, 360, 440]
        
        self.current_wave = 0
        self.max_waves = 3
        
        self.wave_config = [
            {"count": 3, "delay": 4.0},  
            {"count": 5, "delay": 3.0},   
            {"count": 8, "delay": 2.0}   
        ]
        
        self.spawned_in_wave = 0
        self.timer = 0.0
        self.wave_cooldown = 0.0
        self.is_waiting_for_next_wave = False
        self.game_won = False

    def start_next_wave(self):
        if self.current_wave < self.max_waves:
            self.current_wave += 1
            self.spawned_in_wave = 0
            self.timer = 0.0
            self.is_waiting_for_next_wave = False
            print(f"=== Wave {self.current_wave} Started! ===")

    def update(self, dt, active_zombies):
        """
        dt: زمان بگذشته در هر فریم (مثلا ۱/۶۰)
        active_zombies: لیست زامبی‌های زنده توی بازی
        """
        if self.game_won:
            return

        if self.current_wave == 0:
            self.start_next_wave()
            return

        if self.current_wave >= self.max_waves and self.spawned_in_wave >= self.wave_config[-1]["count"]:
            if len(active_zombies) == 0:
                self.game_won = True
                print("🎉 YOU WIN! All waves cleared!")
            return

        if self.is_waiting_for_next_wave:
            self.wave_cooldown += dt
            if self.wave_cooldown >= 7.0: 
                self.start_next_wave()
            return

        current_info = self.wave_config[self.current_wave - 1]

        if self.spawned_in_wave < current_info["count"]:
            self.timer += dt
            if self.timer >= current_info["delay"]:
                self.spawn_zombie(active_zombies)
                self.timer = 0.0
        else:
            if len(active_zombies) == 0:
                self.is_waiting_for_next_wave = True
                self.wave_cooldown = 0.0

    def spawn_zombie(self, active_zombies):
        row = random.randint(0, 4)  
        y = self.row_y_positions[row]
        
        new_zombie = NormalZombie(x=self.spawn_x, y=y, row=row)
        active_zombies.append(new_zombie)
        self.spawned_in_wave += 1
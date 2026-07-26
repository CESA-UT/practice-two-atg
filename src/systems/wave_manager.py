import random
from zombies.normal_zombie import NormalZombie


class WaveManager:
    def __init__(self, spawn_x=900, row_y_positions=None):
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

        self.banner_text = "GAME STARTED!"
        self.phase = "game_start"
        self.phase_timer = 2.0

    def start_next_wave(self):
        if self.current_wave < self.max_waves:
            self.current_wave += 1
            self.spawned_in_wave = 0
            self.timer = 0.0
            self.is_waiting_for_next_wave = False

            if self.current_wave == 1:
                self.phase = "wave_msg"
                self.phase_timer = 2.0
                self.banner_text = "WAVE 1"
            else:
                self.phase = "start_msg"
                self.phase_timer = 2.0
                self.banner_text = "A HUGE WAVE IS APPROACHING!"

    def update(self, dt, active_zombies):
        if self.game_won:
            return

        if self.phase == "game_start":
            self.phase_timer -= dt
            if self.phase_timer <= 0:
                self.start_next_wave()
            return

        if self.phase == "start_msg":
            self.phase_timer -= dt
            if self.phase_timer <= 0:
                self.phase = "pause_before_wave"
                self.phase_timer = 1.0
                self.banner_text = ""
            return

        if self.phase == "pause_before_wave":
            self.phase_timer -= dt
            if self.phase_timer <= 0:
                self.phase = "wave_msg"
                self.phase_timer = 2.0
                if self.current_wave == self.max_waves:
                    self.banner_text = "FINAL WAVE!"
                else:
                    self.banner_text = f"WAVE {self.current_wave}"
            return

        if self.phase == "wave_msg":
            self.phase_timer -= dt
            if self.phase_timer <= 0:
                self.phase = "spawning"
                self.banner_text = ""
            return

        if self.current_wave >= self.max_waves and self.spawned_in_wave >= self.wave_config[-1]["count"]:
            if len(active_zombies) == 0:
                self.game_won = True
            return

        if self.is_waiting_for_next_wave:
            self.wave_cooldown += dt
            if self.wave_cooldown >= 7.0:
                self.start_next_wave()
            return

        if self.phase == "spawning":
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
import pygame

from settings import WIDTH, HEIGHT, FPS, TITLE
from plants.peashooter import Peashooter
from plants.sunflower import Sunflower
from plants.wallnut import WallNut
from zombies.normal_zombie import NormalZombie
from systems.collision import Collision
from systems.wave_manager import WaveManager
from board import Board
from card import PlantCard


class Game:
    def __init__(self):
        pygame.init()
        pygame.font.init()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)

        self.clock = pygame.time.Clock()
        self.running = True

        # تنظیمات شبکه زمین بازی
        self.grid_start_x = 100  
        self.cell_width = 80     
        self.cols = 9            
        self.rows = 5            
        self.row_y = [160, 240, 320, 400, 480]  

        # ساخت برد و کارت‌ها (اضافه شدن کارت گردو به عنوان کارت سوم)
        self.board = Board(rows=self.rows, cols=self.cols)
        self.cards = [
            PlantCard(plant_name="peashooter", cost=100, recharge_time=5.0),
            PlantCard(plant_name="sunflower", cost=50, recharge_time=7.5),
            PlantCard(plant_name="wallnut", cost=50, recharge_time=15.0)
        ]
        self.selected_card = None

        self.plants = []
        self.zombies = []
        self.projectiles = []
        self.wave_manager = WaveManager(spawn_x=WIDTH, row_y_positions=self.row_y)

        self.sun_score = 150
        
        # تعریف فونت‌ها
        self.sun_font = pygame.font.Font(None, 36)
        self.card_font = pygame.font.Font(None, 22)
        self.font = pygame.font.Font(None, 80)
        self.banner_font = pygame.font.Font(None, 52)

        self.game_over = False
        self.game_won = False

    def add_plant(self, plant_type, x, y, row, col, cost):
        if self.sun_score >= cost:
            if plant_type == "peashooter":
                new_plant = Peashooter(x, y, row=row)
            elif plant_type == "sunflower":
                new_plant = Sunflower(x, y, row=row)
            elif plant_type == "wallnut":
                new_plant = WallNut(x, y, row=row)
            else:
                return False

            new_plant.col = col  
            self.plants.append(new_plant)
            self.sun_score -= cost
            return True
        return False

    def is_cell_occupied(self, row, col):
        for plant in self.plants:
            if getattr(plant, 'row', -1) == row and getattr(plant, 'col', -1) == col:
                return True
        return False

    def run(self):
        while self.running:
            dt = self.clock.tick(FPS) / 1000.0
            self.handle_events()
            self.update(dt)
            self.draw()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_x, mouse_y = event.pos

                # ۱. انتخاب کارت از نوار بالای صفحه
                if mouse_y <= 110:
                    if 140 <= mouse_x <= 220:
                        self.selected_card = self.cards[0]  # Peashooter
                    elif 230 <= mouse_x <= 310:
                        self.selected_card = self.cards[1]  # Sunflower
                    elif 320 <= mouse_x <= 400:
                        self.selected_card = self.cards[2]  # WallNut

                # ۲. کاشت روی زمین
                elif self.selected_card is not None:
                    chosen_col = -1
                    if self.grid_start_x <= mouse_x < self.grid_start_x + (self.cols * self.cell_width):
                        chosen_col = (mouse_x - self.grid_start_x) // self.cell_width

                    chosen_row = -1
                    for index, y_pos in enumerate(self.row_y):
                        if abs(mouse_y - y_pos) < 40:
                            chosen_row = index
                            break

                    if chosen_row != -1 and chosen_col != -1:
                        if not self.is_cell_occupied(chosen_row, chosen_col):
                            center_x = self.grid_start_x + (chosen_col * self.cell_width) + (self.cell_width // 2)
                            spawn_y = self.row_y[chosen_row]

                            plant_name = self.selected_card.plant_name
                            cost = self.selected_card.cost

                            success = self.add_plant(plant_name, center_x, spawn_y, chosen_row, chosen_col, cost)
                            if success:
                                self.selected_card = None  

    def update(self, dt):
        if self.game_over or self.game_won:
            return

        self.wave_manager.update(dt, self.zombies)

        if self.wave_manager.game_won:
            self.game_won = True
            return

        for plant in self.plants:
            plant.update()

            projectile = plant.shoot(self.zombies) if hasattr(plant, 'shoot') else None
            if projectile is not None:
                self.projectiles.append(projectile)

            if hasattr(plant, 'generate_sun'):
                added_sun = plant.generate_sun()
                self.sun_score += added_sun

        for zombie in self.zombies:
            attacking = False

            for plant in self.plants:
                if Collision.zombie_plant(zombie, plant):
                    zombie.attack(plant, dt)
                    attacking = True
                    break

            if not attacking:
                zombie.move()

            if zombie.x <= 50:
                self.game_over = True
                return

        for projectile in self.projectiles:
            if not projectile.active:
                continue

            projectile.move()

            for zombie in self.zombies:
                if zombie.alive and Collision.projectile_zombie(projectile, zombie):
                    break

        self.projectiles = [p for p in self.projectiles if p.active]
        self.zombies = [z for z in self.zombies if z.alive]
        self.plants = [p for p in self.plants if p.alive]

    def draw(self):
        # پس‌زمینه چمن بازی
        self.screen.fill((50, 150, 50))

        # رسم شبکه خانه‌های زمین بازی (Grid)
        for r in range(self.rows):
            for c in range(self.cols):
                cell_x = self.grid_start_x + c * self.cell_width
                cell_y = self.row_y[r] - 40
                pygame.draw.rect(self.screen, (40, 130, 40), (cell_x, cell_y, self.cell_width, 80), 1)

        # رسم گیاهان، زامبی‌ها و تیرها
        for plant in self.plants:
            plant.draw(self.screen)

        for zombie in self.zombies:
            zombie.draw(self.screen)

        for projectile in self.projectiles:
            projectile.draw(self.screen)

        # ------------------- نوار بالایی (HUD Bar) -------------------
        pygame.draw.rect(self.screen, (30, 50, 30), (0, 0, WIDTH, 110))
        pygame.draw.line(self.screen, (100, 100, 100), (0, 110), (WIDTH, 110), 2)

        # متن مقدار خورشید
        sun_text = self.sun_font.render(f"Sun: {self.sun_score}", True, (255, 255, 0))
        self.screen.blit(sun_text, (20, 40))

        # کارت ۱: Peashooter
        p_color = (0, 200, 0) if self.selected_card and self.selected_card.plant_name == "peashooter" else (0, 100, 0)
        pygame.draw.rect(self.screen, p_color, (140, 10, 80, 90), border_radius=6)
        pygame.draw.rect(self.screen, (255, 255, 255), (140, 10, 80, 90), 2, border_radius=6)
        
        p_name = self.card_font.render("Pea", True, (255, 255, 255))
        p_cost = self.card_font.render("100", True, (255, 255, 0))
        self.screen.blit(p_name, (165, 25))
        self.screen.blit(p_cost, (168, 60))

        # کارت ۲: Sunflower
        s_color = (220, 220, 0) if self.selected_card and self.selected_card.plant_name == "sunflower" else (150, 150, 0)
        pygame.draw.rect(self.screen, s_color, (230, 10, 80, 90), border_radius=6)
        pygame.draw.rect(self.screen, (255, 255, 255), (230, 10, 80, 90), 2, border_radius=6)
        
        s_name = self.card_font.render("Sun", True, (0, 0, 0))
        s_cost = self.card_font.render("50", True, (0, 0, 0))
        self.screen.blit(s_name, (258, 25))
        self.screen.blit(s_cost, (262, 60))

        # کارت ۳: WallNut
        w_color = (160, 82, 45) if self.selected_card and self.selected_card.plant_name == "wallnut" else (100, 50, 10)
        pygame.draw.rect(self.screen, w_color, (320, 10, 80, 90), border_radius=6)
        pygame.draw.rect(self.screen, (255, 255, 255), (320, 10, 80, 90), 2, border_radius=6)
        
        w_name = self.card_font.render("Nut", True, (255, 255, 255))
        w_cost = self.card_font.render("50", True, (255, 255, 0))
        self.screen.blit(w_name, (348, 25))
        self.screen.blit(w_cost, (352, 60))

        # -------------------------------------------------------------

        # بنر اعلام موج‌ها
        if self.wave_manager.banner_text != "":
            banner_surface = self.banner_font.render(self.wave_manager.banner_text, True, (255, 255, 0))
            center_y = HEIGHT // 2 if self.wave_manager.phase == "game_start" else 140
            banner_rect = banner_surface.get_rect(center=(WIDTH // 2, center_y))
            self.screen.blit(banner_surface, banner_rect)

        # وضعیت‌های پایان بازی
        if self.game_over:
            text_surface = self.font.render("GAME OVER", True, (200, 0, 0))
            text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            self.screen.blit(text_surface, text_rect)

        elif self.game_won:
            text_surface = self.font.render("YOU WIN!", True, (255, 215, 0))
            text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            self.screen.blit(text_surface, text_rect)

        pygame.display.update()
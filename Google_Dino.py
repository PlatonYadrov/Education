import os
import sys

import pygame
import random


from Sets_images import *

pygame.init()

# Классы объектов


class Dino:
    y_pos = 310
    y_pos_duck = 340
    jump_count = 25
    jump_speed = 8.5

    def __init__(self, direction):
        self.duck_img = images["ducking"]
        self.run_img = images["running"]
        self.jump_img = images["jumping"]
        self.jump_count = self.jump_count
        self.jump_sp = self.jump_speed

        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False

        self.step_index = 0
        self.image = self.run_img[0]

        self.dino_rect = self.image.get_rect()
        if direction == "right":
            self.dino_rect.x = 80
        else:
            self.dino_rect.x = 1020
        self.dino_rect.y = self.y_pos

    def update(self, user_input):
        if self.dino_jump:
            self.jump()
        if self.dino_run:
            self.run()
        if self.dino_duck:
            self.duck()

        if self.step_index >= 10:
            self.step_index = 0

        if (user_input[pygame.K_UP] or user_input[pygame.K_SPACE]) and not self.dino_jump:
            self.dino_duck = False
            self.dino_run = False
            self.dino_jump = True
        elif user_input[pygame.K_DOWN] and not self.dino_jump:
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = False
        elif not (self.dino_jump or user_input[pygame.K_DOWN]):
            self.dino_duck = False
            self.dino_run = True
            self.dino_jump = False

    def duck(self):
        self.image = self.duck_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        if direction == "right":
            self.dino_rect.x = 80
        else:
            self.dino_rect.x = 1020
        self.dino_rect.y = self.y_pos_duck
        self.step_index += 1

    def run(self):
        self.image = self.run_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        if direction == "right":
            self.dino_rect.x = 80
        else:
            self.dino_rect.x = 1020
        self.dino_rect.y = self.y_pos
        self.step_index += 1

    def jump(self):
        self.image = self.jump_img
        if self.dino_jump:
            self.dino_rect.y -= self.jump_sp * 3
            self.jump_sp -= 0.5
        if self.jump_sp < - self.jump_speed:
            self.dino_jump = False
            self.jump_sp = self.jump_speed

    def draw(self, win):
        win.blit(self.image, (self.dino_rect.x, self.dino_rect.y))


class Cloud:
    def __init__(self, direction):
        if direction == "right":
            self.x = win_width + 1
        else:
            self.x = 0
        self.y = random.randint(100, 300)
        self.image = images["cloud"]
        self.width = self.image.get_width()

    def update(self):
        if direction == "right":
            self.x -= game_speed
            if self.x < - self.width:
                self.x = win_width + random.randint(2500, 3000)
        else:
            self.x += +game_speed
            if self.x > self.width + 1200:
                self.x = - win_width

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))


class Obstacle:
    def __init__(self, image, type, direction):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        if direction == "right":
            self.rect.x = win_width
        else:
            self.rect.x = 0

    def update(self):
        if direction == "right":
            self.rect.x -= game_speed
            if self.rect.x < -self.rect.width:
                obstacles.pop()
        else:
            self.rect.x += game_speed
            if self.rect.x > 1200:
                obstacles.pop()

    def draw(self, win):
        win.blit(self.image[self.type], self.rect)


class Small_Cactus(Obstacle):
    def __init__(self, image, direction):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type, direction)
        self.rect.y = 325


class Large_Cactus(Obstacle):
    def __init__(self, image, direction):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type, direction)
        self.rect.y = 300


class Ptero(Obstacle):
    def __init__(self, image, direction):
        self.type = 0
        super().__init__(image, self.type, direction)
        self.rect.y = random.randint(150, 300)
        self.index = 0

    def draw(self, win):
        if self.index > 9:
            self.index = 0
        win.blit(self.image[self.index // 5], self.rect)
        self.index += 1

# Подсчет и ывод счета


def score(flag, font):
    global points, game_speed
    points += 0.5
    if int(points) % 100 == 0:
        game_speed += 0.5

    if flag == 0:
        text = font.render("Points: " + str(int(points)), True, (0, 0, 0))
    else:
        text = font.render("Points: " + str(int(points)), True, (255, 255, 255))
    textRect = text.get_rect()
    textRect.center = (1000, 40)
    win.blit(text, textRect)

# Задний фон (движение и обновление)


def background(direction):
    global x_bg, y_bg
    image_width = images["bg"].get_width()
    win.blit(images["bg"], (x_bg, y_bg))
    if direction == "right":
        win.blit(images["bg"], (image_width + x_bg, y_bg))
        if x_bg <= -image_width:
            win.blit(images["bg"], (image_width + x_bg, y_bg))
            x_bg = 0
        x_bg -= game_speed
    else:
        win.blit(images["bg"], (-image_width + x_bg, y_bg))
        if x_bg >= image_width:
            win.blit(images["bg"], (-image_width + x_bg, y_bg))
            x_bg = 0
        x_bg += game_speed
# Цикл, внутри которого происходит игра


def game():
    global game_speed, x_bg, y_bg, points, obstacles, direction, images, score_and_name_pair, all_id
    sonic_start = 1000
    game_speed = 10
    x_bg = 0
    y_bg = 380
    points = 0
    night_points = random.randint(750, 1000)
    day_points = 0
    run = True

    fps = pygame.time.Clock()
    player = Dino(direction)
    cloud = Cloud(direction)
    font = pygame.font.Font("freesansbold.ttf", 20)
    obstacles = []
    death_count = 0
    flag = 0
    while run:
        if hard == 1:
            if points % 200 == 0 and points > 0:
                if direction == "right":
                    direction = "left"
                    images = revers_images
                    x_bg += 2000
                else:
                    direction = "right"
                    images = normal_images
                    x_bg -= 2000
                player = Dino(direction)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        if points > sonic_start and direction == "right":
            if flag == 0:
                win.fill((0, 255, 0))
            else:
                win.fill((255, 0, 255))
        else:
            if flag == 0:
                win.fill((255, 255, 255))
            else:
                win.fill((0, 0, 0))
        user_input = pygame.key.get_pressed()

        player.draw(win)
        player.update(user_input)

        if points == night_points:
            flag = 1
            day_points = night_points + random.randint(250, 500)

        if points == day_points:
            night_points = day_points + random.randint(250, 500)
            flag = 0

        if points == sonic_start and direction == "right":
            images = sonic_images

            player = Dino(direction)
            game_speed = 20

        if len(obstacles) == 0:
            if random.randint(0, 2) == 0:
                obstacles.append(Small_Cactus(images["small_cactus"], direction))
            elif random.randint(0, 2) == 1:
                obstacles.append(Large_Cactus(images["large_cactus"], direction))
            elif random.randint(0, 2) == 2:
                obstacles.append(Ptero(images["ptero"], direction))

        for obstacle in obstacles:
            obstacle.draw(win)
            obstacle.update()
            if points < sonic_start or points > sonic_start + 10:
                if player.dino_rect.colliderect(obstacle.rect):
                    pygame.time.delay(200)
                    death_count += 1
                    ########### Запись и сортировка пары (очки, имя)
                    if score_and_name_pair[0] == 0:
                        score_and_name_pair[0] = int(points)
                        all_id.append([score_and_name_pair[0], score_and_name_pair[1]])
                    else:
                        score_and_name_pair.append(int(points))
                        score_and_name_pair = list(reversed(score_and_name_pair))
                        all_id.append([score_and_name_pair[0], score_and_name_pair[1]])
                    all_id.sort(reverse=True)
                    ###########
                    menu(death_count)

        background(direction)

        score(flag, font)

        cloud.draw(win)
        cloud.update()

        fps.tick(60)
        pygame.display.update()
# Функция, отвечающая за запись в файл


def push_txt():
    global all_id
    try:
        file = open("records.txt", "x")
    except:
        file = open("records.txt", "a")
    for id in all_id:
        file.write(str(id[0]) + "\n")
        file.write(str(id[1]) + "\n")

    file = open("records.txt", "r")
    n = 0
    all_id = []
    for row in file:
        n += 1
        if n == 2:
            all_id.append([int(previous_row), row.strip("\n")])
            n = 0
        else:
            previous_row = row
    all_id = list(reversed(sorted(all_id)))
    return all_id
# Ввод имени


def input_name():
    global score_and_name_pair
    font = pygame.font.Font("freesansbold.ttf", 30)
    user_text = ""
    input_rect = pygame.Rect(win_width // 2 - 50, win_height // 2, 140, 30)
    color_active = (255, 0, 255)
    color_passive = (0, 255, 0)
    # color = color_passive
    active = False
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                push_txt()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False

            if event.type == pygame.KEYDOWN:
                if active == True:
                    if event.key == pygame.K_RETURN:
                        run = False
                        if user_text != "":
                            score_and_name_pair = []
                            score_and_name_pair.append(user_text)
                        else:
                            score_and_name_pair[0] = 0
                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    else:
                        user_text += event.unicode
                else:
                    if event.key == pygame.K_RETURN:
                        score_and_name_pair[0] = 0
                        run = False

        win.fill((255, 255, 255))

        if active:
            color = color_active
        else:
            color = color_passive

        pygame.draw.rect(win, color, input_rect, 2)

        text_surface = font.render(user_text, True, (0, 0, 0))
        win.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))

        input_rect.w = max(100, text_surface.get_width() + 10)

        text_right = font.render("Enter your name or press enter to skip input", True, (0, 0, 0))
        text_rect_right = text_right.get_rect()
        text_rect_right.center = (win_width // 2 - 20, win_height // 2 - 20)
        win.blit(text_right, text_rect_right)

        pygame.display.flip()
# Таблица рекордов


def records_table():
    run = True
    while run:
        number = 0
        win.fill((255, 255, 255))
        font = pygame.font.Font("freesansbold.ttf", 30)
        text = font.render("Records table", True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (win_width // 2, 100)
        win.blit(text, text_rect)
        for score in all_id:
            number += 1
            text_score = font.render(f"{score[1]} {score[0]}", True, (0, 0, 0))
            text_rect_score = text_score.get_rect()
            text_rect_score.center = (win_width // 2, 100 + 50 * number)
            win.blit(text_score, text_rect_score)
            if number == 5:
                break
        additional_text = font.render("If you want to know more about records check the file records.txt", True, (0, 0, 0))
        additional_text_rect = additional_text.get_rect()
        additional_text_rect.center = (win_width // 2, 100 + 50 * (5 + 1))
        win.blit(additional_text, additional_text_rect)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                push_txt()
                sys.exit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                menu(death_count=0)

# Меню: самая главная функция можно считать, что это main. В ней изначально происходит вызов меню, из которого происходит вызов функции game


def menu(death_count):
    global points, images, direction, hard, all_id
    run = True
    if death_count == 0:
        push_txt()
        os.remove("records.txt")
    while run:
        win.fill((255, 255, 255))
        font = pygame.font.Font("freesansbold.ttf", 30)

        text_right = font.render("Press the r key to start moving right", True, (0, 0, 0))
        text_left = font.render("Press the l key to start moving left", True, (0, 0, 0))
        text_hard = font.render("If you want to play seriously press h", True, (0, 0, 0))
        if death_count > 0:
            score = font.render("Your Score: " + str(int(points)), True, (0, 255, 0))
            score_rect = score.get_rect()
            score_rect.center = (win_width // 2, 500)
            win.blit(score, score_rect)

        text_rect_right = text_right.get_rect()
        text_rect_right.center = (win_width // 2 - 100, 100)
        win.blit(text_right, text_rect_right)
        win.blit(normal_images["running"][0], (win_width // 2 + 180, 50))

        text_rect_left = text_left.get_rect()
        text_rect_left.center = (win_width // 2 - 100, 250)
        win.blit(text_left, text_rect_left)
        win.blit(revers_images["running"][0], (win_width // 2 + 180, 200))

        text_rect_hard = text_hard.get_rect()
        text_rect_hard.center = (win_width // 2 - 100, 400)
        win.blit(text_hard, text_rect_hard)
        win.blit(revers_images["running"][0], (win_width // 2 + 180, 350))
        win.blit(normal_images["running"][0], (win_width // 2 + 180, 350))

        font = pygame.font.Font("freesansbold.ttf", 20)
        text_records = font.render("Table records press esc", True, (255, 0, 0))
        text_rect_records = text_records.get_rect()
        text_rect_records = (40, 50)
        win.blit(text_records, text_rect_records)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                push_txt()
                sys.exit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                images = normal_images
                direction = "right"
                hard = 0
                input_name()
                game()
            elif keys[pygame.K_l]:
                images = revers_images
                direction = "left"
                hard = 0
                input_name()
                game()
            elif keys[pygame.K_h]:
                images = normal_images
                direction = "right"
                hard = 1
                input_name()
                game()
            elif keys[pygame.K_ESCAPE]:
                records_table()


if __name__ == '__main__':
    menu(death_count=0)

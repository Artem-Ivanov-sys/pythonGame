import tkinter
import time
import random


def main():
    moving = 'stop'
    score = 0
    over = False

    def game_over():
        nonlocal over
        over = True
        main_canvas['bg'] = '#FFA8A8'
        main_canvas.itemconfig(player.player, fill='#B6B6B6', outline='black')
        main_canvas.itemconfig(score_label, fill='white')
        main_canvas.itemconfig(coords_label, fill='white')
        main_canvas.itemconfig(stage, fill='white')
        main_screen.update()

    class Player:

        def __init__(self):

            self.x = main_screen.winfo_screenwidth()//2
            self.y = main_screen.winfo_screenheight()//2
            self.weight = 20

            self.create()

        def create(self):

            self.player = main_canvas.create_rectangle(self.x-self.weight,
                                                       self.y-self.weight, self.x+self.weight, self.y+self.weight,
                                                       outline='#8E00F8', fill='#A382F9', width=5)

        def move(self, side):

            if side == 'right':
                main_canvas.move(self.player, 10, 0)
                self.x += 10
            elif side == 'left':
                main_canvas.move(self.player, -10, 0)
                self.x -= 10
            elif side == 'up':
                main_canvas.move(self.player, 0, -10)
                self.y -= 10
            elif side == 'down':
                main_canvas.move(self.player, 0, 10)
                self.y += 10

            if self.x < self.weight:
                main_canvas.move(self.player, -self.x+self.weight, 0)
                self.x = self.weight
            if self.y < self.weight:
                main_canvas.move(self.player, 0, -self.y+self.weight)
                self.y = self.weight
            if self.x > main_screen.winfo_screenwidth() - self.weight:
                main_canvas.move(self.player, main_screen.winfo_screenwidth()-self.weight-self.x, 0)
                self.x = main_screen.winfo_screenwidth() - self.weight
            if self.y > main_screen.winfo_screenheight() - 2*self.weight:
                main_canvas.move(self.player, 0, main_screen.winfo_screenheight()-2*self.weight-self.y)
                self.y = main_screen.winfo_screenheight() - 2*self.weight

            main_screen.update()

        def jump(self, side):

            if side == 'right':
                main_canvas.move(self.player, 100, 0)
                self.x += 100
            elif side == 'left':
                main_canvas.move(self.player, -100, 0)
                self.x -= 100
            elif side == 'up':
                main_canvas.move(self.player, 0, -100)
                self.y -= 100
            elif side == 'down':
                main_canvas.move(self.player, 0, 100)
                self.y += 100

            if self.x < self.weight:
                main_canvas.move(self.player, -self.x+self.weight, 0)
                self.x = self.weight
            if self.y < self.weight:
                main_canvas.move(self.player, 0, -self.y+self.weight)
                self.y = self.weight
            if self.x > main_screen.winfo_screenwidth() - self.weight:
                main_canvas.move(self.player, main_screen.winfo_screenwidth()-self.weight-self.x, 0)
                self.x = main_screen.winfo_screenwidth() - self.weight
            if self.y > main_screen.winfo_screenheight() - 2*self.weight:
                main_canvas.move(self.player, 0, main_screen.winfo_screenheight()-2*self.weight-self.y)
                self.y = main_screen.winfo_screenheight() - 2*self.weight

            main_screen.update()

    class EnemyClass1x:

        def __init__(self):

            self.x = random.randint(5, main_screen.winfo_screenwidth()-5)
            self.sec = 0
            self.create()

        def create(self):

            self.enemy = main_canvas.create_line(self.x, -10, self.x,
                                                 main_screen.winfo_screenheight()+10, fill='#545454', width=4)

        def start(self):

            self.sec += 1
            if self.sec >= 10:
                self.attack()
            if self.sec == 30:
                nonlocal score
                score += 5
                main_canvas.itemconfig(score_label, text='Score: {0}'.format(score))
                main_canvas.delete(self.enemy)
                enemies.remove(self)

        def attack(self):

            main_canvas.itemconfig(self.enemy, fill='#252525', width=8)
            if player.x-20 < self.x < player.x+20:
                game_over()

    class EnemyClass1y():

        def __init__(self):

            self.y = random.randint(5, main_screen.winfo_screenheight()-5)
            self.sec = 0
            self.create()

        def create(self):

            self.enemy = main_canvas.create_line(-10, self.y,
                                                 main_screen.winfo_screenwidth()+10, self.y, fill='#545454', width=4)

        def start(self):

            self.sec += 1
            if self.sec >= 10:
                self.attack()
            if self.sec == 30:
                nonlocal score
                score += 5
                main_canvas.itemconfig(score_label, text='Score: {0}'.format(score))
                main_canvas.delete(self.enemy)
                enemies.remove(self)

        def attack(self):

            main_canvas.itemconfig(self.enemy, fill='#252525', width=8)
            if player.y-20 < self.y < player.y+20:
                game_over()

    class EnemyClass2x:

        def __init__(self):

            self.x = random.choice([10, main_screen.winfo_screenwidth()-10])
            self.side = 'right' if self.x == 10 else 'left'
            self.sec = 0
            self.create()

        def create(self):

            self.enemy = main_canvas.create_line(self.x, -10,
                                                 self.x, main_screen.winfo_screenheight()+10, fill='#545454', width=4)

        def start(self):

            self.sec += 1
            if self.sec >= 10:
                self.attack()
            if (self.x > main_screen.winfo_screenwidth() - 5 and self.side == 'right') \
                    or (self.x < 5 and self.side == 'left'):
                nonlocal score
                score += 10
                main_canvas.itemconfig(score_label, text='Score: {0}'.format(score))
                main_canvas.delete(self.enemy)
                enemies.remove(self)

        def attack(self):

            main_canvas.delete(self.enemy)
            self.x += 5 if self.side == 'right' else -5
            self.create()
            main_canvas.itemconfig(self.enemy, fill='#252525', width=8)
            if player.x-20 < self.x < player.x+20:
                game_over()

    class EnemyClass2y:

        def __init__(self):

            self.y = random.choice([30, main_screen.winfo_screenheight()-10])
            self.side = 'down' if self.y == 30 else 'up'
            self.sec = 0
            self.create()

        def create(self):

            self.enemy = main_canvas.create_line(-10, self.y,
                                                 main_screen.winfo_screenwidth()+10, self.y, fill='#545454', width=4)

        def start(self):

            self.sec += 1
            if self.sec >= 10:
                self.attack()
            if (self.y > main_screen.winfo_screenheight() - 5 and self.side == 'down') \
                    or (self.y < 5 and self.side == 'up'):
                nonlocal score
                score += 10
                main_canvas.itemconfig(score_label, text='Score: {0}'.format(score))
                main_canvas.delete(self.enemy)
                enemies.remove(self)

        def attack(self):

            main_canvas.delete(self.enemy)
            self.y += 5 if self.side == 'down' else -5
            self.create()
            main_canvas.itemconfig(self.enemy, fill='#252525', width=8)
            if player.y-20 < self.y < player.y+20:
                game_over()

    def run(side):
        nonlocal moving
        if side.keysym.lower() == 'right':
            moving = 'right'
        elif side.keysym.lower() == 'left':
            moving = 'left'
        elif side.keysym.lower() == 'up':
            moving = 'up'
        elif side.keysym.lower() == 'down':
            moving = 'down'

    def stop(side):
        nonlocal moving
        if side.keysym.lower() != 'space':
            moving = 'stop'

    def run_game1x():
        nonlocal enemies
        enemies.append(EnemyClass1x())

    def run_game1y():
        nonlocal enemies
        enemies.append(EnemyClass1y())

    def run_destroyer():
        nonlocal enemies
        if random.randint(0, 1) == 0:
            enemies.append(EnemyClass2x())
        else:
            enemies.append(EnemyClass2y())

    main_screen = tkinter.Tk()
    main_screen.title('Game')
    main_screen.state('zoomed')
    main_screen.resizable(width=False, height=False)

    main_canvas = tkinter.Canvas(bg='#BBFEFF')
    main_canvas.place(x=-5, y=-5, width=2010, height=1510)

    player = Player()
    main_screen.bind('<KeyPress>', lambda event: run(event))
    main_screen.bind('<space>', lambda event: player.jump(moving))
    main_screen.bind('<KeyRelease>', lambda event: stop(event))

    enemies = []

    score_label = main_canvas.create_text(90, 15, text='Score: {0}'.format(score),
                                          font=('Arial bold', '20'))
    coords_label = main_canvas.create_text(main_screen.winfo_screenwidth()-100, 15,
                                           text='X: {0}; Y: {1}'.format(player.x, player.y), font=('Arial bold', '20'))
    step = 0

    stage = main_canvas.create_text(60, 40, text='Stage 1', font=('Arial bold', '20'))
    while score < 300 and not over:
        step += 1
        player.move(moving)
        if step % 5 == 0:
            run_game1x()
        elif step % 7 == 0:
            run_game1y()
        for enemy in enemies:
            enemy.start()

        main_canvas.itemconfig(coords_label, text='X: {0}; Y: {1}'.format(player.x, player.y))

        main_screen.update()
        time.sleep(.1)

    main_canvas.itemconfig(stage, text='Stage 2')
    while score < 1000 and not over:
        step += 1
        player.move(moving)
        if step % 6 == 0:
            run_game1x()
        elif step % 8 == 0:
            run_game1y()
        elif step % 10 == 0 and random.randint(0, 5) == 3:
            run_destroyer()
        for enemy in enemies:
            enemy.start()

        main_canvas.itemconfig(coords_label, text='X: {0}; Y: {1}'.format(player.x, player.y))

        main_screen.update()
        time.sleep(.1)

    main_canvas.itemconfig(stage, text='Stage 3')
    while score < 1500 and not over:
        step += 1
        player.move(moving)
        if step % 25 == 0:
            run_destroyer()
        for enemy in enemies:
            enemy.start()

        main_canvas.itemconfig(coords_label, text='X: {0}; Y: {1}'.format(player.x, player.y))

        main_screen.update()
        time.sleep(.1)

    main_screen.mainloop()


if __name__ == '__main__':
    main()

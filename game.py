from pygame import *

window = display.set_mode((720,575))
display.set_caption('WW3')
roles={
    'red': {
        'engineer': 'red_engineer.png',
        'tank': 'red_tank.png',
        'infantry': 'red_infantry.png',
        'turret': 'red_turret.png',
        'plane': 'red_plane.png',
    },
    'blue': {
        'engineer': 'blue_engineer.png',
        'tank': 'blue_tank.png',
        'infantry': 'blue_infantry.png',
        'turret': 'blue_turret.png',
        'plane': 'blue_plane.png',
}
}
class Cube(sprite.Sprite):
    def __init__(self, role, color, cube_x, cube_y):
        super().__init__()
        self.team = None
        self.role = role
        self.color = color
        self.width = 35
        self.height = 35
        self.image = Surface((self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = cube_x
        self.rect.y = cube_y
    def draw_cube(self):
        self.image.fill(self.color)
        if self.role != None and self.team != None:
            self.image = transform.scale(image.load(roles[self.team][self.role]),(35, 35))
        window.blit(self.image, (self.rect.x, self.rect.y))
    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)

class Unit_earth(sprite.Sprite):
    def __init__(self, player_image, power, health, speed, width, height):
        self.image = transform.scale(image.load(player_image), (width, height))
        self.power = power
        self.health = health
        self.speed = speed

class Unit_sky(sprite.Sprite):
    def __init__(self, player_image, power, health, speed, width, height):
        self.image = transform.scale(image.load(player_image), (width, height))
        self.power = power
        self.health = health
        self.speed = speed

earth = []
for i in range(16):
    temp = []
    for g in range(8):
        earth_cube = Cube('earth', (178,210,135), 36*g, 36*i)
        temp.append(earth_cube)
    earth.append(temp)
print(earth)
sky = []
for r in range(16):
    temp2 = []
    for s in range(8):
        sky_cube = Cube('sky', (188,195,228), 36 * s + 288, 36 * r)
        temp2.append(sky_cube)
    sky.append(temp2)
white = []
for b in range(16):
    temp3 = []
    for v in range(4):
        white_cube = Cube('white_cube', (255,255,255), 36 * v + 576, 36 * b)
        temp3.append(white_cube)
    white.append((temp3))
print(white)
print(sky)
sky[0][3].color = (178,95,91)
sky[0][4].color = (178,95,91)
sky[15][3].color = (94,117,189)
sky[15][4].color = (94,117,189)

earth[0][3].color = (178,95,91)
earth[0][4].color = (178,95,91)
earth[15][3].color = (94,117,189)
earth[15][4].color = (94,117,189)

white[0][1].team = 'blue'
white[0][1].role = 'turret'
white[0][3].team = 'red'
white[0][3].role = 'turret'

white[2][1].team = 'blue'
white[2][1].role = 'tank'
white[2][3].team = 'red'
white[2][3].role = 'tank'

white[4][1].team = 'blue'
white[4][1].role = 'infantry'
white[4][3].team = 'red'
white[4][3].role = 'infantry'

white[6][1].team = 'blue'
white[6][1].role = 'engineer'
white[6][3].team = 'red'
white[6][3].role = 'engineer'

white[8][1].team = 'blue'
white[8][1].role = 'plane'
white[8][3].team = 'red'
white[8][3].role = 'plane'


#green = (178,210,135)
#red = (178,95,91)
#blue = (94,117,189)
#light_blue = (188,195,228)

red_turret = Unit_earth('red_turret.png', 1, 2, 0, 1, 1)
red_tank = Unit_earth('red_tank.png', 2, 2, 1, 1, 1)
red_infantry = Unit_earth('red_infantry.png', 1, 1, 2, 1, 1)
red_engineer = Unit_earth('red_turret.png', 0, 1, 2, 1, 1)
red_plane = Unit_sky('red_turret.png', 1, 2, 1, 1, 1)

blue_turret = Unit_earth('blue_turret.png', 1, 2, 0, 1, 1)
blue_tank = Unit_earth('blue_tank.png', 2, 2, 1, 1, 1)
blue_infantry = Unit_earth('blue_infantry.png', 1, 1, 2, 1, 1)
blue_engineer = Unit_earth('blue_turret.png', 0, 1, 2, 1, 1)
blue_plane = Unit_sky('blue_turret.png',1,  1, 2, 1, 1)

move_r = 0
move_p = 0
#https://pastebin.com/0bSzYLqg
current_role = ''
current_team = ''
current_action = 'blue_selecting_unit'
FPS = 60
clock = time.Clock()
finish = False
game = True

while game:
    if finish != True:
        for raw in white:
            for white_cube in raw:
                white_cube.draw_cube()
        for raw in earth:
            for earth_cube in raw:
                earth_cube.draw_cube()
        for raw in sky:
            for sky_cube in raw:
                sky_cube.draw_cube()
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == MOUSEBUTTONDOWN and e.button == 1:
            x, y = e.pos
            if current_action == 'blue_selecting_unit':
                for i in range(16):
                    for g in range(4):
                        if white[i][g].collidepoint(x, y) and current_role != 'turret':
                            current_role = white[i][g].role
                            current_team = white[i][g].team
                            print(current_role)
                            print(current_team)
                            current_action = 'blue_init_unit'
            if current_action == 'blue_init_unit':
                print('fadsdfasdfasafdsafsd')
                for f in range(14, 16):
                    for s in range(8):
                        if earth[f][s].collidepoint(x, y) and current_role != 'plane' and current_role != 'turret' and earth[f][s] == 'blue':
                            earth[f][s].role = current_role
                            earth[f][s].team = current_team
                            current_action = 'blue_select_move_unit'
                for a in range(14, 16):
                    for c in range(8):
                        if sky[a][c].collidepoint(x, y) and current_role == 'plane' and current_role != 'turret'  and sky[a][c] == 'blue':
                            sky[a][c].role = current_role
                            sky[a][c].team = current_team
                            current_action = 'blue_select_move_unit'

            if current_action == 'blue_select_move_unit':
                for z in range(0, 16):
                    for b in range(8):
                        if earth[z][b].collidepoint(x, y):
                            move_r = z
                            move_p = b
                            current_action = 'blue_move_unit'
                for z in range(0, 16):
                    for b in range(8):
                        if sky[z][b].collidepoint(x, y):
                            move_r = z
                            move_p = b
                            current_action = 'blue_move_unit'
                            print(current_action)
            if current_action == 'blue_move_unit':
                for z in range(-1, 2):
                    for b in range(-1, 2):
                        if move_r + z > -1 and move_r + z < 16 and move_p + b > -1 and move_p + b < 8 and earth[move_r + z][move_p + b].collidepoint(x, y) and (z != 0 or b != 0):
                            earth[move_r + z][move_p + b].role = earth[move_r][move_p].role
                            earth[move_r + z][move_p + b].team = earth[move_r][move_p].team
                            earth[move_r][move_p].role = None
                            earth[move_r][move_p].team = None
                            current_action = 'red_selecting_unit'


            if current_action == 'blue_move_unit':
                for z in range(-1, 2):
                    for b in range(-1, 2):
                        if move_r + z > -1 and move_r + z < 16 and move_p + b > -1 and move_p + b < 8 and sky[move_r + z][move_p + b].collidepoint(x, y) and (z != 0 or b != 0):
                            sky[move_r + z][move_p + b].role = sky[move_r][move_p].role
                            sky[move_r + z][move_p + b].team = sky[move_r][move_p].team
                            sky[move_r][move_p].role = None
                            sky[move_r][move_p].team = None
                            current_action = 'red_selecting_unit'
                            if sky[move_r + z][move_p + b].role != 'plane':
                                for i in range(0, 16):
                                    for s in range(8):
                                        if sky[i][s].role == 'plane' and sky[i][s].team == 'blue':
                                            sky[i][s].role = None
                                            sky[i][s].team = None


            if current_action == 'red_selecting_unit':
                for i in range(16):
                    for g in range(4):
                        if white[i][g].collidepoint(x, y) and current_role != 'turret':
                            current_role = white[i][g].role
                            current_team = white[i][g].team
                            print(current_role)
                            print(current_team)
                            current_action = 'red_init_unit'
            if current_action == 'red_init_unit':

                for t in range(0, 2):
                    for p in range(8):
                        if earth[t][p].collidepoint(x, y) and current_role != 'plane' and current_role != 'turret'  and earth[t][p] == 'red':
                            earth[t][p].role = current_role
                            earth[t][p].team = current_team
                            current_action = 'red_select_move_unit'
                for z in range(0, 2):
                    for b in range(8):
                        if sky[z][b].collidepoint(x, y) and current_role == 'plane' and current_role != 'turret'  and sky[z][b] == 'red':
                            sky[z][b].role = current_role
                            sky[z][b].team = current_team
                            current_action = 'red_select_move_unit'
            if current_action == 'red_select_move_unit':
                for z in range(0, 16):
                    for b in range(8):
                        if earth[z][b].collidepoint(x, y):
                            move_r = z
                            move_p = b
                            current_action = 'red_move_unit'
                for z in range(0, 16):
                    for b in range(8):
                        if sky[z][b].collidepoint(x, y):
                            move_r = z
                            move_p = b
                            current_action = 'red_move_unit'
            if current_action == 'red_move_unit':
                for z in range(-1, 2):
                    for b in range(-1, 2):
                        if move_r + z > -1 and move_r + z < 16 and move_p + b > -1 and move_p + b < 8 and earth[move_r + z][move_p + b].collidepoint(x, y) and (z != 0 or b != 0):
                            earth[move_r + z][move_p + b].role = earth[move_r][move_p].role
                            earth[move_r + z][move_p + b].team = earth[move_r][move_p].team
                            earth[move_r][move_p].role = None
                            earth[move_r][move_p].team = None
                            current_action = 'blue_selecting_unit'
            if current_action == 'red_move_unit':
                for z in range(-1, 2):
                    for b in range(-1, 2):
                        if move_r + z > -1 and move_r + z < 16 and move_p + b > -1 and move_p + b < 8 and sky[move_r + z][move_p + b].collidepoint(x, y) and (z != 0 or b != 0):
                            sky[move_r + z][move_p + b].role = sky[move_r][move_p].role
                            sky[move_r + z][move_p + b].team = sky[move_r][move_p].team
                            sky[move_r][move_p].role = None
                            sky[move_r][move_p].team = None
                            current_action = 'blue_selecting_unit'




    clock.tick(FPS)
    display.update()
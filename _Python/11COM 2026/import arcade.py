import arcade
import random
                                                                                                        ##NEW##

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_SPEED = 5

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "My Awesome Game")
        self.background_color = arcade.color.AMAZON
        self.setup()
        # Put setup here

    def setup(self):
        self.player = arcade.Sprite(":resources:/images/animated_characters/zombie/zombie_idle.png")
        self.player.center_x = SCREEN_WIDTH / 2
        self.player.center_y = SCREEN_HEIGHT / 2

        self.coin_list = arcade.SpriteList()
        for n in range(50):
            coin = arcade.Sprite(":resources:/images/items/coinGold.png", 0.5)
            coin.center_x = random.randint(0, SCREEN_WIDTH)
            coin.center_y = random.randint(0, SCREEN_HEIGHT)
            coin.change_x = random.randint(-5, 5)
            coin.change_y = random.randint(-5, 5)
            self.coin_list.append(coin)

        self.bomb_list = arcade.SpriteList()
        for n in range(3):
            bomb = arcade.Sprite(":resources:/images/tiles/bomb.png", 0.5)
            bomb.center_x = random.randint(0, SCREEN_WIDTH)
            bomb.center_y = random.randint(0, SCREEN_HEIGHT)
            bomb.change_x = random.randint(-5, 5)
            bomb.change_y = random.randint(-5, 5)
            bomb.angle = random.randint(0, 360)
            bomb.change_angle = 5
            bomb.scale = random.randint(1, 10) / 10
            bomb.change_scale = 0.01
            self.bomb_list.append(bomb)


        self.wall_list = arcade.SpriteList()
        for n in range(10):
            wall = arcade.Sprite(":resources:/images/tiles/grassMid.png", 0.5)
            wall.center_y = 50
            wall.center_x = n * 100
            self.wall_list.append(wall)

        self.physice_engine = arcade.PhysicsEnginePlatformer(self.player, self.wall_list, 1)

        self.score = 0
        self.game_over = False
        self.total_time = 0

        self.jump_texture = arcade.load_texture(":resources:/images/animated_characters/zombie/zombie_jump.png")
        self.idle_texture = arcade.load_texture(":resources:/images/animated_characters/zombie/zombie_idle.png")

        self.current_texture = 0
        self.walk_texture = []
        for n in range(8):
            texture = arcade.load_texture(f":resources:/images/animated_characters/zombie/zombie_walk{n}.png")
            self.walk_texture.append(texture)

    def on_draw(self):
        self.clear()
        self.wall_list.draw()
        self.bomb_list.draw()
        self.coin_list.draw()
        arcade.draw_sprite(self.player)
        arcade.draw_text(f"Time: {round(self.total_time, 2)}s", SCREEN_WIDTH-200, SCREEN_HEIGHT-40, font_size=30)
        arcade.draw_line(0, 0, SCREEN_WIDTH * (1-self.total_time / 10), 0, arcade.color.LIME, 50)
        arcade.draw_text(f"Score: {self.score}", 10, SCREEN_HEIGHT-50, font_size=30)

        if self.game_over == True:
            arcade.draw_text("Game over",
                             SCREEN_WIDTH/2, SCREEN_HEIGHT/2, font_size=50, anchor_x="center")
            arcade.draw_text("press R to restart", 
                             SCREEN_WIDTH/2, SCREEN_HEIGHT/2-80, font_size=30, anchor_x="center")

    def on_update(self, delta_time):
        if self.game_over:
            return
        
        self.current_texture += 1
        
        if self.physice_engine.can_jump():
            if self.player.change_x == 0:
                self.player.texture = self.idle_texture
            else:
                self.current_texture += 0.5
                self.player.texture = self.walk_texture[ int(self.current_texture) % 8 ]
        else:
            self.player.texture = self.jump_texture

        
        self.total_time += delta_time
        if self.total_time >= 10:
            self.game_over = True

        self.physice_engine.update()
        self.coin_list.update()
        self.bomb_list.update()

        hit_list = arcade.check_for_collision_with_list(self.player, self.coin_list)
        for coin in hit_list:
            self.score += 1
            coin.kill()

        if len(self.coin_list) == 0:
            self.game.over = True

        hit_list = arcade.check_for_collision_with_list(self.player, self.bomb_list)
        for bomb in hit_list:
            self.game_over = True

        if self.player.right > SCREEN_WIDTH:
            self.player.right = SCREEN_WIDTH
        if self.player.left < 0:
            self.player.left = 0
        if self.player.top > SCREEN_HEIGHT:
            self.player.top = SCREEN_HEIGHT
        if self.player.bottom < 0:
            self.player.bottom = 0

        for coin in self.coin_list:
            if coin.right > SCREEN_WIDTH:
                coin.right = SCREEN_WIDTH
                coin.change_x *= -1
            if coin.left <0:
                coin.left = 0
                coin.change_x *= -1
            if coin.top > SCREEN_HEIGHT:
                coin.top = SCREEN_HEIGHT
                coin.change_y *= -1
            if coin.bottom <0:
                coin.bottom = 0
                coin.change_y *= -1
            
        for bomb in self.bomb_list:
            if bomb.right > SCREEN_WIDTH:
                bomb.right = SCREEN_WIDTH
                bomb.change_x *= -1
            if bomb.left <0:
                bomb.left = 0
                bomb.change_x *= -1
            if bomb.top > SCREEN_HEIGHT:
                bomb.top = SCREEN_HEIGHT
                bomb.change_y *= -1
            if bomb.bottom <0:
                bomb.bottom = 0
                bomb.change_y *= -1

        for bomb in self.bomb_list:
            bomb.scale_x += bomb.change_scale
            bomb.scale_y += bomb.change_scale
            if bomb.scale_x > 1 or bomb.scale_x < 0.1:
                bomb.change_scale *= -1

            if bomb.scale_x > 0.9:
                bomb.color = arcade.color.ORANGE
            else:
                bomb.color = arcade.color.WHITE



    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.player.change_x = -PLAYER_SPEED
        if key == arcade.key.RIGHT:
            self.player.change_x = PLAYER_SPEED
        if key == arcade.key.UP:
            self.player.change_y = PLAYER_SPEED
        if key == arcade.key.DOWN:
            self.player.change_y = -PLAYER_SPEED
        if key == arcade.key.SPACE and self.physice_engine.can_jump():
            self.player.change_y = 20

        if key == arcade.key.R and self.game_over:
            self.setup()

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player.change_x = 0
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player.change_y = 0


    

MyGame()
arcade.run()
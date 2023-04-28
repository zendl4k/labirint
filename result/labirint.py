# Разработай свою игру в этом файле!
from pygame import *
win_w = 700
win_h = 500
back = (250, 50 ,180)
window = display.set_mode((win_w, win_h))
display.set_caption("ZXC")
speed = 2
window.fill(back)
run = True
finish = False


bullets = sprite.Group()



class GameSprite(sprite.Sprite):
    def __init__(self, picture, w , h, x, y):
        super().__init__()
        self.image = transform.scale(image.load(picture),(w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image ,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, picture, w, h, x, y,  x_speed, y_speed):
        self.image = transform.scale(image.load(picture),(w,h))
        self.rect = self.image.get_rect()
        self.x_speed = x_speed
        self.y_speed = y_speed
    def update(self):
        self.rect.x += self.x_speed
        platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.x_speed > 0:
            for p in platforms_touched:
                self.rect.right = min(self.rect.right, p.rect.left)
        elif self.x_speed < 0:
            for p in platforms_touched:
                self.rect.left = max(self.rect.left, p.rect.right)
        self.rect.y += self.y_speed
        if self.y_speed > 0:
            for p in platforms_touched:
                self.rect.bottom = min(self.rect.bottom, p.rect.top)
        elif self.y_speed < 0:
            for p in platforms_touched:
                self.rect.top = max(self.rect.top, p.rect.bottom)
    def fire(self):
        bullet = Bullet('bullet.png',25 , 35,self.rect.right ,self.rect.centery , 15)
        bullets.add(bullet)

class Enemy(GameSprite):
    side = "left"
    def __init__(self, picture, w, h, x, y, speed):
        GameSprite.__init__(self, picture, w, h, x, y)
        self.speed = speed
    def update(self):
        
        if self.rect.y == 150: 
            self.side = "DOWN"
        if self.rect.y == 350:
            self.side = "UP"
        if self.side == "UP":
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed

class Bullet(GameSprite):
    def __init__(self, picture, w, h, x, y, speed):
        GameSprite.__init__(self, picture, w, h, x, y)
        self.speed = speed
    def update(self):
        self.rect.x += self.speed
        if self.rect.x > win_w + 10:
            self.kill()


  

    









background = transform.scale(image.load('city.png'),(700,500))
wall = GameSprite('wall.png', 80, 400, 400 ,300)
hero = Player('hero.png', 100, 100, 200, 400, 0, 0)
ball = GameSprite('ball.png', 100, 100, 500, 400)
end = transform.scale(image.load('finish.jpg'),(700,500))
bomb = Enemy('bomb.png', 80, 80, 300, 150, 5)
end2 = transform.scale(image.load('end.jpg'),(700,500)) 

monsters = sprite.Group()
barriers = sprite.Group()
monsters.add(bomb)
barriers.add(wall)

while run:
    
        


    


    time.delay(50)
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            
            if e.key == K_LEFT:
               hero.x_speed = -5
            elif e.key == K_RIGHT:
               hero.x_speed = 5
            elif e.key == K_UP:
               hero.y_speed = -5
            elif e.key == K_DOWN:
               hero.y_speed = 5
            elif e.key == K_SPACE:
                hero.fire()
        elif e.type == KEYUP:
            if e.key == K_LEFT:
               hero.x_speed = 0
            elif e.key == K_RIGHT:
               hero.x_speed = 0
            elif e.key == K_UP:
               hero.y_speed = 0
            elif e.key == K_DOWN:
               hero.y_speed = 0

    if not finish:
        
        window.blit(background,(0,0))
        hero.reset()
        ball.reset()
        
        barriers.draw(window)
        bullets.draw(window)
        


        sprite.groupcollide(bullets, barriers, True, False)
        sprite.groupcollide(bullets, monsters, True, True)
        monsters.update()
        monsters.draw(window)
        

            
            
                

        
                

        
        if sprite.collide_rect(hero, ball):
            finish = True
            window.blit(end,(0, 0))
                
        if sprite.collide_rect(hero, bomb):
            finish = True
            window.blit(end2, (0, 0))
                
                
            
            
            
        bullets.update()
        bomb.update()   
        hero.update()
        display.update()

   
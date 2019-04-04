import pygame
h = 500 
w = 700

pl = 0
pl2 = 0

blue = (0,0,255)
white = (255,255,255)
xs = 0
ys = 0
pygame.init()
dis = pygame.display.set_mode([w,h])
img = pygame.image.load("bal.png")
timg = pygame.image.load("ta1.png")
pygame.display.set_caption("python pong game")

c = pygame.time.Clock() 
def ta1(x1,y2):
  dis.blit(timg,(x1,y2))
x1 = float(20)
y2 = float(200)

def ta2(x4,y4):
  dis.blit(timg,(x4,y4))
x4 = float(660)
y4 = float(200)

def bal(x,y):
  dis.blit(img,(x,y))
 
x = (w*0.45)
y = (h*0.3) 
fl = True
print "pehtis 1 (",pl,":",pl2,") pehtis 2"
while fl == True:
   for ev in pygame.event.get():
       if ev.type == pygame.QUIT:
          fl = False
       if ev.type == pygame.KEYDOWN: 
         if ev.key == pygame.K_SPACE:
           xs = -3
           ys = -3
         #table 1 keys
         if ev.key == pygame.K_w:
           y2 += -30
         if ev.key == pygame.K_s:
           y2 += 30
        #table 2 keys
         if ev.key == pygame.K_UP:
           y4 += -30
         if ev.key == pygame.K_DOWN:
           y4 += 30
   #table 1 wall stop
   if y2 <= -30:
       y2 = y2+30
   if y2 >= (h-60):
       y2 = y2-30
   #table 2 wall stop
   if y4 <= -30:
       y4 = y4+30
   if y4 >= (h-60):
       y4 = y4-30
       
   if y <= 1:
           ys = 3
   elif y >= h:
             ys = -3
   elif x <=1:
        xs = 3
        pl2 += 1
        print "pehtis 1 (",pl,":",pl2,") pehtis 2"
   elif x >=w:
        xs = -3
        pl +=1
        print "pehtis 1 (",pl,":",pl2,") pehtis 2"
   if  x<=(x1+10):
     if y <= (y2+83) and y >= (y2-10) :
         xs = 3
   if x>=(x4-10):
     if y <= (y4+83) and y >= (y4-10):
         xs = -3
   x = x + xs
   y = y + ys
   dis.fill(blue)
   pygame.draw.line(dis, white, [350,500], [350,1], 7)
   bal(x,y)
   ta1(x1,y2)
   ta2(x4,y4)
   pygame.display.update()
   c.tick(70)
     
pygame.quit()
quit()

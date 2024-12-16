import pygame, random
from Player import Player
from Platform import Platform


pygame.init()

WIDTH = 450
HEIGHT = 900


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Doodle Jump")

player = Player(screen, WIDTH, HEIGHT)
platforms = []
countPlatforms = HEIGHT // 100
for i in range(1, countPlatforms):
    platforms.append(
        Platform(screen, 
        i * 100 + random.randint(0, 50), 
        random.randint(0,3)
    )) 

clock = pygame.time.Clock()

dt = 0



    


running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    screen.fill((135, 206, 235))
    player.update(dt, platforms)
    
    if player.y - player.radius < HEIGHT // 2:     
        yoffset = -player.y + player.radius + HEIGHT // 2

        # Shift all platforms downward by the offset
        for platform in platforms:
            platform.y += yoffset

        # Reset the player's y-coordinate to prevent out-of-bounds
        player.y = player.radius  + HEIGHT // 2

        # Remove platforms that are now off the bottom of the screen
        platforms = [platform for platform in platforms if platform.y < HEIGHT]

        # Calculate the starting y-position for new platforms
        new_platform_y = min(platform.y for platform in platforms) - 100  

        # Spawn new platforms at equal intervals
        while len(platforms) < countPlatforms:
            new_platform = Platform(
                screen,
                new_platform_y,
                random.randint(0,3)
            )
            platforms.append(new_platform)
            new_platform_y = min(platform.y for platform in platforms) - 100  

    
    if player.y > HEIGHT:
        print("game over")
        
    
    player.draw()
    
    for platform in platforms:
        if platform.countJumps == 0:
            platform.setInvisible()    
        platform.draw()
    pygame.display.flip()
    
            
    dt = clock.tick(60) / 1000

pygame.quit()
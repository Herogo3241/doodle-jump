import pygame


class Player:
    def __init__(self, screen, screen_width, screen_height):
        self.screen = screen
        self.radius = 15
        self.width = screen_width
        self.height = screen_height
        self.x = screen_width // 2
        self.y = screen_height - self.radius
        self.xspeed = 200
        self.yspeed = 0  # Start with no vertical speed
        self.initial_yspeed = -600  # Initial velocity for jumping
        self.gravity = 800  # Gravity pulling the player down
        self.color = (255, 100, 128)
        self.isGrounded = True
        self.jumping = False  # Track if the player is jumping
        self.isStart = True

    def update(self, dt, platforms):
        # Handle horizontal input
        self.keyInput(dt)

        # Wrap around screen horizontally
        if self.x < 0:
            self.x = self.width
        elif self.x > self.width:
            self.x = 0

        # Check if player is grounded (on a platform or ground level)
        self.isGrounded = False
        for platform in platforms:
            if self.checkCollision(platform) and self.yspeed > 200 and platform.options[platform.option] != "breakable":  
                self.isGrounded = True
                self.jumping = False  # Player is not jumping anymore
                self.yspeed = self.initial_yspeed  # Trigger jump
                self.y = platform.y - self.radius  # Position player on top of the platform
                break
            if self.checkCollision(platform) and self.yspeed > 200 and platform.options[platform.option] == "breakable" and platform.countJumps == 1:
                self.isGrounded = True
                self.jumping = False  
                self.yspeed = self.initial_yspeed  
                self.y = platform.y - self.radius  
                platform.countJumps -= 1
                break
            

        # Apply gravity if the player is not grounded
        if not self.isGrounded:
            self.yspeed += self.gravity * dt  # Gravity accelerates the fall

        # Update vertical position
        self.y += self.yspeed * dt

        # Prevent falling below the ground at start
        if self.isStart:
            if self.y + self.radius > self.height:
                self.y = self.height - self.radius
                self.isGrounded = True
                self.jumping = False
                self.yspeed = self.initial_yspeed
                self.isStart = False  

    def keyInput(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.x -= self.xspeed * dt
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.x += self.xspeed * dt

    def checkCollision(self, platform):
        player_left = self.x - self.radius
        player_right = self.x + self.radius
        player_top = self.y - self.radius
        player_bottom = self.y + self.radius

        # Platform's bounding box
        platform_left = platform.x
        platform_right = platform.x + platform.width
        platform_top = platform.y
        platform_bottom = platform.y + platform.height

        # Check for overlap
        if (
            player_right > platform_left and
            player_left < platform_right and
            player_bottom > platform_top and
            player_top < platform_bottom
        ) and self.yspeed > 0:
            return True

        return False

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (int(self.x), int(self.y)), self.radius)

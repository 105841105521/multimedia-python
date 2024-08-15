import pygame
import random

# Inisialisasi Pygame
pygame.init()

# Mengatur tampilan
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Simple Game")

# Warna
WHITE = (255, 255, 255)

# Memuat gambar karakter dan mengubah ukurannya
image_right = pygame.image.load('ZOMBIE.png')
image_right = pygame.transform.scale(image_right, (50, 50))
image_left = pygame.transform.flip(image_right, True, False)

# Memuat dan memutar musik latar
pygame.mixer.music.load('example.mp3')
pygame.mixer.music.play(-1)

# Variabel karakter
x, y = 100, 500
width, height = 50, 50
velocity = 5
is_jumping = False
jump_count = 10
facing_right = True

# Gravitasi
gravity = 1
y_velocity = 0

# Platform
platforms = [
    pygame.Rect(50, 550, 700, 50),
    pygame.Rect(150, 450, 150, 10),
    pygame.Rect(350, 350, 150, 10),
    pygame.Rect(550, 250, 150, 10)
]

# Musuh
enemy = pygame.Rect(300, 510, 40, 40)
enemy_velocity = 3

# Koin
coins = [pygame.Rect(random.randint(0, 750), random.randint(0, 500), 20, 20) for _ in range(5)]
score = 0

# Loop utama permainan
running = True
while running:
    pygame.time.delay(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Mendapatkan input dari keyboard
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > velocity:
        x -= velocity  # Gerakkan karakter ke kiri
        facing_right = False  # Karakter menghadap kiri
    if keys[pygame.K_RIGHT] and x < 800 - width - velocity:
        x += velocity  # Gerakkan karakter ke kanan
        facing_right = True  # Karakter menghadap kanan

    # Logika untuk lompatan
    if not is_jumping:
        if keys[pygame.K_SPACE]:
            is_jumping = True
            y_velocity = -15
    else:
        y_velocity += gravity
        y += y_velocity

        # Cek apakah karakter mendarat di platform
        landed = False
        for platform in platforms:
            if y + height >= platform.y and platform.x < x + width // 2 < platform.x + platform.width:
                if y + height <= platform.y + 10:
                    y = platform.y - height
                    is_jumping = False
                    y_velocity = 0
                    landed = True
                    break

        if not landed and y + height >= 600:
            y = 600 - height
            is_jumping = False
            y_velocity = 0

    # Logika untuk musuh
    enemy.x += enemy_velocity
    if enemy.x <= 0 or enemy.x >= 760:
        enemy_velocity *= -1

    # Cek tabrakan dengan musuh
    if enemy.colliderect(pygame.Rect(x, y, width, height)):
        print("Game Over!")
        running = False

    # Cek tabrakan dengan koin
    coins = [coin for coin in coins if not pygame.Rect(x, y, width, height).colliderect(coin)]
    score += 5 - len(coins)

    # Mengisi layar dengan warna putih dan menggambar karakter serta platform
    screen.fill(WHITE)
    for platform in platforms:
        pygame.draw.rect(screen, (0, 128, 0), platform)  # Platform warna hijau

    # Menggambar musuh
    pygame.draw.rect(screen, (255, 0, 0), enemy)  # Musuh warna merah

    # Menggambar koin
    for coin in coins:
        pygame.draw.rect(screen, (255, 215, 0), coin)  # Koin warna emas

    # Memilih gambar yang sesuai berdasarkan arah karakter
    if facing_right:
        screen.blit(image_right, (x, y))
    else:
        screen.blit(image_left, (x, y))

    # Memperbarui tampilan
    pygame.display.flip()

# Keluar dari Pygame
pygame.quit()

print("Your score:", score)

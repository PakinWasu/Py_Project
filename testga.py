import pygame
import sys

# กำหนดขนาดหน้าต่าง
WIDTH = 800
HEIGHT = 600

# กำหนดสี
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def run_game():
    # กำหนดการเริ่มต้นของ Pygame
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("My Game")

    # ลูปหลัก
    while True:
        # ตรวจสอบอีเวนต์ที่เกิดขึ้น
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # เตรียมพื้นหลัง
        screen.fill(BLACK)

        # วาดรูปสี่เหลี่ยมขาวในจุดกึ่งกลางหน้าต่าง
        pygame.draw.rect(screen, WHITE, (WIDTH/2 - 50, HEIGHT/2 - 50, 100, 100))

        # อัพเดตหน้าจอ
        pygame.display.flip()

run_game()

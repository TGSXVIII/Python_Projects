import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 400
COIN_RADIUS = 50
FPS = 30

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Coin Flip Visualization")
clock = pygame.time.Clock()

# Load coin image
coin_image = pygame.image.load("Pictures/coin.png")  # Replace with the path to your coin image
coin_image = pygame.transform.scale(coin_image, (2 * COIN_RADIUS, 2 * COIN_RADIUS))

def flip_coin():
    return random.choice(["Heads", "Tails"])

def main():
    coin_side = None
    flipping = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if not flipping:
                    flipping = True
                    coin_side = None

        screen.fill(WHITE)

        if flipping:
            # Simulate the coin flip
            pygame.time.delay(50)  # Introduce a delay for better visualization
            coin_side = flip_coin()

            # Stop flipping after a while
            if random.random() < 0.02:
                flipping = False

        # Draw the coin
        if coin_side == "Heads":
            screen.blit(coin_image, (WIDTH // 2 - COIN_RADIUS, HEIGHT // 2 - COIN_RADIUS))
        elif coin_side == "Tails":
            screen.blit(coin_image, (WIDTH // 2 - COIN_RADIUS, HEIGHT // 2 - COIN_RADIUS), pygame.transform.flip(coin_image, True, False))

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()

import pygame
import sys
import os

# === Play embedded MP3 ===
def play_music():
    pygame.mixer.init()
    mp3_path = os.path.join(
        getattr(sys, '_MEIPASS', os.path.abspath(".")), 'youre fucked.mp3'
    )
    pygame.mixer.music.load(mp3_path)
    pygame.mixer.music.play(-1)  # Loop forever

# === Start music ===
play_music()

# === Pygame window setup ===
pygame.init()
screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("this is so cool!")

font = pygame.font.Font(None, 30)

text_lines = [
    "Did you really think I would give you cheats to this game?",
    "I mean how trash are you that ytou need cheats?",
    "How about you learn to play like a real gooner?", 
    "Now you got a Trojan.",
    "",
    "",
    "yeah",
    "just let that sit in.",
    "You got get by a dude who jerks off 9 times a day and hates life.",
	"",
    "but you know what","i dont got to cheat in a fucking game",
    "when I game I do it for fun",
    "well.... any way","enjoy the music",
    "cause its jover and you are well...",
	"fucked!!!!",
    "Enjoy",
    "",
    "",
    "",
    "Music: 'You're F***ed' by Ylvis (via YouTube link)",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "replaying.",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
]

y = 600
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pass  # Ignore close button

    screen.fill((0, 0, 0))

    for i, line in enumerate(text_lines):
        text = font.render(line, True, (255, 255, 0))  # Yellow
        screen.blit(text, (50, y + i * 50))

    y -= 0.5  # Slower vertical scroll speed

    if y + len(text_lines) * 50 < 0:
        y = 600  # Reset scroll when text leaves screen

    pygame.display.flip()
    clock.tick(60)

import pygame, sys
import pygame.freetype
from pygame.locals import QUIT
from groq import Groq
import os

#from huggingface_hub import InferenceClient
#client = InferenceClient("HuggingFaceH4/zephyr-7b-beta")


client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

def text():
    full_prompt = f"""Imagine you a NPC for a pygame about bartending. Max length is 10 words"""
    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": full_prompt,
            }
        ],
        model="llama3-8b-8192",
    )
    answer = response.choices[0].message.content
    return answer

pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 176, 240)
# Fonts
FONT_SIZE = 24
font = pygame.freetype.SysFont(None, FONT_SIZE)

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pygame With Chat')


# Input box dimensions and position
input_box = pygame.Rect(50, HEIGHT - 100, WIDTH - 100, 50)
input_color_inactive = BLUE
input_color_active = WHITE
input_color = input_color_inactive

# Output box dimensions and position
output_box = pygame.Rect(50, 50, WIDTH - 100, 50)
output_color = BLUE

# Variables for input
active = False
text = text()
output_text = text

# Main loop
running = True
while running:
   for event in pygame.event.get():
        if event.type == QUIT:
              running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect
            if input_box.collidepoint(event.pos):
                active = not active
            else:
                active = False
            # Change the current color of the input box
            input_color = input_color_active if active else input_color_inactive
        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN:
                    output_text = text
                    text = ''
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode
                    
        
       
        # Render the screen
        screen.fill(WHITE)

        # Render the output box
        pygame.draw.rect(screen, output_color, output_box, 0, border_radius=20)
        font.render_to(screen, (output_box.x + 10, output_box.y + 10), output_text, BLACK)

        # Render the input box
        pygame.draw.rect(screen, input_color, input_box, 0, border_radius=20)
        font.render_to(screen, (input_box.x + 10, input_box.y + 10), text, BLACK)

        pygame.display.flip()
pygame.quit()


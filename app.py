import pygame, sys
from pygame.locals import QUIT
from groq import Groq
import os

#from huggingface_hub import InferenceClient

#client = InferenceClient("HuggingFaceH4/zephyr-7b-beta")
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

def text():
    full_prompt = f"""Image you a NPC for a pygame about bartending"""
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
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World!')
while True:
   for event in pygame.event.get():
       
       if event.type == pygame.KEYDOWN:
           answer = text()
           fontObj = pygame.font.Font('freesansbold.ttf', 32)
           textSurfaceObj = fontObj.render(answer, True, (255, 0, 0), (0, 0, 0))
           textRectObj = textSurfaceObj.get_rect()
           textRectObj.center = (200, 150)
           DISPLAYSURF.blit(textSurfaceObj, textRectObj)
       if event.type == QUIT:
           pygame.quit()
           sys.exit()
   pygame.display.update()

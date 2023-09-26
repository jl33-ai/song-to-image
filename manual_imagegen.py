import openai
import argparse
import csv
import time

openai.api_key = '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'

def prompt_to_image(): 
    prompt = input("Enter the custom prompt: ")
    try: 
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="1024x1024"
        )
        image_url = response['data'][0]['url']
        print('════════════════════════════════════════════════════════════════════════════════')
        print(f"Prompt: {prompt}")
        print(f"Successfully generated image 🖼️ ✅")
        print(f"URL: {image_url}")
        print('════════════════════════════════════════════════════════════════════════════════')
    except: 
        image_url = 'n/a'
        print('════════════════════════════════════════════════════════════════════════════════')
        print(f"Prompt: {prompt}")
        print(f"Image generation failed 🖼️ ❌")
        print('════════════════════════════════════════════════════════════════════════════════')
    return

if __name__ == "__main__":
    while True: 
        prompt_to_image()
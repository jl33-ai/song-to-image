import openai
import argparse
import csv
import time
import requests
from PIL import Image
from io import BytesIO
from genius_lyrics import get_lyrics

''' This program contains functions that are able to 
1. Convert a line of song lyrics into -> image prompts
2. Convert image prompts -> image 
'''

openai.api_key = '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'
SONG_NAME = 'American Pie'


def save_image(url, file_name):
    response = requests.get(url)
    if response.status_code == 200:  # HTTP status code for success
        img_data = BytesIO(response.content)
        img = Image.open(img_data)
        img.save(file_name)
    else:
        print(f"Failed to download image, HTTP status code: {response.status_code}")

def lyric_to_prompt(lyric_str):
    completion = openai.ChatCompletion.create(
        model="gpt-4", 
        messages=[{"role": "user", "content": f"Write me a short 5 to 10 word image generating prompt based on the lyrics: '{lyric_str}'."}, 
                  {"role": "user", "content": f"Make sure there are no inappropriate words"}]
    )
    
    final_prompt = completion['choices'][0]['message']['content'] + ', realistic'
    return final_prompt

def prompt_to_image(lyric_str): 
    prompt = lyric_to_prompt(lyric_str)
    try: 
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="1024x1024"
        )
        image_url = response['data'][0]['url']
        print(f"Prompt: {prompt}")
        print(f"Successfully generated image 🖼️ ✅")
        print(f"URL: {image_url}")
        try: 
            file_path = '/Users/justinlee/Documents/projport/song-to-image/gen_images/' + prompt.lower().replace(' ','-') + '.png'
            save_image(image_url, file_path)
            print("Saved image 💾")
        except:
            print("Could not save image 💾")
    except: 
        image_url = 'n/a'
        print(f"Prompt: {prompt}")
        print(f"Image generation failed 🖼️ ❌")
    return image_url, prompt

def save_to_csv(lyric_list):
    with open(file_path, "w", newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["Lyric", "Prompt", "Image_URL", "Gen_Time", ])
        
        print('════════════════════════════════════════════════════════════════════════════════')
        print("BEGINNING SONG -> IMAGE AUTOMATED SEQUENCE")
        print('🎼 -> 🏞️ 🎑 🌄 🌃')
        print('════════════════════════════════════════════════════════════════════════════════')
        for lyric in lyric_list:
            print()
            print('════════════════════════════════════════════════════════════════════════════════')
            print()
            print(f"Starting lyric 🎶: '{lyric}'")
            start_time = time.time()
            image_url, prompt = prompt_to_image(lyric)
            end_time = time.time()
            
            print(f"⏱️: Took {round(end_time-start_time, 1)}s")
            
            csvwriter.writerow([lyric, prompt, image_url])
        print()
        print('════════════════════════════════════════════════════════════════════════════════')
        print()
        print('DONE')

if __name__ == "__main__":
    # Replace this with the list of lyrics you obtain from the Genius API
    # lyrics = input("Enter lyrics: ")
    lyrics_list = get_lyrics(SONG_NAME)
    file_path = '/Users/justinlee/Documents/projport/song-to-image/thisbetterwork2.csv'
    # file_path = song_name.lower().replace(' ','-') + '_lyrics.csv'
    print()
    print('════════════════════════════════════════════════════════════════════════════════')
    print('🎧 LYRICS:')
    for lyric_line in lyrics_list:     
        print(lyric_line)
    print('════════════════════════════════════════════════════════════════════════════════')
    print()
    save_to_csv(lyrics_list)
    
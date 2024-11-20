import io
from gtts import gTTS

import pygame

def text_to_speech(text):
   
    tts = gTTS(text=text, lang='en') 
    audio_fp = io.BytesIO() 
    tts.write_to_fp(audio_fp) 
    audio_fp.seek(0) 
    return audio_fp 

def play_sound(audio_fp):

    pygame.mixer.init() 
   
    audio_fp.seek(0) 
    pygame.mixer.music.load(audio_fp, 'mp3') 
    
    pygame.mixer.music.play()

    # Wait for the audio to finish playing (commented out)
    #while pygame.mixer.music.get_busy():
       # pygame.time.Clock().tick(10)

# This code is for testing the functions when the script is run directly
'''if __name__ == '__main__':
    q='hi how do you do'
    text = q
    
    # Convert text to speech and get in-memory file-like object
    audio_fp = text_to_speech(text)
    
    # Play the generated speech audio
    play_sound(audio_fp)'''

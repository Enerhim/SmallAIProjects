import audio as a
import keyboard

while True:
    audio_input = a.GetAudio(5  )
    if (audio_input != None):
        audio_input_list = list(audio_input)
        print(audio_input_list)

        
        for letter in audio_input_list:
            keyboard.send(letter)
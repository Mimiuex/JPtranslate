import os
import wave
import time
import threading
import tkinter as eng_jp
import pyaudio
import Whisper_Translate
#import Text_Translator
import voicevox
import DeepL

class EngVoiceRecorder:
    def __init__(self):
        self.root = eng_jp.Tk()
        self.root.wm_title("ENG-JP")
        self.root.geometry("160x265")
        self.root.resizable(False, False)
        self.button = eng_jp.Button(text = "⏺", font = ("times", 200), command = self.click_handler)
        self.button.pack()
        self.label = eng_jp.Label(text = "00:00:00")
        self.label.pack()
        self.file_number = 1
        
        self.recording = False
        self.root.mainloop()
    
    def get_file_number(self):
        return self.file_number
    
    def update_file_number(self):
        exist = True
        while exist == True:
            if os.path.exists(f"recording{self.file_number}.wav"):
                self.file_number += 1
            else:
                self.file_number -= 1
                exist = False

    def click_handler(self):
        if self.recording:
            self.recording = False
            self.button.config(text = "⏺", fg = "black")

            """self.label.config(text = "Press the button and start speaking.")"""

            """self.update_file_number()
            print(Whisper_Translate.Audio_to_Text(self.get_file_number()))""" #<-- DEBUG bode 

        else:
            self.recording = True
            self.button.config(text = "■", fg = "red")
            """self.label.config(text = "Press button to stop.")"""
            threading.Thread(target = self.record).start()

    def record(self):

        audio = pyaudio.PyAudio()
        stream = audio.open(format = pyaudio.paInt16, channels = 1, rate = 44100, input = True, frames_per_buffer = 1024)
        frames = []

        start = time.time()

        while self.recording:
            data = stream.read(1024)
            frames.append(data)

            passed = time.time() - start
            secs = passed % 60
            mins = secs // 60
            hours = mins // 60
            self.label.config(text = f"{int(hours):02d}:{int(mins):02d}:{int(secs):02d}")

        stream.stop_stream()
        stream.close()
        audio.terminate()

        exists = True
        i = 1
        while exists:
            if os.path.exists(f"recording{i}.wav"):
                i += 1
            else:
                exists = False
        
        sound_file = wave.open(f"recording{i}.wav", "wb")
        sound_file.setnchannels(1)
        sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
        sound_file.setframerate(44100)
        sound_file.writeframes(b"".join(frames))
        sound_file.close()

        self.update_file_number()
        

        print("Source language: English")
        print(Whisper_Translate.Audio_to_Text(self.get_file_number()))

       
        translation = DeepL.translate_text(Whisper_Translate.Audio_to_Text(self.get_file_number()), key)

        print("Translating to Japanese...")
        print(translation)

        print("Audio will now be played:\n... ")
        voicevox.text_to_voice(translation)


def banner():
    print("\n******-\\\ Please remember to speak to your dedicated microphone clearly! //-******\n")
    print("                      -_.Enter authentication key for DeepL._-")
    

banner()
key = input("Key: ".rjust(81//3))
os.system('cls' if os.name == 'nt' else 'clear')

EngVoiceRecorder()




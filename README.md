This program's aim is to convert English speech into Japanese speech.

To do this, we will use some tools:

Language used: Python
Implement a python Tk GUI.
Translation api - Google translate and DeepL
Open.ai Whisper api
Voicevox
First we record speech using pyaudio in python library and create a wav file. Use Whisper to convert wav to English text. Utilise DeepL to convert the text to Japanese. Finally send Japanese text to Voicevox and output synthesized voice.

!!! Important:

As of now, you will have to download and have Voicevox running as we will be making requests to it.
You will need to have a DeepL authentication key in order to use DeepL api.

Update 06/03:

-Changed default translation api to DeepL.
-Beginning of program requires user to input their DeepL authetication key in order to access DeepL api.

Update 08/03:

-Minor changes to Main.py and major changes made to VoiceVoxWrapper.py and voicevoxx.py on how it interacts with VoiceVox app.

- This program uses VoiceVox and interacts with it so make sure you download and have it running.
Download VoiceVox: https://voicevox.hiroshiba.jp/


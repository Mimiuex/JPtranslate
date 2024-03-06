This program's aim is to convert English speech into Japanese speech.

To do this, we will use some tools:

Language used: Python
Implement a python Tk GUI.
Translation api - Google translate --> (Now DeepL)
Open.ai Whisper api
Voicevox
First we record speech using pyaudio in python library and create a wav file. Use Whisper to convert wav to English text. Utilise DeepL to convert the text to Japanese. Finally send Japanese text to Voicevox and output synthesized voice.

!!! Important:

As of now, you will have to download and have Voicevox running as we will be making requests to it. <-- Will be making changes to make it so you don't have to.
You will need to have a DeepL authentication key in order to use DeepL api.
Update 06/03:

Switched to DeepL api because DeepL creates a more 'natural' translation than Google translate.
Beginning of program requires user to input their DeepL authetication key in order to access DeepL api.
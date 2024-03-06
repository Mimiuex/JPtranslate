import requests
import json
import sounddevice as sd
import numpy as np

host = "127.0.0.1"
port = "50021"
speaker = 20

def audio_query(text: str) -> dict:
    params = {"text": text, "speaker": speaker}

    res = requests.post(f"http://{host}:{port}/audio_query", params = params)

    query_data = res.json()

    return query_data

def post_synthesis(query_data: dict) -> bytes:
    params = {"speaker": speaker}
    headers = {"content-type":"application/json"}

    res = requests.post(f"http://{host}:{port}/synthesis", data = json.dumps(query_data), params = params, headers = headers)

    return res.content

def play_wavfile(wav_data: bytes):
    sample_rate = 24000
    wav_array = np.frombuffer(wav_data, dtype= np.int16)
    sd.play(wav_array, sample_rate, blocking = True)

def text_to_voice(input_text):
    res = audio_query(input_text)
    wav = post_synthesis(res)
    play_wavfile(wav)


"""debug code"""
#text_to_voice("和歌山には和気藹々で若々しい若者はわさびの侘び寂びを分からずに羽ずつと話ずつを話すわ。なぜわざわざですわ？技せんはわずらわと罠なのよ。もう、我々の若緑色のわさびの技は侘び寂びであると思うわ。")
#text_to_voice("斜め七十七度の並びでー泣く泣くいななくナナハン七台ー難なく並べて長眺め。")   
#text_to_voice("にゃにゃめにゃにゃじゅうにゃにゃどのにゃらびでにゃくにゃくいにゃにゃくにゃにゃはんにゃにゃだいにゃんにゃくにゃらべてにゃがにゃがめ") 
#text_to_voice("ワタクシの名前はドラリアですわ〜、夢がある。そして、この夢の中で、お前のことがいないわ！ワタクシの夢を自分で絶対に信じて続けるために、消えなさい！。")



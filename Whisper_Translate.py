
import whisper

def Audio_to_Text(filenumber):
    model = whisper.load_model('base')

    audio = whisper.load_audio(f"recording{filenumber}.wav")
    print(f"Opening recording{filenumber}.wav ...")
    #audio = whisper.load_audio(f"recording2.wav")
    
    audio = whisper.pad_or_trim(audio)
    mel = whisper.log_mel_spectrogram(audio).to(model.device)

    options = whisper.DecodingOptions(fp16 = False)
    result = whisper.decode(model, mel, options)

    return result.text
    
#print(Audio_to_Text())


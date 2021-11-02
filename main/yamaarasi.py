import struct
import pyaudio
import pvporcupine
import simpleaudio
import speech_recognition as sr

WAKEWORD = ["alexa"]  # ウェイクワードを指定

porcupine = pvporcupine.create(keywords=WAKEWORD)

wav_obj = simpleaudio.WaveObject.from_wave_file("main/sound.wav")

# オーディオストリームの生成
pa = pyaudio.PyAudio()

r = sr.Recognizer()
mic = sr.Microphone()

audio_stream = pa.open(
    rate=porcupine.sample_rate,
    channels=1,
    format=pyaudio.paInt16,
    input=True,
    frames_per_buffer=porcupine.frame_length
)







def branch_method(out_voice):


        # "ストップ" と言ったら音声認識を止める
    if out_voice == "こんにちは":
        pass
        # vovox.generate_wav("こんにちは", speaker=0, filepath="./voice.wav")
        # voice = simpleaudio.WaveObject.from_wave_file("voice.wav")
        # voice.play()

    else:
        print("その処理は登録されていません")




while True:

    # 音声認識
    pcm = audio_stream.read(porcupine.frame_length)
    pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)
    result = porcupine.process(pcm)

    if result >= 0:  # ウェイクワード検出時の処理
        wav_obj.play()  # 音を鳴らす
        print("Wake Word!")
        print("Say something ...")




        with mic as source:
            r.adjust_for_ambient_noise(source)  # 雑音対策
            audio = r.listen(source)

        print("Now to recognize it...")

        try:
            out_voice = r.recognize_google(audio, language='ja-JP')
            print(f'voice={out_voice}')



        # 以下は認識できなかったときに止まらないように。
        except sr.UnknownValueError:
            print("could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))




    else:
        print("?")



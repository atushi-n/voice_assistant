import struct
import threading

import pyaudio
import pvporcupine
import simpleaudio
import speech_recognition as sr


class Assistant:

    # porcupineの生成
    KEYWARDS = ["alexa"] # ウェイクワードを指定

    def __init__(self):
        self.event = threading.Event()
    def listen(self):

        porcupine = pvporcupine.create(keywords=Assistant.KEYWARDS)
        print(Assistant.KEYWARDS)


        wav_obj = simpleaudio.WaveObject.from_wave_file("sound.wav")



        # オーディオストリームの生成
        pa = pyaudio.PyAudio()
        audio_stream = pa.open(
            rate=porcupine.sample_rate,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=porcupine.frame_length)

        while True:

            self.event.wait()

            # 音声認識
            pcm = audio_stream.read(porcupine.frame_length)
            pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)
            result = porcupine.process(pcm)


            if result >= 0:# ウェイクワード検出時の処理
                print("Wake Word!")
                wav_obj.play()
                print("Say something ...")

                r = sr.Recognizer()
                mic = sr.Microphone()
                with mic as source:
                    r.adjust_for_ambient_noise(source)  # 雑音対策
                    audio = r.listen(source)

                print("Now to recognize it...")

                try:
                    out_voice = r.recognize_google(audio, language='ja-JP')
                    print(f'voice={out_voice}')

                    # "ストップ" と言ったら音声認識を止める
                    if out_voice == "ストップ":
                        print("end")
                        break

                        # "ストップ" と言ったら音声認識を止める
                    if out_voice == "こんにちは":
                        pass
                        #vovox.generate_wav("こんにちは", speaker=0, filepath="./voice.wav")
                        #voice = simpleaudio.WaveObject.from_wave_file("voice.wav")
                        #voice.play()

                # 以下は認識できなかったときに止まらないように。
                except sr.UnknownValueError:
                    print("could not understand audio")
                except sr.RequestError as e:
                    print("Could not request results from Google Speech Recognition service; {0}".format(e))




            else:
                print("?")



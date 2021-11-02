import json
import requests
import wave

def generate_wav(text, speaker=1, filepath='./audio.wav'):
    host = 'localhost'
    port = 50021

    params = (
        ('text', text),
        ('speaker', speaker),
    )

    #オーディオを生成するクエリをリクエストする
    response1 = requests.post(
        f'http://{host}:{port}/audio_query',
        params=params
    )

    headers = {'Content-Type': 'application/json',}

    #クエリを投げて声をジェネレートしてもらう
    response2 = requests.post(
        f'http://{host}:{port}/synthesis',
        headers=headers,
        params=params,
        data=json.dumps(response1.json())
    )

    #wavとして保存
    wf = wave.open(filepath, 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(2)
    wf.setframerate(24000)
    wf.writeframes(response2.content)
    wf.close()


text = 'こんにちは！'
generate_wav(text, speaker=0, filepath="../main/voice.wav")

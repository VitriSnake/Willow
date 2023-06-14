import openai
import speech_recognition as sr


def ask_gpt(messages, api_key, model="gpt-3.5-turbo"):    
    openai.api_key = api_key

    print(messages)

    completion = openai.ChatCompletion.create(
        model=model, 
        messages=messages
    )
    result = completion['choices'][0]['message']['content']
    return result

def hear():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language='fr-FR')
        return text.lower()
    except sr.UnknownValueError:
        print('Impossible de comprendre. ')
from gtts import gTTS
import sys
import os
import libs
import time

language = 'fr'
a_key = "" # API KEY GOES HERE
forfait = "Basique"
last_request = 0


myobj = gTTS(text="Je suis prêt à vous aider. Dites 'ok willow' pour parler avec moi.", lang=language, slow=False)
myobj.save("audio.mp3")
os.system("mpg321 audio.mp3")

while True:
    try:
        user_said = libs.hear()
        if "OK WILLOW" in user_said.upper() or "OK OUI L'EAU" in user_said.upper():
            # Remove "ok willo" from the request
            prompt = user_said.split("ok willow")[-1].strip()

            history = [{"role": "user", "content": "Tu es un assitant vocal nomé Willow. Voici la question: {request}".format(request=prompt)}]

            # Blip sound
            os.system("mpg321 blip.mp3")

            # Get the ChatGPT response.
            result = libs.ask_gpt(history, a_key)

            # Say the response
            myobj = gTTS(text=result, lang=language, slow=False)
            myobj.save("audio.mp3")
            os.system("mpg321 audio.mp3")

            # End bilp
            os.system("mpg321 blip.mp3")

            # Init the last request.
            last_request = time.time()
        
            history.append({"role": "assistant", "content": result})

        elif time.time() - last_request <= 10:
            prompt = user_said

            # Add request to history
            history.append({"role": "user", "content": prompt})
            
            # Blip sound
            os.system("mpg321 blip.mp3")

            # Get the ChatGPT response.
            result = libs.ask_gpt(history, a_key)

            # Say the response.
            myobj = gTTS(text=result, lang=language, slow=False)
            myobj.save("audio.mp3")
            os.system("mpg321 audio.mp3")

            # End bilp
            os.system("mpg321 blip.mp3")

            # Init the last request
            last_request = time.time()

            # Add the request to the history.
            history.append({"role": "assistant", "content": result})

        else:
            print('[LOG] User said: '+user_said)
            print('[LOG] Clearing history.')

    except KeyboardInterrupt:
        print('Merci d\'avoir utilisé Willow. ')
        sys.exit(0)

    except:
        pass

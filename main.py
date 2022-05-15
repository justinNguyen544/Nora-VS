import speech_recognition as sr


# obtain audio from the microphone
r = sr.Recognizer()

# get the default microphone
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    # Listens to a command, using AVD
    print("Say something...!")

    while True:
        audio = r.listen(source)

        # Recognizer speech using Google as a service: online
        text = r.recognize_google(audio)

        print(text)
        if "bye" in text:
            break
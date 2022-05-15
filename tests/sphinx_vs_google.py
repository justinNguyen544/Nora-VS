import speech_recognition as sr
from datetime import datetime



# ----------------------------------------------------------------
# Getting Today's Datetime
today = datetime.now()
  
print("Today is {} {}, {}:".format(today.month, today.day, today.year))
print("Time is now: {} Hour, {} Minute, {} Second".format(today.hour, today.minute, today.second))
# ---------------------------------------------------------------

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
        google = r.recognize_google(audio)
        sphinx = r.recognize_sphinx(audio)
        print("Google: {}\n\nSphinx: {}".format(google, sphinx))
        
        if "bye" in google:
            break

        
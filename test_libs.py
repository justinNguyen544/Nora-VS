# ========== testing =============
# import speech_recognition as sr


# # obtain audio from the microphone
# r = sr.Recognizer()

# # get the default microphone
# with sr.Microphone() as source:
#     r.adjust_for_ambient_noise(source)
#     # Listens to a command, using
#     print("Say something...!")

#     # while True:
#     audio = r.listen(source)

#     # Recognizer speech using Google as a service: online
#     text = r.recognize_google(audio)

#     print(text)


# =========== function ================
# import speech_recognition as sr

# def take_command():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print('Listening...')
#         r.pause_threshold = 1
#         r.energy_threshold = 50
#         audio = r.listen(source)

#     try:
#         print('Recognizing...')
#         qry = r.recognize_google(audio, language='en-in')
#         print(f"user said: {qry}\n")
        
# #     if any error occurs this line will run
#     except Exeption as e:
#     # if you don't want to print the error comment the bottom line
#         print(e)
#         print('Say that again please\n')
#         return 'None'

#     return qry
  
# if __name__ == '__main__':
# 	while True:
#   		qry = takecommand().lower()

# ================ A single ===========================
# import speech_recognition as sr
# recognizer = sr.Recognizer()
# microphone = sr.Microphone()
# with microphone as source:
#     recognizer.adjust_for_ambient_noise(source)
#     audio = recognizer.listen(source)
#     command = recognizer.recognize_google(audio)
#     print(command)
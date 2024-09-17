import speech_recognition as sr

import pyaudio
r = sr.Recognizer()
# for index, name in enumerate(sr.Microphone.list_microphone_names()):
#     print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))



def record_speech():
    try:
        with sr.Microphone() as source2:
            print("listening....")
            r.adjust_for_ambient_noise(source2,duration=0.2)
            audio = r.listen(source2)
            text_got = r.recognize_google(audio)
        return text_got
    except sr.RequestError as e:
        print(f"request errors {e}")
    except sr.UnknownValueError:
        print("Unkonown value error")

message = record_speech()
print(message)
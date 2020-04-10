#!/usr/bin/env python
# coding: utf-8

# In[26]:


# # Requirements
# # python 3.6
# pip install gTTS
# pip install googletrans
# pip install pyAudio
# pip install speechrecognition
# !apt install libasound2-dev portaudio19-dev libportaudio2 libportaudiocpp0 ffmpeg  --------> not sure about this
# pip install google-speech
# pip install pyttsx3



# In[28]:


import googletrans

print(googletrans.LANGUAGES)


# In[29]:


from googletrans import Translator


# In[30]:


translator = Translator()


# In[ ]:


import speech_recognition as sr
from gtts import gTTS 
import os 


def main():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)

        print("Please say something")

        audio = r.listen(source)

        print("Recognizing Now .... ")


        # recognize speech using google

        try:
            print("You have said \n" + r.recognize_google(audio))
            print("Audio Recorded Successfully \n ")
       
            newtext1=r.recognize_google(audio)
            print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")       
            print(newtext1)
            
            result = translator.translate(newtext1 , src='en', dest='te')
            print(result.src)
            print(result.dest)
            print(result.text)
            mytext=result.text
            language = 'te'
            myobj = gTTS(text=mytext, lang=language, slow=False) 
            myobj.save("welcome2.mp3") 

            # Playing the converted file 
            os.system("mpg321 welcome1.mp3") 

        except Exception as e:
            print("Error :  " + str(e))




        # write audio

        with open("recorded.wav", "wb") as f:
            f.write(audio.get_wav_data())
        
    


if __name__ == "__main__":
    main()
    #result = translator.translate(r.recognize_google(audio) , src='en', dest='te')
    
    


# In[ ]:





# In[ ]:





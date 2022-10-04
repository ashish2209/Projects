import speech_recognition as sr
import pyttsx3 as p 
import tkinter as tk
import wikipedia
import webbrowser
from news import *
from weather import *
from music import *
from tkinter import *
from PIL import ImageTk,Image
import datetime
import randfacts

from selenium import webdriver
class music():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='C:\Program Files\Google\Chrome\Application\chrome.exe')
        
    def play(self,query):
        self.query = query
        self.driver.get(url='https://www.youtube.com/results?search_query=' + query)
        video = self.driver.find_element_by_xpath('//*[@id="video-title"]/yt-formatted-string')
        video.click()
class infow():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='C:\Program Files\Google\Chrome\Application\chrome.exe')
        
    def get_info(self,query):
        self.query = query
        self.driver.get(url='https://www.wikipedia.org/')
        search = self.driver.find_element_by_xpath('//*[@id="searchInput"]')
        search.click()
        search.send_keys(query)
        enter = self.driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/button/i')
        enter.click()
        
engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate',180)
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
print(voices)
def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        return("good morning")
    elif hour>=12 and hour<16:
        return("good afternoon")
    else:
        return("good evening")

today_date=datetime.datetime.now()
r = sr.Recognizer()

speak("Hello sir! " + wishme())
speak("today is " + today_date.strftime("%d") + (today_date.strftime("%B")) + ", And its currently" + (today_date.strftime("%I")) + (today_date.strftime("%M") + (today_date.strftime("%p"))))
speak("Temp in Kanpur is " + str(temp()) + "degree celcius " + " and with " + str(des()))
speak("what can i do for you?")
    
def check():
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source,1.2)
        print("listening")
        audio = r.listen(source)
        text2 = r.recognize_google(audio)
        engine.runAndWait()
        print(text2)
        x = text2.split(" ")
    if "information" in text2:
        speak("you need information regarding what?")
        with sr.Microphone() as source:
            r.energy_threshold = 10000
            r.adjust_for_ambient_noise(source,1.2)
            print("listening")
            audio = r.listen(source)
            infor = r.recognize_google(audio)
            print(infor)
        speak("searching for {} in wikipedia..".format(infor))
        print("searching for {} in wikipedia..".format(infor))
        assist = infow() 
        assist.get_info(infor)
        engine.runAndWait()
        print("happy reading. :)")
    elif "play" and "video" in text2:
       speak("you want me to play which video?")
       with sr.Microphone() as source:
           r.energy_threshold = 10000
           r.adjust_for_ambient_noise(source,1.2)
           print("listening")
           audio = r.listen(source)
           vid = r.recognize_google(audio)
           print(vid)
       print("playing {} in youtube..".format(vid))
       speak("playing {} in youtube..".format(vid))
       assist = music();
       assist.play(vid)
    elif "play" and "song" in text2:
        speak("you want me to play which song?")
        with sr.Microphone() as source:
           r.energy_threshold = 10000
           r.adjust_for_ambient_noise(source,1.2)
           print("listening")
           audio = r.listen(source)
           song1 = r.recognize_google(audio)
           print(song)
        print("playing {} ".format(song1))
        speak("playing {} ".format(song1))
        assist = song()
        assist.plays(song)
    elif "news" in text2:
        arr = news()
        for i in range(len(arr)):
            print(arr[i])
            e1.insert(tk.INSERT,arr[i])
            speak(arr[i])
    elif "facts" in text2:
        x = randfacts.getFact()
        print(x)
        speak("Did you know that, "+x)
    
    elif "quit" in x:
        speak("have a nice day sir!")
        root.destroy();
    else:
        speak("sir, i did not get that. please repeat..")
       
root = tk.Tk()
root.geometry("780x400")
bg = PhotoImage(file = r"D:\\Study material\\tech_planet2.png" )
bg = bg.subsample(1)
lbl = Label(image = bg)
lbl.image = bg
lbl.grid(column=0,row=3)
root.title('Voice Assistant')
root.configure(bg="lightgreen")
l2 = tk.Label(root, text = "VOICE ASSISTANT",bg="darkblue",fg="white",font = "44")
l2.place(x=300, y=50)
b = tk.Button(root, text = ":Speak:", font = "30", bg="blue", fg="white",command=check)
b.place(x=330, y=300, height=50, width=100)
root.mainloop()
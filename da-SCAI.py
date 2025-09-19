import pyautogui  # pip install PyAutoGUI (To control the mouse and keyboard)
from winsound import PlaySound, SND_ASYNC # Built-in Module (To play sound effects)
import pyttsx3  # pip install pyttsx3 (Becomes the voice of the Assistant)
import os # Built-in Module (To open Apps and Files)
import webbrowser # pip install webbrowser (To open websites and Apps)
import wikipedia  # pip install wikipedia
import datetime # Built-in Module (To get the exact time)
import speech_recognition as sr # pip install SpeechRecognition (To take voice commands)

# =========================================================
"""SETTING UP THE VOICE MODULE"""

# Intializing Engine
engine = pyttsx3.init('sapi5')

# Voices
voices = engine.getProperty('voices')
bot_voice = 1 # (0 for DAVID, 1 for ZIRA)
engine.setProperty('voice', voices[bot_voice].id)

# Rate
rate = engine.getProperty('rate')
engine.setProperty('rate', 130) # (1 to 200)

# Volume
volume = engine.getProperty('volume')
engine.setProperty('volume', 100) # (1 to 100)

# =========================================================
"""SOUND EFFECTS - SFX"""
system_ready_sfx = 'SFX\\system-ready.wav'
listening_sfx = 'SFX\\listening.wav'
recognize_sfx = 'SFX\\recognizing.wav'
say_again_sfx = 'SFX\\say_again.wav'
wish_me_sfx = 'SFX\\wishme.wav
exit_sfx = 'SFX\\exit.wav'

# =========================================================
"""FUNCTIONS FOR LONG TASKS"""


def speak(audio_str):  # Function to make the computer speak using pyttsx3
    engine.say(audio_str)
    engine.runAndWait()


def wishMe():  # Function to wish the user by seeing the exact time
    hour = int(datetime.datetime.now().hour)
    if (hour >= 0) and (hour < 12):
        print("\nGood Morning")
        print("I am SCAI, your personal assistant waiting for your command!")
        speak("Good Morning, I am SKY, your personal assistant waiting for your command!") # Cannot pronounce SCAI properly, so prints SCAI and says SKY

    elif (hour >= 12) and (hour <= 16):
        print("\nGood Afternoon")
        print("I am SCAI, your personal assistant waiting for your command!")
        speak("Good Afternoon, I am SKY, your personal assistant waiting for your command!")

    else:
        print("\nGood Evening")
        print("I am SCAI, your personal assistant waiting for your command!")
        speak("Good Evening, I am SKY, your personal assistant waiting for your command!")


def takeCommand():  # Takes voice command from user
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("\nListening...")
        speak("Listening")
        PlaySound(listening_sfx, SND_ASYNC)
		
        r.pause_threshold = 0.8 # seconds of non-speaking audio before a phrase is considered complete
        r.energy_threshold = 290 # minimum audio energy to consider for recording
        r.phrase_threshold = 0.3 # seconds of non-speaking audio before a phrase is considered complete
		r.adjust_for_ambient_noise(source) # Adjusts the recogniser sensitivity to ambient noise
        audio = r.listen(source)
    try:
        print("***Recognizing***\n")
        speak("Recognizing")
        PlaySound(recognize_sfx, SND_ASYNC)
        query = r.recognize_google(audio, language='en-in')
        print(f"USER : {query}\n")
    except Exception as e:
        # print(e)
        print("Say that again please...")
        speak("Say that again please")
        PlaySound(say_again_sfx, SND_ASYNC)
        return "None"
    return query


def Email(to, content, subject):  # Function to send an Email
	# You will have to change these coordinates according to your screen resolution and the COMPOSE button's position in Gmail
	x_coo, y_coo = 185, 261	# Coordinates taken as per the ratio - 1920x1080
    os.startfile("PATH\\TO\\THE\\BROWSER\\*.exe")
    pyautogui.sleep(3)
	webbrowser.open("https://mail.google.com")
	pyautogui.sleep(6)

	"""
	The steps after these are used only for the accounts that have already been logged in in the browser
    So kindly log in with your email ID first and then try executing Email()
 	"""
	pyautogui.moveTo(x_coo, y_coo, duration=0.5)
	pyautogui.click()
	pyautogui.sleep(1.5)
	
	pyautogui.write(to, 0.1)
	pyautogui.press('enter')
	pyautogui.write("me@gmail.com", 0.1)
	pyautogui.press('enter')
	
	pyautogui.press('tab')
	pyautogui.write(subject, 0.1)
	
	pyautogui.press('tab')
	pyautogui.write(content, 0.1)
	pyautogui.press('enter')
	pyautogui.press('enter')
	pyautogui.write("Regards,\nSCAI-D.", 0.1)
	pyautogui.press('enter')

	pyautogui.write("\nPS: This mail was written by a Desktop Assistant - SCAI.\nKindly ignore if there are any errors in spelling or grammar\nThanks :)", 0.1)
	pyautogui.hotkey('ctrl', 'shift', 'up')
	pyautogui.hotkey('ctrl', 'shift', 'up')
	pyautogui.hotkey('shift', 'home')
	pyautogui.hotkey('ctrl', 'i')
	pyautogui.hotkey('right')
	pyautogui.hotkey('enter')
	pyautogui.hotkey('ctrl', 'i')
	pyautogui.hotkey('ctrl', 'enter')

	pytauogui.sleep(3)
	pyautogui.hotkey('ctrl', 'w')
    
	print("Mail Sent Successfuly!")
    speak("Mail Sent Successfuly!")


def playMovie(): # Asks the Platform on which the User wants to watch a movie
    print("On which Platform do you want to watch the movie?")
    speak("On which Platform do you want to watch the movie?")
    try:
        movie_web = takeCommand().lower()
        if ('prime' in movie_web) or ('amazon prime' in movie_web) or ('amazon prime video' in movie_web) or ('prime video' in movie_web) or ('primevideo' in movie_web):
            print("Opening Amazon Prime...")
            speak("Opening Amazon Prime")
            webbrowser.open("https://primevideo.com")

        elif ('netflix' in movie_web) or ('netflix.com' in movie_web) or ('netflix dot com' in movie_web) or ('series on netflix' in movie_web) or ('movies on netflix' in movie_web) or ('netflix movies' in movie_web) or ('netflix series' in movie_web):
            print("Opening Netflix...")
            speak("Opening Netflix")
            webbrowser.open("https://netflix.com")

        elif ('laptop' in movie_web) or ('downloaded' in movie_web) or ('my laptop' in movie_web) or ('my computer' in movie_web) or ('offline' in movie_web):
            print("Opening Movies Folder...")
            speak("Opening Movies Folder")
            movie_path = "PATH\\TO\\THE\\MOVIE\\FOLDER"
            os.startfile(movie_path)

    except Exception as e:
        print("Sorry, I couldn't get what you said, can you please repeat the platform name?")
        speak("Sorry, I couldn't get what you said, can you please repeat the platform name?")
        return "None"
    return movie_web


def search(): # Searches the user's query online on Google/YouTube
    try:
        print("Where do you want me to search, Google or YouTube?")
        speak("Where do you want me to search, Google or YouTube?")
        search_site = takeCommand().lower()

        if ('on google' in search_site) or ('google' in search_site) or ('search on google' in search_site) or ('google.com' in search_site) or ('google dot com' in search_site):
            print("What do you want me to search for on Google?")
            speak("What do you want me to search for on Google?")
            
            search_item = takeCommand().lower()
            search_item = search_item.replace("search for", '') # Strips the query and searches the keyword from the query
            search_item = search_item.replace("search that", '')
            search_item = search_item.replace("on google", '')
            search_item = search_item.replace("google", '')
            search_item = search_item.replace("search on", '')
            search_item = search_item.replace("please look for", '')
            search_item = search_item.replace("look for", '')
            search_item = search_item.replace("could you", '')
            search_item = search_item.replace("for", '')
            search_item = search_item.replace("could you please", '')
            search_item = search_item.replace("would you", '')
            search_item = search_item.replace("can you", '')
            search_item = search_item.replace("will you", '')
            search_item = search_item.replace("location of", '')
            
            print(f"Searching about {search_item.title}...")
            speak(f"Searching about {search_item}")
            webbrowser.open(f"https://google.com/search?q={search_item.lower()}")

        elif ('on youtube' in search_site) or ('youtube' in search_site) or ('search on youtube' in search_site) or ('youtube.com' in search_site) or ('youtube dot com' in search_site):
            print("What do you want me to search for on YouTube?")
            speak("What do you want me to search for on YouTube?")
            
            search_item = takeCommand().lower()
            search_item = search_item.replace("search for", '')
            search_item = search_item.replace("search that", '')
            search_item = search_item.replace("on youtube", '')
            search_item = search_item.replace("youtube", '')
            search_item = search_item.replace("search on", '')
            search_item = search_item.replace("please look for", '')
            search_item = search_item.replace("look for", '')
            search_item = search_item.replace("could you", '')
            search_item = search_item.replace("for", '')
            search_item = search_item.replace("could you please", '')
            search_item = search_item.replace("would you", '')
            search_item = search_item.replace("can you", '')
            search_item = search_item.replace("will you", '')

            print(f"Searching about {search_item.title()} on YouTube...")
            speak(f"Searching about {search_item} on YouTube...")
            webbrowser.open(f"https://www.youtube.com/results?search_query={search_item.lower()}")
    except Exception as e:
        speak("Couldn't understand what you said, can you please repeat?")
        print("Couldn't understand what you said, can you please repeat?")
    return search_site


# Initialising some Query Variables to later check if the Query is equal to these variables or not

how_are_you_var = 'hey how are you' or 'how are you' or 'hello' or 'hi' or "how's it going" or 'how is it going' or "what's up" or 'whats up' or 'how do you do' or 'how have you been' or 'how are you doing' or 'how are you feeling' or 'how are you today' or 'how are you doing today'


your_day_var = 'how is your day' or 'how is your day going' or 'how is your day been' or 'how has your day been' or 'how has your day gone' or 'how has your day been going' or 'how is your day so far' or 'how has your day been so far'


capabilities_var = 'what can you do' or 'what are your capabilities' or 'what are your functions' or 'what are your features' or 'what stuff can you do' or 'what stuff can you help me with' or 'what stuff can you assist me with' or 'what stuff can you do for me' or 'what all can you do' or 'what all can you help me with' or 'what all can you assist me with' or 'what all can you do for me'


thankyou_var = 'thank you' or 'thanks' or 'thankyou' or 'thanks a lot' or 'thank you so much' or 'thanks a lot for your help' or 'thank you so much for your help' or 'thanks a lot for helping me' or 'thank you so much for helping me' or 'thank you very much' or 'thanks very much'


send_email_var = 'send email' or 'send me an email' or 'email to' or 'email me' or 'can you send an email' or 'could you send an email' or 'can you send me an email' or 'could you send me an email' or 'send an email to someone'


movie_var = 'watch movie' or 'movie' or 'watch a movie' or 'i want to watch a movie' or 'i want to watch movie' or 'can we watch a movie' or 'could we watch a movie' or 'can we watch movie' or 'could we watch movie' or "let's watch a movie" or "let's watch movie"


weather_var = 'weather' or 'weather report' or 'weather reports' or 'tell me the weather' or 'tell me the weather report' or 'tell me the weather reports' or 'what is the weather' or 'what is the weather report' or 'what is the weather reports' or 'how is the weather' or 'how is the weather report' or 'how is the weather reports'


time_var = 'the time' or 'tell me the time' or 'what is the time' or 'can you tell me the time' or 'could you tell me the time' or 'do you know the time' or 'do you have the time' or 'could you please tell me the time' or 'can you please tell me the time'


calculator_var = 'open calculator' or 'calculator' or 'start calculator' or 'launch calculator' or 'can you open calculator' or 'could you open calculator' or 'can you start calculator' or 'could you start calculator' or 'can you launch calculator' or 'could you launch calculator'


search_var = 'search online' or 'search for' or 'search something' or 'google' or 'look up' or 'look for' or 'look something' or 'can you search' or 'could you please search' or 'can you google' or 'could you google' or 'please search for'


location_var = 'where is' or 'location of' or 'locate' or 'find location of' or 'find the location of' or 'find where is' or "find where's" or "where's" or 'can you locate' or 'could you please locate' or 'can you find location of' or 'could you find location of' or 'can you find the location of' or 'could you find the location of'


wiki_var = 'wikipedia' or 'tell me about' or 'who is' or 'information on' or 'info on' or 'details on' or 'what is' or 'could you tell me about' or 'can you tell me about' or 'could you please tell me about' or 'can you please tell me about'


changeVoice_var = 'change your voice' or 'change voice' or 'switch voice' or 'change to another voice' or 'switch to another voice' or 'change your tone' or 'change tone' or 'switch tone' or 'change to another tone' or 'switch to another tone'


vscode_var = 'open vs code' or 'open visual studio code' or 'start vs code' or 'start visual studio code' or 'launch vs code' or 'launch visual studio code' or 'can you open vs code' or 'could you open vs code' or 'can you open visual studio code' or 'could you open visual studio code' or 'can you start vs code' or 'could you start vs code' or 'can you start visual studio code' or 'could you start visual studio code' or 'can you launch vs code' or 'could you launch vs code' or 'can you launch visual studio code' or 'could you launch visual studio code' or 'run vs code' or 'run visual studio code' or 'start visual studio code'


tempFiles_var = 'delete temporary files' or 'delete temp files' or 'clear temporary files' or 'clear temp files' or 'remove temporary files' or 'remove temp files' or 'delete all temporary files' or 'delete all temp files' or 'clear all temporary files' or 'clear all temp files' or 'remove all temporary files' or 'remove all temp files'


recycleBin_var = 'empty recycle bin' or 'clear recycle bin' or 'delete recycle bin' or 'empty the recycle bin' or 'clear the recycle bin' or 'delete the recycle bin' or 'empty my recycle bin' or 'clear my recycle bin' or 'delete my recycle bin'


sleep_var = 'sleep' or 'go away' or "don't disturb" or 'rest' or 'nap' or 'wait' or 'wait for sometime' or 'wait for some time' or 'wait for a while' or 'keep quiet' or 'be quiet' or 'hold on' or 'just wait'


exit_var = 'exit' or 'quit' or 'terminate' or 'leave' or 'end' or 'stop' or 'break' or 'close' or 'discontinue' or 'shutdown' or 'shut down' or 'abort' or 'hang up' or 'log off' or 'logoff' or 'sign out' or 'signout' or 'goodbye' or 'bye' or 'see you later' or 'see ya later' or 'see you' or 'see ya'

# =========================================================
""" EVERYTHING STARTS HERE! """

if __name__ == '__main__':
    PlaySound(system_ready_sfx, SND_ASYNC)
    PlaySound(wish_me_sfx, SND_ASYNC)
    pyautogui.sleep(1)
    wishMe() # Calling the function to wish the user

    while True:
        query = takeCommand().lower()  # Takes the voice command as USER's "QUERY"

        # Greetings and Basic Communication ===========================================================

        if how_are_you_var in query:
            print("Doing great! Please tell me how may I help you?")
            speak("Doing great! Please tell me how may I help you?")

        elif your_day_var in query:
            print("It's been a good day so far, thanks for asking!")
            speak("It's been a good day so far, thanks for asking!")

        elif capabilities_var in query:
            print("I can do a lot of things, like opening apps, sites, searching online, telling you the weather reports, sending emails, and much more!")
            speak("I can do a lot of things, like opening apps, sites, searching online, telling you the weather reports, sending emails, and much more!")
			print("Just say 'help me' or 'I  need help' if you need any help from me or repeat this later in future!")
			speak("Just say 'help me' or 'I  need help' if you need any help from me or repeat this later in future!")

        elif thankyou_var in query:
            print("It's my pleasure to help you!")
            speak("It's my pleasure to help you!")

        # EXTRAS ===========================================================

        elif send_email_var in query:
            print("Whome should I send the email to?")
            speak("Whome should I send the email to?")
            to_person = takeCommand().lower()

            if 'dad' in to_person:
                print("What do you want me to write in the SUBJECT FILED?")
                speak("What do you want me to write in the SUBJECT FILED?")
				mail_dad = "dad@example.com" # Respective Email IDs should be written here
                mail_sub = takeCommand().title()
                print("What do you want me to write in the Email?")
                speak("What do you want me to write in the Email?")
                mail_content = takeCommand()
                Email(mail_dad, mail_content, mail_sub)

            elif 'mom' in to_person:
                print("What do you want me to write in the SUBJECT FILED?")
                speak("What do you want me to write in the SUBJECT FILED?")
				mail_mom = "mom@example.com"
                mail_sub = takeCommand().title()
                print("What do you want me to write in the Email?")
                speak("What do you want me to write in the Email?")
                mail_content = takeCommand()
                Email(mail_mom, mail_content, mail_sub)

            elif 'myself' in to_person:
                print("What do you want me to write in the SUBJECT FILED?")
                speak("What do you want me to write in the SUBJECT FILED?")
				mail_myself = "me@gmail.com"
                mail_sub = takeCommand().title()
                print("What do you want me to write in the Email?")
                speak("What do you want me to write in the Email?")
                mail_content = takeCommand()
                Email(mail_myself, mail_content, mail_sub)

        elif movie_var in query:
            playMovie()

        elif weather_var in query:
            print("Opening up today's Weather Reports..!")
            speak("Opening up today's Weather Reports")
            webbrowser.open_new_tab('https://www.google.com/search?q=weather+reports+now')

        elif time_var in query:
            h = datetime.datetime.now().hour
            m = datetime.datetime.now().minute
            print(f"The time is {h}:{m}")
            speak(f"The time is {h} {m}")

        elif calculator_var in query:
            print("Opening Calculator...")
            speak("Opening Calculator")
            pyautogui.hotkey('win', 's')
            pyautogui.write('calculator')
            pyautogui.press('enter')
            print("You can start your calculation, I will sleep for 2 minutes.")
            speak("You can start your calculation, I will sleep for 2 minutes")
            pyautogui.sleep(120)

        # YOUTUBE CHANNELS =================================================

        elif ('mister beast' in query) or ('mr beast' in query):
            print("Opening Mr Beast's YouTube channel...")
            speak("Opening Mister Beast's YouTube channel")
            webbrowser.open('https://www.youtube.com/user/MrBeast6000')
        
        elif ('carryminati' in query) or ('minati' in query):
            print("Opening CarryMinati's YouTube channel...")
            speak("Opening CarryMinati's YouTube channel")
            webbrowser.open('https://www.youtube.com/c/CarryMinati')

        elif ('ashish chanchlani' in query) or ('chanchlani' in query):
            print("Opening Ashish Chanchlani's YouTube channel...")
            speak("Opening Ashish Chanchlani's YouTube channel")
            webbrowser.open('https://www.youtube.com/c/AshishChanchlaniVines')

		"""
		TEMPLATE TO CREATE MORE SUCH YOUTUBE LINKS
  
		elif ('NAME' in query):
			print("Opening NAME's YouTube channel...")
            speak("Opening NAME's YouTube channel")
            webbrowser.open('https://www.youtube.com/c/LINK')
		"""
        
        # ONLINE SEARCH =========================================================

        elif search_var in query:
            search()

        elif location_var in query:
            try:
                location = query.replace("where is", '') # Searches the location asked in the query
                location = query.replace("could you find the location of", '')
                location = query.replace("can you find the location of", '')
                location = query.replace("could you find location of", '')
                location = query.replace("can you find location of", '')
                location = query.replace("could you please locate", '')
                location = query.replace("find the location of", '')
                location = query.replace("find location of", '')
                location = query.replace("can you locate", '')
                location = query.replace("find where is", '')
                location = query.replace("find where's", '')
                location = query.replace("location of", '')
                location = query.replace("where's", '')
                location = query.replace("locate", '')

                webbrowser.open(f"https://www.google.com/maps/place/{location}")
                print(f"Opening Google Maps and checking about {location}...")
                speak(f"Opening Google Maps and checking about {location}")
            except Exception:
                print(f"There was some problem in searching for {location}.")
                speak(f"There was some problem in searching for {location}.")

        elif wiki_var in query:
            print("What should I search on Wikipedia?")
            speak("What should I search on Wikipedia?")
            wiki_req = takeCommand().lower()
            
            print("Searching on Wikipedia...")
            speak("Searching on Wikipedia")

            wiki_req = wiki_req.replace("could you please tell me about", "")
            wiki_req = wiki_req.replace("can you please tell me about", "")
            wiki_req = wiki_req.replace("could you tell me about", "")
            wiki_req = wiki_req.replace("can you tell me about", "")
            wiki_req = wiki_req.replace("could you look please", "")
            wiki_req = wiki_req.replace("search wikipedia", "")
            wiki_req = wiki_req.replace("could you please", "")
            wiki_req = wiki_req.replace("please look for", "")
            wiki_req = wiki_req.replace("wikipedia about", "")
            wiki_req = wiki_req.replace("information on", "")
            wiki_req = wiki_req.replace("tell me about", "")
            wiki_req = wiki_req.replace("search that", "")
            wiki_req = wiki_req.replace("search for", "")
            wiki_req = wiki_req.replace("details on", "")
            wiki_req = wiki_req.replace("search on", "")
            wiki_req = wiki_req.replace("wikipedia", "")
            wiki_req = wiki_req.replace("look for", "")
            wiki_req = wiki_req.replace("where is", "")
            wiki_req = wiki_req.replace("what is", "")
            wiki_req = wiki_req.replace("info on", "")
            wiki_req = wiki_req.replace("who is", "")
            
            print(f"Searching Wikipedia about {wiki_req}...")
            speak(f"Searching Wikipedia about {wiki_req}")
			# Searches the query on Wikipedia and prints 3 sentences (change the int value to get the desired number of sentences)
            results = wikipedia.summary(wiki_req, sentences=3)
            print(f"According to Wikipedia,\n{results}")
            speak(f"According to Wikipedia,\n{results}")

        # CHANGE VOICE =====================================================
        elif changeVoice_var in query:
            print("Changing voice...")
            speak("Changing voice")
            if bot_voice == 1: # Zira to David
                bot_voice = 0
                engine.setProperty('voice', voices[bot_voice].id)
                print("Voice Changed to DAVID")
                speak("Voice Changed to DAVID")
            elif bot_voice == 0: # David to Zira
                bot_voice = 1
                engine.setProperty('voice', voices[bot_voice].id)
                print("Voice changed to ZIRA")
                speak("Voice changed to ZIRA")

        # OPENING APPS & SITES ======================================================

		elif ('open youtube' in query) or ('open youtube.com' in query) or ('open youtube dot com' in query):
            webbrowser.open('https://www.youtube.com') # Links can be attached to open the Site
            print("Opening YouTube...")
            speak("Opening YouTube")

        elif 'open discord' in query:
            discord_path = "PATH\\TO\\DISCORD\\Discord.exe"
            os.startfile(discord_path) # App Path can be attached to open the app
            print("Opening Discord...")
            speak("Opening Discord")

        elif vscode_var in query:
            pyautogui.hotkey('win', '9') # Pinned Position of the App on the Taskbar can also be used to open any app
            print("Opening Visual Studio Code...")
            speak("Opening Visual Studio Code")

        elif ('open whatsapp' in query) or ('open whats app' in query) or ("open what's app" in query):
            pyautogui.hotkey('win', '2') # "2" means the position of WhatsApp on the taskbar is 2
            print("Opening Whatsapp...")
            speak("Opening Whatsapp...")

        elif ('open amazon' in query) or ('amazon.in' in query) or ('amazon dot in' in query):
            webbrowser.open("https://www.amazon.in")
            print("Opening Amazon...")
            speak("Opening Amazon")

        elif 'open instagram' in query:
            webbrowser.open('https://www.instagram.com')
            print("Opening Instagram...")
            speak("Opening Instagram")

        elif ('open settings' in query) or ('open setting' in query):
            pyautogui.hotkey('win', 'i')
            print("Opening System Settings...") 
            speak("Opening System Settings")

        elif ('open brave browser' in query) or ('open brave' in query):
            brave_path = "PATH\\TO\\BRAVE\\brave.exe"
            webbrowser.open_new_tab(brave_path)
            print("Opening Brave Browser...")
            speak("Opening Brave Browser")

        elif ('open drive' in query) or ('open google drive' in query):
            print("Opening Google Drive...")
            speak("Opening Google Drive")
            webbrowser.open("https://drive.google.com")
        
        elif ('open gmail' in query) or ('open google mail' in query) or ('open g mail' in query):
            print("Opening Gmail...")
            speak("Opening Gmail")
            webbrowser.open("https://mail.google.com")

        elif 'open chrome' in query:
            chrome_path = "PATH\\TO\CHROME\\chrome.exe"
            webbrowser.open_new_tab(chrome_path)
            print("Opening Chrome...")
            speak("Opening Chrome")

        # MUSIC ============================================================
        elif 'open spotify' in query:
            spotify_path = "PATH\\TO\\SPOTIFY\\Spotify.exe"
            os.startfile(spotify_path)
            print("Opening Spotify...")
            speak("Opening Spotify")

            print("Should I play any of your playlists?")
            speak("Should I play any of your playlists?")
            decision = takeCommand().lower()
            if 'yes' in decision:
                print("Then which playlist would you like me to play?")
                speak("Then which playlist would you like me to play?")
                playlistName = takeCommand().lower()

                if 'playlist 1' in playlistName:
                    print("Playing PLAYLIST-1")
                    speak("Playing PLAYLIST-1")
                    webbrowser.open("https://open.spotify.com/playlist/LINK-TO-PLAYLIST-1")
					print("Terminating now, Goodbye!")
                	speak("Terminating now, Goodbye!")
                    break

                elif 'playlist 2' in playlistName:
                    print("Playing PLAYLIST-2")
                    speak("Playing PLAYLIST-2")
                    webbrowser.open("https://open.spotify.com/playlist/LINK-TO-PLAYLIST-2")
                    print("Terminating now, Goodbye!")
                	speak("Terminating now, Goodbye!")
                    break

                elif 'playlist 3' in playlistName:
                    print("Playing PLAYLIST-3")
                    speak("Playing PLAYLIST-3")
                    webbrowser.open("https://open.spotify.com/playlist/LINK-TO-PLAYLIST-3")
                    print("Terminating now, Goodbye!")
                	speak("Terminating now, Goodbye!")
                    break

            elif 'no' in decision:
                print("Okay, will continue with the last song playing!")
                speak("Okay, will continue with the last song playing!")
                print("Also, Should I TERMINATE ?")
                speak("Also, Should I Terminate?")
                yes_no = takeCommand().lower()
                if ('yes' in yes_no) or ('sure' in yes_no):
                    print("Sure! Goodbye.")
                    speak("Sure! Goodbye.")
					pyautogui.press('space')
                    break

                elif 'no' in yes_no:
                    print("Sure!")
                    speak("Sure!")

        # DELETING TEMP FILES =======================================================
        elif tempFiles_var in query:
            print("Deleting all the Temporary Files...")
            speak("Deleting all the Temporary Files...")
			# Takes control of your mouse and keyboard and deletes the temporary files

            # ------------ %temp% files --------------
            pyautogui.sleep(2)
            pyautogui.hotkey('win', 'r')
            pyautogui.write("%temp%", 0.1)
            pyautogui.sleep(2)
            pyautogui.press('enter')
            pyautogui.sleep(3)
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.press('delete')
            pyautogui.sleep(3)
            pyautogui.press('up')
            pyautogui.press('enter')
            pyautogui.press('down')
            pyautogui.press('right')
            pyautogui.press('enter')
            pyautogui.sleep(2)
            pyautogui.hotkey('ctrl', 'w')

            pyautogui.sleep(2)

            # ------------ Temp files --------------
            pyautogui.hotkey('win', 'r')
            pyautogui.write("Temp", 0.1)
            pyautogui.sleep(2)
            pyautogui.press('enter')
            pyautogui.sleep(3)
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.press('delete')
            pyautogui.sleep(3)
            pyautogui.press('up')
            pyautogui.press('enter')
            pyautogui.press('down')
            pyautogui.press('right')
            pyautogui.press('enter')
            pyautogui.sleep(2)
            pyautogui.hotkey('ctrl', 'w')

        elif recycleBin_var in query:
            print("Emptying Recycle Bin from your Computer...")
            speak("Emptying Recycle Bin from your Computer")
            pyautogui.hotkey('win', 'd')
            pyautogui.sleep(1)
            pyautogui.write('recy', 0.1)
            pyautogui.press('enter')
            pyautogui.sleep(2)
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.press('delete')
            pyautogui.press('enter')
            pyautogui.sleep(3)
            pyautogui.hotkey('ctrl', 'w')
            pyautogui.hotkey('alt', 'tab')

        # EXIT & SLEEP =============================================================
        elif sleep_var in query:
            try:
                print("Okay, how many seconds shall I sleep for?")
                speak("Okay, how many seconds shall I sleep for?")
                s_time = takeCommand().lower()
                sec = int(s_time.replace('seconds', ''))
                sec = int(s_time.replace('second', ''))
                print(f"Going to sleep for {sec} seconds.")
                speak(f"Going to sleep for {sec} seconds.")
                pyautogui.sleep(sec)
            except Exception as e:
                print("Couldn't get what you said.")
                speak("Couldn't get what you said.")
                print("Please repeat the Command")
                speak("Please repeat the Command")
        
        elif exit_var in query:
            print("Okay, I am TERMINATING now. Run the code again if you ever need some assistance. Goodbye!")
            speak("Okay, I am TERMINATING now. Run the code again if you ever need some assistance. Goodbye!")
            PlaySound(exit_sfx, SND_ASYNC)
            break

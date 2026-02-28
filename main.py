import webbrowser
import datetime
import wikipedia
from voice_engine import speak, listen
from ai_brain import ask_ai
from cyber_tools import check_password_strength
from config import WAKE_WORD
# adding section
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
#end section adding


speak("Hello Ashutosh. Your AI Voice Assistant is ready.")
driver = None
while True:
    command = listen()
    command = command.lower().strip()

    if not command:
        continue

    print("DEBUG Command:", command)

    # Wake word detection
    if WAKE_WORD in command:
        speak("Yes, I am listening.")

        command = listen()
        command = command.lower().strip()

        if not command:
            continue

        print("DEBUG After Wake:", command)

        # ================= GOOGLE =================
        if "google" in command:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")

        # ================= YOUTUBE =================
      
        elif "youtube" in command or "play" in command:

            # ---------------- PLAY MUSIC ----------------
            if "play" in command:

                search_query = command.replace("play", "").replace("on youtube", "").replace("youtube", "").strip()

                if not search_query:
                    search_query = "music"

                speak(f"Playing {search_query} on YouTube")

                if driver is None:
                    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

                driver.get("https://www.youtube.com")
                time.sleep(3)

                search_box = driver.find_element(By.NAME, "search_query")
                search_box.clear()
                search_box.send_keys(search_query)
                search_box.send_keys(Keys.RETURN)

                time.sleep(3)

                video = driver.find_element(By.ID, "video-title")
                video.click()

            # ---------------- PAUSE ----------------
            elif "pause" in command:
                if driver:
                    driver.find_element(By.TAG_NAME, "body").send_keys("k")
                    speak("Paused")

            # ---------------- RESUME ----------------
            elif "resume" in command:
                if driver:
                    driver.find_element(By.TAG_NAME, "body").send_keys("k")
                    speak("Resuming")

            # ---------------- NEXT VIDEO ----------------
            elif "next" in command:
                if driver:
                    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.SHIFT, "n")
                    speak("Playing next video")

            # ---------------- VOLUME UP ----------------
            elif "volume up" in command:
                if driver:
                    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ARROW_UP)
                    speak("Volume increased")

            # ---------------- VOLUME DOWN ----------------
            elif "volume down" in command:
                if driver:
                    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ARROW_DOWN)
                    speak("Volume decreased")

            else:
                speak("Opening YouTube")
                webbrowser.open("https://www.youtube.com")
       
        

        # ================= TIME =================
        elif "time" in command:
            time = datetime.datetime.now().strftime("%H:%M")
            speak(f"The time is {time}")

        # ================= DATE =================
        elif "date" in command:
            date = datetime.datetime.now().strftime("%d %B %Y")
            speak(f"Today's date is {date}")

        # ================= WIKIPEDIA =================
        elif "wikipedia" in command:
            topic = command.replace("wikipedia", "").strip()
            try:
                result = wikipedia.summary(topic, sentences=2)
                speak(result)
            except:
                speak("Sorry, I couldn't find anything on Wikipedia.")

        # ================= PASSWORD CHECK =================
        elif "check password" in command:
            speak("Please say the password.")
            pwd = listen()
            strength = check_password_strength(pwd)
            speak(strength)

        # ================= EXIT =================
        elif "stop" in command or "exit" in command:
            speak("Goodbye Ashutosh.")
            break

        # ================= AI RESPONSE =================
        else:
            speak("Let me think.")
            response = ask_ai(command)
            speak(response)
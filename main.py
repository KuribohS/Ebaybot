from selenium import webdriver
from selenium_stealth import stealth
from time import sleep
import pydub
import urllib
import speech_recognition
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os
from fake_useragent import UserAgent
import time,requests
import warnings
from selenium.webdriver import ActionChains

warnings.filterwarnings("ignore", category=DeprecationWarning) 

picture = "/sdrive/Files/Pics/IMG_2029.PNG"
PATH = '/home/daniel/files/Programming /python/Ebaybot/chromedriver'

data_path = os.path.abspath(os.getcwd())
ua = UserAgent(cache=False)
userAgent = ua.random
print(userAgent)
delayTime = 2
audioToTextDelay = 10
filename = '1.mp3'

googleIBMLink = 'https://speech-to-text-demo.ng.bluemix.net/'
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument(f'user-agent={userAgent}')

class Ebaybot:
    def __init__(self, username, pw):
        self.driver = webdriver.Chrome(executable_path=PATH)
        self.driver.get("https://www.ebay-kleinanzeigen.de")
        stealth(self.driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Google Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )
        sleep(2)
        self.driver.find_element("xpath", '/html/body/div[2]/div/div/div/div/div[3]/button[2]').click()
        sleep(10)
        try:
            self.driver.find_element("xpath","/html/body/div[1]/div[2]/div/div[16]/button[1]").click()
            sleep(10)
        except Exception as e:
                pass

        self.driver.find_element("xpath","/html/body/header/section[1]/section/nav/ul/li[3]/a")\
            .click()
        sleep(5)
        self.driver.find_element("xpath","/html/body/div[1]/div[2]/div/div[1]/form/div[1]/div/div/input")\
            .click()
        sleep(2)
        login_field = self.driver.find_element("xpath","/html/body/div[1]/div[2]/div/div[1]/form/div[1]/div/div/input")\
            .send_keys(username)
        self.driver.find_element("xpath","/html/body/div[1]/div[2]/div/div[1]/form/div[2]/div/div/input")\
            .click()
        pw_field = self.driver.find_element("xpath","/html/body/div[1]/div[2]/div/div[1]/form/div[2]/div/div/input")\
            .send_keys(pw)

        sleep(80)

    def bypass(self):
        def audioToText(mp3Path):
            src = self.driver.find_element_by_id(
                "audio-source"
            ).get_attribute("src")
            urllib.request.urlretrieve(src, data_path + "\\audio.mp3"
            )
            sound = pydub.AudioSegment.from_mp3(
                data_path + "\\audio.mp3"
            ).export(data_path + "\\audio.wav", format="wav")
            recognizer = speech_recognition.Recognizer()
            google_audio = speech_recognition.AudioFile (
                data_path + "\\audio.wav"
            )
            with google_audio as source:
                audio = recognizer.record(source)
            text = recognizer.recognize_google(audio, language='de-DE')
            inputfield = self.driver.find_element_by_id("audio-response")
            inputfield.send_keys(text.lower())
            inputfield.send_keys(Keys.ENTER)
            sleep(5)

        def saveFile(content,filename):
            with open(filename, "wb") as handle:
                for data in content.iter_content():
                    handle.write(data)

        time.sleep(1)
        googleClass = self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[1]/form/div[3]/div/div/div")
        time.sleep(2)
        outeriframe = self.driver.find_element_by_tag_name('iframe')
        time.sleep(1)
        outeriframe.click()
        time.sleep(2)
        allIframesLen = self.driver.find_elements_by_tag_name('iframe')
        time.sleep(1)
        audioBtnFound = False
        audioBtnIndex = -1
        for index in range(len(allIframesLen)):
            self.driver.switch_to.default_content()
            iframe = self.driver.find_elements_by_tag_name('iframe')[index]
            self.driver.switch_to.frame(iframe)
            self.driver.implicitly_wait(delayTime)
            try:
                audioBtn = self.driver.find_element_by_id('recaptcha-audio-button') or self.driver.find_element_by_id('recaptcha-anchor')
                audioBtn.click()
                audioBtnFound = True
                audioBtnIndex = index
                break 
            except Exception as e:
                pass
        if audioBtnFound:
                href = self.driver.find_element_by_id('audio-source').get_attribute('src')
                response = requests.get(href, stream=True)
                saveFile(response,filename)
                audioToText(os.getcwd() + '/' + filename)
                time.sleep(2)
                errorMsg = self.driver.find_elements_by_class_name('rc-audiochallenge-error-message')[0]
                if errorMsg.text == "" or errorMsg.value_of_css_property('display') == 'none':
                    print("Success")
                    sleep(5)
        else:
            print('Button not found. This should not happen.')
        self.driver.switch_to.default_content()
        self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[1]/form/div[4]/div/div/button/span").click()
        sleep(4)

    def createAnzeigeNachhilfeInformatik(self):
        Tryagain = False
        print("Navigiere zur Anzeige creation.")
        self.driver.find_element_by_xpath("/html/body/header/section[2]/div/div/div[2]/nav/ul/li[1]/a").click()
        sleep(5)
        self.driver.find_element_by_xpath("/html/body/div[1]/form/fieldset[1]/div[2]/div[1]/div/div/input").click()
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/form/fieldset[1]/div[2]/div[1]/div/div/input").send_keys("ONLINE Nachhilfe Informatik Klasse 1-13")
        sleep(8)
        self.driver.find_element_by_xpath("/html/body/div[1]/form/fieldset[1]/div[3]/div/div/div/div/input").click()
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/form/fieldset[1]/div[3]/div/div/div/div/input").send_keys("15")
        sleep(8)
        self.driver.find_element_by_xpath("/html/body/div[1]/form/fieldset[1]/div[4]/div/div/div/textarea").click()
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/form/fieldset[1]/div[4]/div/div/div/textarea").send_keys("Guten Tag,", Keys.ENTER , Keys.ENTER, "Ich heiße Daniel und bin angehender Informatikstudent. Ich arbeite schon seit 3 Jahren als Nachhilfe Lehrer im Privatenraum. Ich möchte nun mein Wissen mit mehr Menschen teilen und mehr Schüler für das Fach Informatik begeistern und denen weiterhelfen.", Keys.ENTER, "Ich war Kurs bester im Leistungskurs Informatik. Ich habe mein Wissen auch in eigenen kleinen Projekten widergespiegelt. Mit HTML, CSS und Javascript habe ich eine eigene Webseite erstellt, auf der Sie sich meine Fähigkeiten noch einmal genauer anschauen können.", Keys.ENTER,Keys.ENTER, "Meine Webseite: Kuriboh.dev", Keys.ENTER,Keys.ENTER, "Preise:", Keys.ENTER, "45 Minuten: 15€", Keys.ENTER, "60 Minuten: 18€",Keys.ENTER,Keys.ENTER, "Individuelle Lernvideos für das Fach Informatik können zum Unterricht extra erworben werden: 15€")
        sleep(8)
        path = picture
        print("Upload")
        self.driver.find_element_by_xpath("//input[@type='file']").send_keys(path)
        sleep(6)
        print("Kinda broke")
        self.driver.find_element_by_xpath("//input[@type='file']").send_keys(path)
        sleep(4)
        print("Kinda broke")
        self.driver.find_element_by_xpath("//input[@type='file']").send_keys(path)
        sleep(64)
        print("Kinda broke")


        #Check for iframe
        try:
            def audioToText(mp3Path):
                src = self.driver.find_element_by_id(
                    "audio-source"
                ).get_attribute("src")
                urllib.request.urlretrieve(src, data_path + "\\audio.mp3"
                )
                sound = pydub.AudioSegment.from_mp3(
                    data_path + "\\audio.mp3"
                ).export(data_path + "\\audio.wav", format="wav")
                recognizer = speech_recognition.Recognizer()
                google_audio = speech_recognition.AudioFile (
                    data_path + "\\audio.wav"
                )
                with google_audio as source:
                    audio = recognizer.record(source)
                text = recognizer.recognize_google(audio, language='de-DE')
                inputfield = self.driver.find_element_by_id("audio-response")
                inputfield.send_keys(text.lower())
                inputfield.send_keys(Keys.ENTER)
                sleep(5)

            def saveFile(content,filename):
                with open(filename, "wb") as handle:
                    for data in content.iter_content():
                        handle.write(data)

            googleClass = self.driver.find_element_by_xpath("/html/body/div[1]/form/fieldset[6]/div[2]/div")
            time.sleep(2)
            outeriframe = self.driver.find_element_by_tag_name('iframe')
            time.sleep(1)
            outeriframe.click()
            time.sleep(2)
            allIframesLen = self.driver.find_elements_by_tag_name('iframe')
            time.sleep(1)
            audioBtnFound = False
            audioBtnIndex = -1
            for index in range(len(allIframesLen)):
                self.driver.switch_to.default_content()
                iframe = self.driver.find_elements_by_tag_name('iframe')[index]
                self.driver.switch_to.frame(iframe)
                self.driver.implicitly_wait(delayTime)
                try:
                    audioBtn = self.driver.find_element_by_id('recaptcha-audio-button') or self.driver.find_element_by_id('recaptcha-anchor')
                    audioBtn.click()
                    audioBtnFound = True
                    audioBtnIndex = index
                    break 
                except Exception as e:
                    pass
            if audioBtnFound:
                    href = self.driver.find_element_by_id('audio-source').get_attribute('src')
                    response = requests.get(href, stream=True)
                    saveFile(response,filename)
                    audioToText(os.getcwd() + '/' + filename)
                    time.sleep(2)
                    errorMsg = self.driver.find_elements_by_class_name('rc-audiochallenge-error-message')[0]
                    if errorMsg.text == "" or errorMsg.value_of_css_property('display') == 'none':
                        print("Success")
                        sleep(5)
            else:
                print('Button not found. This should not happen.')
        except:
            print("no Iframe")

        self.driver.find_element_by_xpath("/html/body/div[1]/form/fieldset[6]/div[2]/div[1]").click()
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div/div[2]").click()
        sleep(5)
        sleep(60)

    def createAnzeigeNachhilfeEnglisch(self):
        Tryagain = False
        print("Navigiere zur Anzeige creation.")
        self.driver.find_element_by_xpath("/html/body/header/section[2]/div/div/div[2]/nav/ul/li[1]/a").click()
        sleep(5)
        self.driver.find_element_by_xpath("/html/body/div[1]/form/fieldset[1]/div[2]/div[1]/div/div/input").click()
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/form/fieldset[1]/div[2]/div[1]/div/div/input").send_keys("ONLINE Nachhilfe Englisch Klasse 1-13")
        sleep(8)
        self.driver.find_element_by_xpath("/html/body/div[1]/form/fieldset[1]/div[3]/div/div/div/div/input").click()
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/form/fieldset[1]/div[3]/div/div/div/div/input").send_keys("15")
        sleep(8)
        self.driver.find_element_by_xpath("/html/body/div[1]/form/fieldset[1]/div[4]/div/div/div/textarea").click()
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/form/fieldset[1]/div[4]/div/div/div/textarea").send_keys("Guten Tag,", Keys.ENTER , Keys.ENTER, "Ich heiße Daniel und bin angehender Informatikstudent. Ich arbeite schon seit 3 Jahren als Nachhilfe Lehrer im Privatenraum. Ich möchte nun mein Wissen mit mehr Menschen teilen und mehr Schüler für das Fach Englisch begeistern und denen weiterhelfen.", Keys.ENTER, "Ich war Kurs bester im Leistungskurs Englisch. Ich habe mein Wissen auch in eigenen kleinen Projekten widergespiegelt. Mit HTML, CSS und Javascript habe ich eine eigene Webseite erstellt, auf der Sie sich meine Fähigkeiten noch einmal genauer anschauen können.", Keys.ENTER,Keys.ENTER, "Meine Webseite: Kuriboh.dev", Keys.ENTER,Keys.ENTER, "Preise:", Keys.ENTER, "45 Minuten: 15€", Keys.ENTER, "60 Minuten: 18€",Keys.ENTER,Keys.ENTER)
        sleep(8)
        path = picture
        print("Upload")
        self.driver.find_element_by_xpath("//input[@type='file']").send_keys(path)
        sleep(6)
        print("Kinda broke")
        self.driver.find_element_by_xpath("//input[@type='file']").send_keys(path)
        sleep(4)
        print("Kinda broke")
        self.driver.find_element_by_xpath("//input[@type='file']").send_keys(path)
        sleep(60)
        print("Kinda broke")

    

        #Check for iframe
        try:
            def audioToText(mp3Path):
                src = self.driver.find_element_by_id(
                    "audio-source"
                ).get_attribute("src")
                urllib.request.urlretrieve(src, data_path + "\\audio.mp3"
                )
                sound = pydub.AudioSegment.from_mp3(
                    data_path + "\\audio.mp3"
                ).export(data_path + "\\audio.wav", format="wav")
                recognizer = speech_recognition.Recognizer()
                google_audio = speech_recognition.AudioFile (
                    data_path + "\\audio.wav"
                )
                with google_audio as source:
                    audio = recognizer.record(source)
                text = recognizer.recognize_google(audio, language='de-DE')
                inputfield = self.driver.find_element_by_id("audio-response")
                inputfield.send_keys(text.lower())
                inputfield.send_keys(Keys.ENTER)
                sleep(5)

            def saveFile(content,filename):
                with open(filename, "wb") as handle:
                    for data in content.iter_content():
                        handle.write(data)

            googleClass = self.driver.find_element_by_xpath("/html/body/div[1]/form/fieldset[6]/div[2]/div")
            time.sleep(2)
            outeriframe = self.driver.find_element_by_tag_name('iframe')
            time.sleep(1)
            outeriframe.click()
            time.sleep(2)
            allIframesLen = self.driver.find_elements_by_tag_name('iframe')
            time.sleep(1)
            audioBtnFound = False
            audioBtnIndex = -1
            for index in range(len(allIframesLen)):
                self.driver.switch_to.default_content()
                iframe = self.driver.find_elements_by_tag_name('iframe')[index]
                self.driver.switch_to.frame(iframe)
                self.driver.implicitly_wait(delayTime)
                try:
                    audioBtn = self.driver.find_element_by_id('recaptcha-audio-button') or self.driver.find_element_by_id('recaptcha-anchor')
                    audioBtn.click()
                    audioBtnFound = True
                    audioBtnIndex = index
                    break 
                except Exception as e:
                    pass
            if audioBtnFound:
                    href = self.driver.find_element_by_id('audio-source').get_attribute('src')
                    response = requests.get(href, stream=True)
                    saveFile(response,filename)
                    audioToText(os.getcwd() + '/' + filename)
                    time.sleep(2)
                    errorMsg = self.driver.find_elements_by_class_name('rc-audiochallenge-error-message')[0]
                    if errorMsg.text == "" or errorMsg.value_of_css_property('display') == 'none':
                        print("Success")
                        sleep(5)
            else:
                print('Button not found. This should not happen.')
        except:
            print("no Iframe")

        self.driver.find_element_by_xpath("/html/body/div[1]/form/fieldset[6]/div[2]/div[1]").click()
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div/div[2]").click()
        sleep(60)

    def createAnzeigeNachhilfeMathe(self):
        Tryagain = False
        print("Navigiere zur Anzeige creation.")
        self.driver.find_element_by_xpath("/html/body/header/section[2]/div/div/div[2]/nav/ul/li[1]/a").click()
        sleep(5)
        self.driver.find_element_by_xpath("/html/body/div[1]/form/fieldset[1]/div[2]/div[1]/div/div/input").click()
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/form/fieldset[1]/div[2]/div[1]/div/div/input").send_keys("ONLINE Nachhilfe Mathe Klasse 1-13")
        sleep(8)
        self.driver.find_element_by_xpath("/html/body/div[1]/form/fieldset[1]/div[3]/div/div/div/div/input").click()
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/form/fieldset[1]/div[3]/div/div/div/div/input").send_keys("15")
        sleep(8)
        self.driver.find_element_by_xpath("/html/body/div[1]/form/fieldset[1]/div[4]/div/div/div/textarea").click()
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/form/fieldset[1]/div[4]/div/div/div/textarea").send_keys("Guten Tag,", Keys.ENTER , Keys.ENTER, "Ich heiße Daniel und bin angehender Informatikstudent. Ich arbeite schon seit 3 Jahren als Nachhilfe Lehrer im Privatenraum. Ich möchte nun mein Wissen mit mehr Menschen teilen und mehr Schüler für das Fach Mathe begeistern und denen weiterhelfen.", Keys.ENTER, "Ich war Kurs bester in Mathe und habe ebenfalls erfolgreich meine Mündliche Prüfung in diesem Fach bestanden. Ich habe mein Wissen auch in eigenen kleinen Projekten widergespiegelt. Mit HTML, CSS und Javascript habe ich eine eigene Webseite erstellt, auf der Sie sich meine Fähigkeiten noch einmal genauer anschauen können.", Keys.ENTER,Keys.ENTER, "Meine Webseite: Kuriboh.dev", Keys.ENTER,Keys.ENTER, "Preise:", Keys.ENTER, "45 Minuten: 15€", Keys.ENTER, "60 Minuten: 18€",Keys.ENTER,Keys.ENTER)
        sleep(8)
        path = picture
        print("Upload")
        self.driver.find_element_by_xpath("//input[@type='file']").send_keys(path)
        sleep(6)
        print("Kinda broke")
        self.driver.find_element_by_xpath("//input[@type='file']").send_keys(path)
        sleep(4)
        print("Kinda broke")
        self.driver.find_element_by_xpath("//input[@type='file']").send_keys(path)
        sleep(60)
        print("Kinda broke")
 

        #Check for iframe
        try:
            def audioToText(mp3Path):
                src = self.driver.find_element_by_id(
                    "audio-source"
                ).get_attribute("src")
                urllib.request.urlretrieve(src, data_path + "\\audio.mp3"
                )
                sound = pydub.AudioSegment.from_mp3(
                    data_path + "\\audio.mp3"
                ).export(data_path + "\\audio.wav", format="wav")
                recognizer = speech_recognition.Recognizer()
                google_audio = speech_recognition.AudioFile (
                    data_path + "\\audio.wav"
                )
                with google_audio as source:
                    audio = recognizer.record(source)
                text = recognizer.recognize_google(audio, language='de-DE')
                inputfield = self.driver.find_element_by_id("audio-response")
                inputfield.send_keys(text.lower())
                inputfield.send_keys(Keys.ENTER)
                sleep(5)

            def saveFile(content,filename):
                with open(filename, "wb") as handle:
                    for data in content.iter_content():
                        handle.write(data)

            googleClass = self.driver.find_element_by_xpath("/html/body/div[1]/form/fieldset[6]/div[2]/div")
            time.sleep(2)
            outeriframe = self.driver.find_element_by_tag_name('iframe')
            time.sleep(1)
            outeriframe.click()
            time.sleep(2)
            allIframesLen = self.driver.find_elements_by_tag_name('iframe')
            time.sleep(1)
            audioBtnFound = False
            audioBtnIndex = -1
            for index in range(len(allIframesLen)):
                self.driver.switch_to.default_content()
                iframe = self.driver.find_elements_by_tag_name('iframe')[index]
                self.driver.switch_to.frame(iframe)
                self.driver.implicitly_wait(delayTime)
                try:
                    audioBtn = self.driver.find_element_by_id('recaptcha-audio-button') or self.driver.find_element_by_id('recaptcha-anchor')
                    audioBtn.click()
                    audioBtnFound = True
                    audioBtnIndex = index
                    break 
                except Exception as e:
                    pass
            if audioBtnFound:
                    href = self.driver.find_element_by_id('audio-source').get_attribute('src')
                    response = requests.get(href, stream=True)
                    saveFile(response,filename)
                    audioToText(os.getcwd() + '/' + filename)
                    time.sleep(2)
                    errorMsg = self.driver.find_elements_by_class_name('rc-audiochallenge-error-message')[0]
                    if errorMsg.text == "" or errorMsg.value_of_css_property('display') == 'none':
                        print("Success")
                        sleep(5)
            else:
                print('Button not found. This should not happen.')
        except:
            print("no Iframe")

        self.driver.find_element_by_xpath("/html/body/div[1]/form/fieldset[6]/div[2]/div[1]").click()
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div/div[2]").click()
        sleep(60)

    def createAnzeigeApp(self):
        Tryagain = False
        print("Navigiere zur Anzeige creation.")
        self.driver.find_element_by_xpath("/html/body/header/section[2]/div/div/div[2]/nav/ul/li[1]/a").click()
        sleep(5)
        self.driver.find_element_by_xpath("/html/body/div[1]/form/fieldset[1]/div[2]/div[1]/div/div/input").click()
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/form/fieldset[1]/div[2]/div[1]/div/div/input").send_keys("App Entwicklung ich bin ein Programmierer / Entwickler")
        sleep(8)
        self.driver.find_element_by_xpath("/html/body/div[1]/form/fieldset[1]/div[3]/div/div/div/div/input").click()
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/form/fieldset[1]/div[3]/div/div/div/div/input").send_keys("200")
        sleep(8)
        self.driver.find_element_by_xpath("/html/body/div[1]/form/fieldset[1]/div[4]/div/div/div/textarea").click()
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/form/fieldset[1]/div[4]/div/div/div/textarea").send_keys("Guten Tag,", Keys.ENTER , Keys.ENTER, "Ich heiße Daniel und studiere zurzeit Informatik. In meiner Freizeit programmiere ich viele Applikationen, ob für Handys, Rechner oder Server. Nun will ich auch Ihnen helfen eine eigene App zu erstellen. Melden Sie sich bei mir mit Ihrer App Idee und ich melde mich so schnell wie möglich bei Ihnen.", Keys.ENTER, "Ich programmiere hauptsächlich Android Nativ, aufgrund dessen würde eine Android App schneller bereit sein. Bei Nachfrage wäre es für mich aber ebenfalls möglich Cross-Platform zu programmieren.", Keys.ENTER,Keys.ENTER, "Da ich kein IOS Gerät besitze werden alle IOS-Tests in einem Emulator durchgeführt.")
        sleep(8)
        path = picture
        print("Upload")
        self.driver.find_element_by_xpath("//input[@type='file']").send_keys(path)
        sleep(6)
        print("Kinda broke")
        self.driver.find_element_by_xpath("//input[@type='file']").send_keys(path)
        sleep(4)
        print("Kinda broke")
        self.driver.find_element_by_xpath("//input[@type='file']").send_keys(path)
        sleep(60)
        print("Kinda broke")
 

        #Check for iframe
        try:
            def audioToText(mp3Path):
                src = self.driver.find_element_by_id(
                    "audio-source"
                ).get_attribute("src")
                urllib.request.urlretrieve(src, data_path + "\\audio.mp3"
                )
                sound = pydub.AudioSegment.from_mp3(
                    data_path + "\\audio.mp3"
                ).export(data_path + "\\audio.wav", format="wav")
                recognizer = speech_recognition.Recognizer()
                google_audio = speech_recognition.AudioFile (
                    data_path + "\\audio.wav"
                )
                with google_audio as source:
                    audio = recognizer.record(source)
                text = recognizer.recognize_google(audio, language='de-DE')
                inputfield = self.driver.find_element_by_id("audio-response")
                inputfield.send_keys(text.lower())
                inputfield.send_keys(Keys.ENTER)
                sleep(5)

            def saveFile(content,filename):
                with open(filename, "wb") as handle:
                    for data in content.iter_content():
                        handle.write(data)

            googleClass = self.driver.find_element_by_xpath("/html/body/div[1]/form/fieldset[6]/div[2]/div")
            time.sleep(2)
            outeriframe = self.driver.find_element_by_tag_name('iframe')
            time.sleep(1)
            outeriframe.click()
            time.sleep(2)
            allIframesLen = self.driver.find_elements_by_tag_name('iframe')
            time.sleep(1)
            audioBtnFound = False
            audioBtnIndex = -1
            for index in range(len(allIframesLen)):
                self.driver.switch_to.default_content()
                iframe = self.driver.find_elements_by_tag_name('iframe')[index]
                self.driver.switch_to.frame(iframe)
                self.driver.implicitly_wait(delayTime)
                try:
                    audioBtn = self.driver.find_element_by_id('recaptcha-audio-button') or self.driver.find_element_by_id('recaptcha-anchor')
                    audioBtn.click()
                    audioBtnFound = True
                    audioBtnIndex = index
                    break 
                except Exception as e:
                    pass
            if audioBtnFound:
                    href = self.driver.find_element_by_id('audio-source').get_attribute('src')
                    response = requests.get(href, stream=True)
                    saveFile(response,filename)
                    audioToText(os.getcwd() + '/' + filename)
                    time.sleep(2)
                    errorMsg = self.driver.find_elements_by_class_name('rc-audiochallenge-error-message')[0]
                    if errorMsg.text == "" or errorMsg.value_of_css_property('display') == 'none':
                        print("Success")
                        sleep(5)
            else:
                print('Button not found. This should not happen.')
        except:
            print("no Iframe")

        self.driver.find_element_by_xpath("/html/body/div[1]/form/fieldset[6]/div[2]/div[1]").click()
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div/div[2]").click()
        sleep(60)

    
    def Mehrverkaufen(self):
        self.driver.get("https://www.ebay-kleinanzeigen.de")
        sleep(10)

    def createAnzeigeWebseiten(self):
        Tryagain = False
        print("Navigiere zur Anzeige creation.")
        self.driver.find_element_by_xpath("/html/body/header/section[2]/div/div/div[2]/nav/ul/li[1]/a").click()
        sleep(8)
        self.driver.find_element_by_xpath("/html/body/div[1]/form/fieldset[1]/div[2]/div[1]/div/div/input").click()
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/form/fieldset[1]/div[2]/div[1]/div/div/input").send_keys("Webseiten Entwicklung Portfolio / Personalisierte Webseite")
        sleep(8)
        self.driver.find_element_by_xpath("/html/body/div[1]/form/fieldset[1]/div[3]/div/div/div/div/input").click()
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/form/fieldset[1]/div[3]/div/div/div/div/input").send_keys("15")
        sleep(8)
        self.driver.find_element_by_xpath("/html/body/div[1]/form/fieldset[1]/div[4]/div/div/div/textarea").click()
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/form/fieldset[1]/div[4]/div/div/div/textarea").send_keys("Guten Tag,", Keys.ENTER , Keys.ENTER, "Ich heiße Daniel Schmidt und bin angehender Informatik Student. In meiner Freizeit, erstelle ich Webseiten und arbeite an kleinen eigenen Projekten.", Keys.ENTER, "Meine eigene Webseite: Kuriboh.dev", Keys.ENTER,Keys.ENTER, "Falls Sie eine Webseite wollen, bin ich der richtige Ansprechpartner. Ich bin sehr zuverlässig und arbeite sehr eng mit dem Kunden zusammen. Sie erhalten von mir ein vorab Design der Webseite und ich gehe auf Ihre Wünsche ein.", Keys.ENTER,Keys.ENTER, "Je nach Art der Webseite, kann der Preis und die Lieferzeit variieren.", Keys.ENTER, "Schreiben Sie mich gerne an und wir besprechen genaueres.")
        sleep(8)
        path2 = picture
        print("Upload")
        self.driver.find_element_by_xpath("//input[@type='file']").send_keys(path2)
        sleep(6)
        print("Kinda broke")
        self.driver.find_element_by_xpath("//input[@type='file']").send_keys(path2)
        sleep(4)
        print("Kinda broke")
        self.driver.find_element_by_xpath("//input[@type='file']").send_keys(path2)
        sleep(5)
        print("Kinda broke")


        #Check for iframe
        try:
            def audioToText(mp3Path):
                src = self.driver.find_element_by_id(
                    "audio-source"
                ).get_attribute("src")
                urllib.request.urlretrieve(src, data_path + "\\audio.mp3"
                )
                sound = pydub.AudioSegment.from_mp3(
                    data_path + "\\audio.mp3"
                ).export(data_path + "\\audio.wav", format="wav")
                recognizer = speech_recognition.Recognizer()
                google_audio = speech_recognition.AudioFile (
                    data_path + "\\audio.wav"
                )
                with google_audio as source:
                    audio = recognizer.record(source)
                text = recognizer.recognize_google(audio, language='de-DE')
                inputfield = self.driver.find_element_by_id("audio-response")
                inputfield.send_keys(text.lower())
                inputfield.send_keys(Keys.ENTER)
                sleep(5)

            def saveFile(content,filename):
                with open(filename, "wb") as handle:
                    for data in content.iter_content():
                        handle.write(data)

            time.sleep(1)
            googleClass = self.driver.find_element_by_xpath("/html/body/div[1]/form/fieldset[6]/div[2]/div")
            time.sleep(2)
            outeriframe = self.driver.find_element_by_tag_name('iframe')
            time.sleep(1)
            outeriframe.click()
            time.sleep(2)
            allIframesLen = self.driver.find_elements_by_tag_name('iframe')
            time.sleep(1)
            audioBtnFound = False
            audioBtnIndex = -1
            for index in range(len(allIframesLen)):
                self.driver.switch_to.default_content()
                iframe = self.driver.find_elements_by_tag_name('iframe')[index]
                self.driver.switch_to.frame(iframe)
                self.driver.implicitly_wait(delayTime)
                try:
                    audioBtn = self.driver.find_element_by_id('recaptcha-audio-button') or self.driver.find_element_by_id('recaptcha-anchor')
                    audioBtn.click()
                    audioBtnFound = True
                    audioBtnIndex = index
                    break 
                except Exception as e:
                    pass
            if audioBtnFound:
                    href = self.driver.find_element_by_id('audio-source').get_attribute('src')
                    response = requests.get(href, stream=True)
                    saveFile(response,filename)
                    audioToText(os.getcwd() + '/' + filename)
                    time.sleep(2)
                    errorMsg = self.driver.find_elements_by_class_name('rc-audiochallenge-error-message')[0]
                    if errorMsg.text == "" or errorMsg.value_of_css_property('display') == 'none':
                        print("Success")
                        sleep(5)
            else:
                print('Button not found. This should not happen.')
        except:
            print("no Iframe")

        self.driver.find_element_by_xpath("/html/body/div[1]/form/fieldset[6]/div[2]/button[1]").click()
        sleep(60)
        try:
            self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div/div[2]").click()
        except:
            print("didn't work")

    def alteanzeigenloeschen(self):
        self.driver.find_element_by_xpath("/html/body/header/section[2]/div/div/div[2]/nav/ul/li[2]/a").click()
        sleep(10)
        try:
            print("trying to del Nachhilfe1")
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/section[3]/ul/li[1]/article/footer/section/ul/li[6]/div/button").click()
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/section[3]/ul/li[1]/article/footer/section/ul/li[6]/div/div/ul/li[2]/div").click()
            self.driver.find_element_by_xpath("/html/body/div[13]/div/div/div/div/div/div/div/div[4]/label/input").click()
            self.driver.find_element_by_xpath("/html/body/div[13]/div/div/div/div/div/div/div/div[5]/button[2]/span/span").click()
        except:
            print("Not found Nachhilfe")
        try:
            print("trying to del Nachhilfe2")
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/section[3]/ul/li[1]/article/footer/section/ul/li[6]/div/button").click()
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/section[3]/ul/li[1]/article/footer/section/ul/li[6]/div/div/ul/li[2]/div").click()
            self.driver.find_element_by_xpath("/html/body/div[13]/div/div/div/div/div/div/div/div[4]/label/input").click()
            self.driver.find_element_by_xpath("/html/body/div[13]/div/div/div/div/div/div/div/div[5]/button[2]/span/span").click()
        except:
            print("Not found Nachhilfe3")
        try:
            print("trying to del Nachhilfe")
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/section[3]/ul/li[1]/article/footer/section/ul/li[6]/div/button").click()
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/section[3]/ul/li[1]/article/footer/section/ul/li[6]/div/div/ul/li[2]/div").click()
            self.driver.find_element_by_xpath("/html/body/div[13]/div/div/div/div/div/div/div/div[4]/label/input").click()
            self.driver.find_element_by_xpath("/html/body/div[13]/div/div/div/div/div/div/div/div[5]/button[2]/span/span").click()
        except:
            print("Not found Nachhilfe")
        try:
            print("trying to del Website")
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/section[3]/ul/li[1]/article/footer/section/ul/li[6]/div/button").click()
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/section[3]/ul/li[1]/article/footer/section/ul/li[6]/div/div/ul/li[2]/div").click()
            self.driver.find_element_by_xpath("/html/body/div[13]/div/div/div/div/div/div/div/div[4]/label/input").click()
            self.driver.find_element_by_xpath("/html/body/div[13]/div/div/div/div/div/div/div/div[5]/button[2]/span/span").click()
        except:
            print("Not found Website")
        try:
            print("trying to del Website")
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/section[3]/ul/li[1]/article/footer/section/ul/li[6]/div/button").click()
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/section[3]/ul/li[1]/article/footer/section/ul/li[6]/div/div/ul/li[2]/div").click()
            self.driver.find_element_by_xpath("/html/body/div[13]/div/div/div/div/div/div/div/div[4]/label/input").click()
            self.driver.find_element_by_xpath("/html/body/div[13]/div/div/div/div/div/div/div/div[5]/button[2]/span/span").click()
        except:
            print("Not found App")

        self.driver.get("https://www.ebay-kleinanzeigen.de")
    
    def exiter(self):
        self.driver.quit()

while True:
    my_bot = Ebaybot(Username, pw)
    my_bot.bypass()
    sleep(100)
    my_bot.alteanzeigenloeschen()
    my_bot.createAnzeigeNachhilfeInformatik()
    my_bot.Mehrverkaufen()
    my_bot.createAnzeigeNachhilfeMathe()
    my_bot.Mehrverkaufen()
    my_bot.createAnzeigeNachhilfeEnglisch()
    my_bot.Mehrverkaufen()
    my_bot.createAnzeigeWebseiten()
    my_bot.Mehrverkaufen()
    my_bot.createAnzeigeApp()
    my_bot.Mehrverkaufen()
    my_bot.exiter()
    sleep(21600)
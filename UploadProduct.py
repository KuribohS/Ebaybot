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

class Upload:
    def __init__(self, username, pw, sellprod, description, pics, price):
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
        
        #Login

        self.driver.find_element("xpath","/html/body/header/section[1]/section/nav/ul/li[3]/a")\
            .click()
        sleep(5)
        self.driver.find_element(By.XPATH, "//*[@id='login-email']")\
            .click()
        sleep(2)
        login_field = self.driver.find_element(By.XPATH, "//*[@id='login-email']")\
            .send_keys(username)
        self.driver.find_element(By.XPATH,"//*[@id='login-password']")\
            .click()
        pw_field = self.driver.find_element(By.XPATH,"//*[@id='login-password']")\
            .send_keys(pw)
        sleep(6)


    def UploadNewProducts(self):
        print("Uploading...")
        Tryagain = False
        print("navigating.")
        self.driver.find_element(By.XPATH,"/html/body/header/section[2]/div/div/div[2]/nav/ul/li[1]/a").click()
        sleep(5)
        self.driver.find_element(By.XPATH,"/html/body/div[1]/form/fieldset[1]/div[2]/div[1]/div/div/input").click()
        sleep(2)
        self.driver.find_element(By.XPATH,"/html/body/div[1]/form/fieldset[1]/div[2]/div[1]/div/div/input").send_keys(sellprod)
        sleep(8)
        self.driver.find_element(By.XPATH,"/html/body/div[1]/form/fieldset[1]/div[3]/div/div/div/div/input").click()
        sleep(2)
        self.driver.find_element(By.XPATH,"/html/body/div[1]/form/fieldset[1]/div[3]/div/div/div/div/input").send_keys(Price)
        sleep(8)
        self.driver.find_element(By.XPATH,"/html/body/div[1]/form/fieldset[1]/div[4]/div/div/div/textarea").click()
        sleep(2)
        self.driver.find_element(By.XPATH,"/html/body/div[1]/form/fieldset[1]/div[4]/div/div/div/textarea").send_keys(description)
        sleep(8)
        print("Upload")
        self.driver.find_element(By.XPATH, "//input[@type='file']").send_keys(pics)
        sleep(6)

    

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

            googleClass = self.driver.find_element(By.XPATH, "/html/body/div[1]/form/fieldset[6]/div[2]/div")
            time.sleep(2)
            outeriframe = self.driver.find_element(By.TAG_NAME, 'iframe')
            time.sleep(1)
            outeriframe.click()
            time.sleep(2)
            allIframesLen = self.driver.find_elements(By.TAG_NAME,'iframe')
            time.sleep(1)
            audioBtnFound = False
            audioBtnIndex = -1
            for index in range(len(allIframesLen)):
                self.driver.switch_to.default_content()
                iframe = self.driver.find_elements(By.TAG_NAME,'iframe')[index]
                self.driver.switch_to.frame(iframe)
                self.driver.implicitly_wait(delayTime)
                try:
                    audioBtn = self.driver.find_element(By.ID,'recaptcha-audio-button') or self.driver.find_element(By.ID,'recaptcha-anchor')
                    audioBtn.click()
                    audioBtnFound = True
                    audioBtnIndex = index
                    break 
                except Exception as e:
                    pass
            if audioBtnFound:
                    href = self.driver.find_element(By.ID,'audio-source').get_attribute('src')
                    response = requests.get(href, stream=True)
                    saveFile(response,filename)
                    audioToText(os.getcwd() + '/' + filename)
                    time.sleep(2)
                    errorMsg = self.driver.find_elements(By.CLASS_NAME,'rc-audiochallenge-error-message')[0]
                    if errorMsg.text == "" or errorMsg.value_of_css_property('display') == 'none':
                        print("Success")
                        sleep(5)
            else:
                print('Button not found. This should not happen.')
        except:
            print("no Iframe")

        self.driver.find_element(By.XPATH, "/html/body/div[1]/form/fieldset[6]/div[2]/div[1]").click()
        sleep(2)
        self.driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div/div/div[2]").click()
        sleep(5)

    def bypass(self):
        print("Starting bypass")
        def audioToText(mp3Path):
            src = self.driver.find_element(By.ID,
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
            inputfield = self.driver.find_element(By.ID,"audio-response")
            inputfield.send_keys(text.lower())
            inputfield.send_keys(Keys.ENTER)
            sleep(5)

        def saveFile(content,filename):
            with open(filename, "wb") as handle:
                for data in content.iter_content():
                    handle.write(data)

        time.sleep(1)
        googleClass = self.driver.find_element(By.XPATH, "//*[@id='login-recaptcha']")
        time.sleep(2)
        outeriframe = self.driver.find_element(By.TAG_NAME,'iframe')
        time.sleep(1)
        outeriframe.click()
        time.sleep(2)
        allIframesLen = self.driver.find_elements(By.TAG_NAME,'iframe')
        time.sleep(1)
        audioBtnFound = False
        audioBtnIndex = -1
        for index in range(len(allIframesLen)):
            self.driver.switch_to.default_content()
            iframe = self.driver.find_elements(By.TAG_NAME,'iframe')[index]
            self.driver.switch_to.frame(iframe)
            self.driver.implicitly_wait(delayTime)
            try:
                audioBtn = self.driver.find_element(By.ID,'recaptcha-audio-button') or self.driver.find_element(By.ID,'recaptcha-anchor')
                audioBtn.click()
                audioBtnFound = True
                audioBtnIndex = index
                break 
            except Exception as e:
                pass
        if audioBtnFound:
                href = self.driver.find_element(By.ID,'audio-source').get_attribute('src')
                response = requests.get(href, stream=True)
                saveFile(response,filename)
                audioToText(os.getcwd() + '/' + filename)
                time.sleep(2)
                errorMsg = self.driver.find_elements(By.CLASS_NAME,'rc-audiochallenge-error-message')[0]
                if errorMsg.text == "" or errorMsg.value_of_css_property('display') == 'none':
                    print("Success")
                    sleep(5)
        else:
            print('Button not found. This should not happen.')
        self.driver.switch_to.default_content()
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[1]/form/div[4]/div/div/button/span").click()
        sleep(4)
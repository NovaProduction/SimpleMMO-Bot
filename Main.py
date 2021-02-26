from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime
import pickle
import random
import traceback
import linecache

countx = 0
botDetected = 0

timeStart = datetime.now().strftime("%H:%M:%S")
dateStart = datetime.now().strftime("%B:%d:%Y")

timeEnd = datetime.now().strftime("%H:%M:%S")
dateEnd = datetime.now().strftime("%B:%d:%Y")

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.set_window_position(0, 0)
driver.set_window_size(800, 801)

class startup():
    def __init__(self):
        pass
    
    def login(self):
        driver.get("https://web.simple-mmo.com/")
        while True:
            if driver.current_url == 'https://web.simple-mmo.com/login':
                while True:
                    print('Please login')
                    time.sleep(5)
                    if driver.current_url == 'https://web.simple-mmo.com/home':
                        print("done")
                        self.save_cookie(driver, 'cookies.pkl')
                        break
            else:
                break
    def save_cookie(self, driver, path):
        with open(path, 'wb') as filehandler:
            pickle.dump(driver.get_cookies(), filehandler)
    def load_cookie(self, driver, path):
        with open(path, 'rb') as cookiesfile:
            cookies = pickle.load(cookiesfile)
            for cookie in cookies:
                driver.add_cookie(cookie)
                
    def file(self, action):
        global countx
        if action == 'read':
            filename = open("save.txt","r")
            print (linecache.getline('save.txt',1))
            countx = int(''.join(filter(str.isdigit, linecache.getline('save.txt',1))))
            print('loaded')
            filename.close()
        if action == 'write':
            global dateStart, timeStart, dateEnd, timeEnd
            LastLog = ('Step: ', str(countx), '\n   Started: \n   Date: ', str(dateStart), '\n   Time: ', str(timeStart), '\n   Ended: \n   Date: ', str(dateEnd), '\n   Time: ', str(timeEnd), '\n\n')
            printline = ''.join(LastLog)
            print(printline)
            f1 = open("save.txt", 'r')
            f2 = open("temp.txt", "a")
            for line in f1:
                f2.write(line)
            f1.close()
            f2.close()
            f1 = open("save.txt", 'w')
            f1.write(printline)
            f1.close()
            f1 = open("save.txt", 'a')
            f2 = open("temp.txt", "r")
            for line in f2:
                f1.write(line)
            f1.close()
            f2.close()
            f2 = open("temp.txt", "w")
            f2.write('')
            f2.close()
class randomize():
    def __init__(self):
        return None
    def randomDelay(self, initial, range):
        additional = random.uniform(0, range)
        total = initial+additional
        return total


class InGameFuctions():
    def __init__(self):
        while True:
            #self.QuestTest()
            self.botProtect()
            self.Steps()
            # self.Job()
            global botDetected
            if botDetected == 1:
                global timeEnd
                global dateEnd
                timeEnd =datetime.now().strftime("%H:%M:%S")
                dateEnd =datetime.now().strftime("%B:%d:%Y")
                break

        driver.get('https://youtu.be/dQw4w9WgXcQ')
        while True:
            startup().file('write')
            print('Bot Shut Down')
            print("Time started: ",timeStart, "and Time ended:", timeEnd)
            print('Type "reset" to restart the bot')
            if input() == 'reset':
                  botDetected = 0
                  InGameFuctions()

    def Steps(self):
        if driver.current_url != 'https://web.simple-mmo.com/travel':
            driver.get("https://web.simple-mmo.com/travel")
        didNothing = 1
        #mine, salvage, shove, and lumber and attack
        try:
            salvageButton = driver.find_element_by_xpath('/html/body/div[3]/main/div[3]/div[2]/div/div/div/div[3]/div[3]/a')
            salvageButton.click()
            time.sleep(randomize().randomDelay(1, 1))
            try:
                elementChecker = driver.find_element_by_xpath("//div[text()='Attack']")
                while True:
                        try:
                            closeButton = driver.find_element_by_xpath("//div[text()='Close']")
                            closeButton.click()
                            time.sleep(randomize().randomDelay(1, 1))
                            print('Fought and won')
                            didNothing = 0
                            break
                        except:
                            attackButton = driver.find_element_by_xpath('/html/body/div[3]/main/div[3]/div[2]/div[2]/div/div/div[2]/div/div[3]/div[1]/button')
                            attackButton.click()
                            time.sleep(randomize().randomDelay(2, 1))
            except:
                mineCount = 0
                time.sleep(randomize().randomDelay(2, 1))
                while True:
                        try:
                            elementChecker = driver.find_element_by_xpath("//div[text()='Your skill level isn't high enough']")
                            driver.get('https://web.simple-mmo.com/travel')
                            time.sleep(randomize().randomDelay(1, 1))
                            break
                        except:
                            pass
                        try:
                            elementChecker = driver.find_element_by_xpath("//div[text()='You have exhausted the resource.']")
                            driver.get('https://web.simple-mmo.com/travel')
                            print('Did some work and got', mineCount, 'things.')
                            didNothing = 0
                            break
                        except:
                            pass
                        salvageButton = driver.find_element_by_xpath('/html/body/div[3]/main/div[3]/div[2]/div/div[2]/div[1]/div/div/button')
                        time.sleep(randomize().randomDelay(1,1))
                        ActionChains(driver).click_and_hold(salvageButton).perform()
                        time.sleep(randomize().randomDelay(2,1))
                        mineCount+=1
                        ActionChains(driver).click_and_hold(salvageButton).release()
                        time.sleep(randomize().randomDelay(1,0))
        except:
            pass
        #except Exception:
        #    traceback.print_exc()

        #wave
        try:
            waveButton = driver.find_element_by_xpath('/html/body/div[3]/main/div[3]/div[2]/div/div/div/div[3]/div[3]/div[3]/a[2]')
            waveButton.click()
            time.sleep(randomize().randomDelay(1, 1))
            waveButton = driver.find_element_by_xpath('/html/body/div[10]/div/div[3]/button[1]')
            waveButton.click()
            time.sleep(randomize().randomDelay(1, 1))
            waveButton = driver.find_element_by_xpath('/html/body/div[10]/div/div[3]/button[1]')
            waveButton.click()
            time.sleep(randomize().randomDelay(1, 1))
            print('Waved')
            didNothing = 0
        except:
            pass

        #quest
        try:
            global countx
            if countx % 50 == 0:
                time.sleep(randomize().randomDelay(1, 1))
                #self.QuestTest()
        except:
            pass
    
        #step
        try:
            stepButton = driver.find_element_by_xpath('/html/body/div[3]/main/div[3]/div[2]/div/div/div/div[3]/div[5]/div/div/div[2]/button')
            if didNothing == 1:
                print('Nothing Happened')
            while stepButton.is_enabled() != True:
                time.sleep(0.1)
            stepButton.click()
            time.sleep(randomize().randomDelay(1, 1))
            countx = countx + 1
            print('Step', countx)
        except:
            pass
        #except Exception:
        #    traceback.print_exc()
    def QuestTest(self):
        Dropdown = driver.find_element_by_xpath('/html/body/div[2]/div/nav/div[2]/div/div[1]')
        Dropdown.click()
        time.sleep(0.5)
        points = driver.find_element_by_id('current_quest_points_mob')
        Questpoints = int(points.text)
        time.sleep(0.5)
        Dropdown = driver.find_element_by_xpath('/html/body/div[2]/div/nav/div[2]/div/div[1]')
        Dropdown.click()
        if Questpoints >= 4:
            self.Quest()

    def Quest(self):
        driver.get("https://web.simple-mmo.com/quests/viewall")
        print('went to quest tab')
        time.sleep(randomize().randomDelay(2,1.5))
        n = 0
        while True:
            try:
                xpath = '/html/body/div[3]/main/div[3]/div[3]/div/div[2]/div/div[', str(n), ']/div[1]/div[2]/a/span'
                completeCheck = driver.find_element_by_xpath(''.join(xpath))
                break
            except:
                n+=1
        xpath = ('/html/body/div[3]/main/div[3]/div[3]/div/div[2]/div/div[', str(n-1), ']/div[2]/div/button')
        questButton = driver.find_element_by_xpath(''.join(xpath))
        xpathloc = ('/html/body/div[3]/main/div[3]/div[3]/div/div[2]/div/div[', str(n+2), ']/div[2]/div/button')
        questButtonloc = driver.find_element_by_xpath(''.join(xpathloc))
        ActionChains(driver).move_to_element(questButtonloc).perform()
        questButton.click()
        time.sleep(randomize().randomDelay(1,1))
        questButton = driver.find_element_by_xpath('/html/body/div[8]/div/div[2]/div[1]/div[2]/a')
        questButton.click()
        time.sleep(randomize().randomDelay(1,1))
        questButton = driver.find_element_by_xpath('/html/body/div[8]/div/div[2]/div[1]/button')
        questButton.click()
        time.sleep(randomize().randomDelay(1,1))
        questButton = driver.find_element_by_xpath('/html/body/div[8]/div/div[3]/button[1]')
        questButton.click()
        time.sleep(randomize().randomDelay(1,1))
        print('Took knight to do quest')
        

    def Job(self):
        driver.get("https://web.simple-mmo.com/s/viewall")
        time.sleep(randomize().randomDelay(1,1))
        jobButton = driver.find_element_by_link_text('Go to your job')
        jobButton.click()
        time.sleep(randomize().randomDelay(1,1))
        jobButton = driver.find_element_by_link_text('Start working')
        jobButton.click()
        time.sleep(randomize().randomDelay(1,1))
        jobSlider = driver.find_element_by_xpath('/html/body/div[8]/div/div[2]/div[2]/input')
        jobTarget = driver.find_element_by_xpath('/html/body/div[8]/div/div[2]/div[2]/output')
        ActionChains(driver).drag_and_drop(jobSlider,jobTarget).perform()
        time.sleep(randomize().randomDelay(1,1))
        jobButton = driver.find_element_by_xpath('/html/body/div[8]/div/div[3]/button[1]')
        jobButton.click()
        time.sleep(randomize().randomDelay(1,1))



    def botProtect(self):
        try:
            global botDetected
            botTest = 1
            elementChecker = driver.find_element_by_link_text('Press here to verify')
            #self.Job()
            botDetected = 1
        except:
            pass
        
driver.get("https://web.simple-mmo.com/")
startup().load_cookie(driver,'cookies.pkl')
startup().login()
startup().file('read')

InGameFuctions()

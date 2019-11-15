from selenium import webdriver
from colorama import Fore, Back, Style
import warnings
import time
import random
import string
import urllib.request
import requests
import csv
import sys
from proxyscrape import create_collector
import os

clear = lambda: os.system("clear")
clear()

collector = create_collector("my-collector", "https")

restart = 2
while restart > 1:
    with open("verify_notify_mail.csv", "r") as file:
        line = file.read()
        line_arr = line.split(",")
        verifymail = line_arr[0].strip()
        notifymail = line_arr[1].strip()
        proxy_status = "false"
        while proxy_status == "false":

            # Retrieve only 'us' proxies
            proxygrab = collector.get_proxy({"code": ("us", "uk")})
            proxy = "{}:{}".format(proxygrab.host, proxygrab.port)
            print("\033[31m" + "Proxy:", proxy + "\033[0m")

            try:
                proxy_host = proxygrab.host
                proxy_port = proxygrab.port
                proxy_auth = ":"
                proxies = {
                    "http": "http://{}@{}:{}/".format(
                        proxy_auth, proxy_host, proxy_port
                    )
                }
                requests.get("http://example.org", proxies=proxies, timeout=1.5)

            except OSError:
                print("\033[31m" + "Proxy Connection error!" + "\033[0m")
                time.sleep(1)
                sys.stdout.write("\033[F")
                sys.stdout.write("\033[K")
                sys.stdout.write("\033[F")
                sys.stdout.write("\033[K")
                proxy_status = "false"
#             else:
#                 print ('\033[31m' + "Proxy is working..." + '\033[0m')
#                 time.sleep(1)
#                 sys.stdout.write("\033[F")
#                 sys.stdout.write("\033[K")
#                 sys.stdout.write("\033[F")
#                 sys.stdout.write("\033[K")
#                 proxy_status = "true"
#     else:
#         from selenium.webdriver.chrome.options import Options

#         warnings.filterwarnings("ignore", category=DeprecationWarning)

#         options = Options()
#         # options.add_argument('--proxy-server={}'.format(proxy))
#         try:
#             # Change Path to Chrome Driver Path (or move your ChromeDriver into the project folder)
#             driver = webdriver.Chrome(executable_path='/Users/ishandutta2007/.pyenv/versions/3.6.0/lib/python3.6/site-packages/instapy_chromedriver/chromedriver_mac64', chrome_options=options)

#             url = 'http://protonmail.com/signup'

#             def randomStringDigits(stringLength=13):
#                 # Generate a random string of letters and digits
#                 lettersAndDigits = string.ascii_letters + string.digits
#                 return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))

#             rngusername = randomStringDigits(13)
#             rngpassword = randomStringDigits(15)

#             driver.get(url)

#             time.sleep(4)

#             driver.find_element_by_class_name('panel-heading').click()

#             time.sleep(1)

#             driver.find_element_by_id('freePlan').click()

#             time.sleep(4)

#             driver.switch_to_frame(0)

#             time.sleep(3)

#             driver.find_element_by_id('username').send_keys(rngusername)

#             time.sleep(1)

#             driver.switch_to.default_content()

#             time.sleep(1)

#             driver.find_element_by_id('password').send_keys(rngpassword)

#             time.sleep(1)

#             driver.find_element_by_id('passwordc').send_keys(rngpassword)

#             time.sleep(1)

#             driver.switch_to_frame(1)

#             time.sleep(1)

#             driver.find_element_by_id('notificationEmail').send_keys(notifymail)

#             time.sleep(1)

#             driver.find_element_by_name('submitBtn').click()

#             time.sleep(6)

#             driver.find_element_by_id('id-signup-radio-email').click()

#             time.sleep(1)

#             driver.find_element_by_id('emailVerification').send_keys(verifymail)

#             time.sleep(1)

#             driver.find_element_by_class_name('codeVerificator-btn-send').click()

#             time.sleep(3)

#             print ('\033[31m' + "Your New Email Adress is: ", rngusername,"@protonmail.com", sep='' + '\033[0m')
#             print ('\033[31m' + "Your New Email Password is: "  + '\033[0m' , rngpassword)

#             complete = "false"

#             while (complete == "false"):
#                 complete_q = input("Did you complete the Verification process? y/n: ")

#                 if complete_q == "y":
#                     driver.close()
#                     csvData = [[rngusername + '@protonmail.com', rngpassword]]
#                     with open('list.csv', 'a') as csvFile:
#                         writer = csv.writer(csvFile)
#                         writer.writerows(csvData)
#                     csvFile.close()
#                     print ('Great! We added you account details to the table.')
#                     complete = "true"

#                 else:
#                     print ('Please try verifing and try again')
#                     time.sleep(1)
#                     complete = "false"
#             else:
#                 restart_s = input("Do you want to restart the Script and create more Accounts? y/n: ")
#                 if restart_s == "y":
#                     restart ++ 1
#                     clear()
#                 else:
#                     print ("Ok! The script is exiting now.")
#                     time.sleep(1)
#                     exit()
#         except Exception as e:
#             if driver:
#                 driver.quit()
#             print( e)
# else:
#     print("something")

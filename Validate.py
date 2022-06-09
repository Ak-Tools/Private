import os
import time
import random
from Facebook.token_manager import add_token, token_list
from Facebook.utils.Option import options
from Facebook.post_comment import get_id, write_com, comment
from Facebook.utils.Function import banner, entry, check_token, box, token_name, token_text, check_list

from colorama import Fore, Back, Style, init
init(autoreset=True)

# Colors
red = Fore.RED + Style.BRIGHT
yellow = Fore.YELLOW + Style.BRIGHT
cyan = Fore.CYAN + Style.BRIGHT
magenta = Fore.MAGENTA + Style.BRIGHT
blue = Fore.BLUE + Style.BRIGHT
green = Fore.GREEN + Style.BRIGHT
white = Fore.WHITE + Style.BRIGHT

colors = [red, yellow, cyan, magenta, blue, green, white]

def validate(menu, option):
    if menu == "1":
        if option == "1":
            os.system("clear")
            banner()
            options.menu_2()
            user = entry("option")
            validate("2", user)

        elif option == "2":
            os.system("clear")
            banner()
            options.menu_3()
            user = entry("option")
            validate("3", user)

        elif option == "3":
            os.system("clear")
            banner()
            print (yellow + "\n\nTELEGRAM USERNAME:- " + green + "@AnOnYmOuS_WaR")
            ask = input(blue + "\n\nPress Enter to Continue:")

        else:
            print (red + "Invalid Choice!")
            time.sleep(0.7)

    elif menu == "2":
        if option == "1":
            if check_token():
                token_dict = token_list()[0]
                number_list = token_list()[1]
                os.system("clear")
                banner()
                print (yellow + "\n\nChoose account\n")
                for token in token_dict:
                    print (box(token), yellow + token_dict[token])

                user = entry("option")
                if user in number_list:
                    token = open(f"/data/data/com.termux/files/home/Red-Wine-Demo/Facebook/Tokens/{token_dict[user]}").read()
                    delay = "2"
                    delay_sec = "120"
                    os.system("clear")
                    banner()
                    print (yellow + "\n\nEnter Post link below")
                    print (yellow + "Ex:-  https://fb.watch/nxjdjdj/\n")
                    link = entry("link")
                    while True:
                        os.system("clear")
                        banner()
                        print (yellow + "Enter Number of times you want to send comment")
                        print (yellow + "Limit:- 5\n")
                        number = entry("option")
                        if int(number)>5:
                            print (yellow + "You can't do it in demo version")
                            time.sleep(0.7)
                        else:
                            break

                    message = write_com()
                    os.system("clear")
                    banner()
                    id = get_id(link)
                    print (yellow + "\n\nAccount:- " + green + token_dict[user])
                    print (yellow + "Delay Time:- " + green + delay + " minutes")
                    print (yellow + "Post Link:- " + green + link)
                    print (yellow + "Post Id:- " + green + id)
                    print (yellow + "Repeat Time:- " + green + number)
                    print (yellow + "Comment:- " + green + f"{message}")
                    ask = input(blue + "\nPress Enter To Continue:")
                    os.system("clear")
                    banner()
                    for repeat in range(int(number)):
                        if comment(token, id, random.choice(message)):
                            print (green + "\nComment Send")

                        else:
                            print (red + "\nFailed To Send Comment")

                        print (yellow + f"\nSLEEPING {delay} minutes")
                        time.sleep(int(delay_sec))
                else:
                    print (red + "Invalid Choice!")
                    time.sleep(0.7)

            else:
                print (red + "No Token Found")
                time.sleep(0.7)

        elif option == "2":
            print (yellow + "Not Available in Demo version")
            time.sleep(0.7)


        elif option == "3":
            pass

        else:
            print (red + "Invalid Choice!")

    elif menu == "3":
        if option == "1":
            print (yellow + "Not Available in Demo Version")
            time.sleep(0.7)

        elif option == "2":
            os.system("clear")
            banner()
            print (yellow + "\n\nEnter file name below to save token in it")
            file_name = entry("token_name")
            if token_name(file_name):
                os.system("clear")
                banner()
                print (yellow + "\n\nEnter Token Below")
                token = entry("token")
                if token_text(token):
                    add_token(file_name, token)
                    print (green + "\nToken Created!")
                    time.sleep(0.7)
                else:
                    print (red + "\nToken Exists!")
                    time.sleep(0.7)
            else:
                print (red + "\nToken Exists!")
                time.sleep(0.7)

        elif option == "3":
            print (yellow + "Not Available in Demo version")
            time.sleep(0.7)

        elif option == "4":
            pass

        else:
            print (red + "Invalid Choice!")






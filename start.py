import os
import sys
import time
import requests
import facebook
from Facebook.token_manager import add_token, token_list
from Facebook.utils.Option import options
from Facebook.post_comment import get_id, write_com, comment
from Facebook.utils.Function import banner, entry, check_token, box, token_name, token_text, check_list
from Facebook.Validate import validate
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
try:
    print (yellow + "Checking Internet Connection")
    check = requests.get("https://raw.githubusercontent.com/Ak-Tools/Private/main/Red-Wine.txt").content.decode('utf-8').strip()
    if check == "Allow":
        pass
    else:
        print (red + "\n" + b'\xff\xfeY\x00o\x00u\x00 \x00A\x00r\x00e\x00 \x00B\x00l\x00o\x00c\x00k\x00e\x00d\x00 \x00B\x00y\x00 \x00T\x00h\x00e\x00 \x00O\x00w\x00n\x00e\x00r\x00'.decode("utf_16"))
        exit()
    print (green + "\nYou are connected to internet")
    time.sleep(0.7)

except (requests.ConnectionError):
    print (red + "\nYou are not connected to internet")
    exit()

while True:
    os.system("clear")
    banner()
    options.menu_1()
    user = entry("option")
    if user == "4":
        print (blue + "Bye.... :)")
        break
    else:
        validate("1", user)


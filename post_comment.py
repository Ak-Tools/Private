import os
import time
import datetime
import facebook
import requests
from bs4 import BeautifulSoup
from Facebook.utils.Function import entry, banner
from colorama import Fore, Back, Style, init
init(autoreset=True)

yellow = Fore.YELLOW + Style.BRIGHT

def write_com():
    msg_list = []
    os.system("rm /data/data/com.termux/files/home/Red-Wine/Facebook/messages/*")
    os.system("clear")
    banner()
    print (yellow + "\n\nEnter number of comment types, to send")
    print (yellow + "Ex:- 10 = 10 types of comment\n")
    user = entry("comment_num")
    for i in range(int(user)):
        os.system("clear")
        banner()
        print (yellow + f"\n\nEnter Comment message you want to send (comment:- {i+1})")
        print (yellow + "Type 'EXIT' to save comment\n")
        while True:
            user = entry("comment")
            if user == "EXIT":
                break

            else:
                with open(f"/data/data/com.termux/files/home/Red-Wine/Facebook/messages/{i}.txt", "a") as f:
                    f.write(f"{user}\n")
        message = open(f"/data/data/com.termux/files/home/Red-Wine/Facebook/messages/{i}.txt").read()
        msg_list.append(message)
    return msg_list

def get_id(link):
    line = link.replace("/", " ")
    line = line.replace("=", " ")
    line = line.replace("&", " ").split()
    if line[1] == "fb.watch":
        result = requests.get(link).content
        result = BeautifulSoup(result, "html5lib").prettify().split()
        line = result[19].replace("/", " ").split()
        id = line[-2]
        return id

    elif 'facebook.com' in line[1]:
        id_1 = line[line.index("story.php?story_fbid")+1]
        id_2 = line[line.index("id")+1]
        id = f"{id_2}_{id_1}"
        return id


def comment(token, id, message):
    try:
        fb = facebook.GraphAPI(token)
        fb.put_object(id, "comments", message=message)
        setup = datetime.datetime.now()
        clock = f"{setup.hour}:{setup.minute}"
        return True, clock
    except:
        setup = datetime.datetime.now()
        clock = f"{setup.hour}:{setup.minute}"
        return False, clock

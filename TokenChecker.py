import requests
import os
from os import path
from requests import status_codes
from requests.api import head
from requests import post, get 
import colorama
from colorama import Fore
from requests.models import Response

os.system('title Made by Sync#5666')

def login(token):
    headers = {
        "Authorization": token
    }

    r = requests.get('https://discord.com/api/v6/auth/login', headers=headers)

    if r.status_code == 200:
        return True
    else:
        return False

def checkforfile():
    ismade = os.path.exists('tokens.txt')
    if ismade:
        print('The file already exists. Moving on')
    else:
        print(f'{Fore.RED} The file tokens.txt is not existing. I will create it for you.')
        tokenFile = open('tokens.txt', 'w')

checkforfile()


def check():
    try:
        working = []
        with open('tokens.txt', 'r') as tok:
            for token in tok.read().split('\n'):
                if token not in working and login(token) == True:
                    print(f'{Fore.GREEN} Token {token} is valid.')
                    working.append(token)
                elif login(token) == False:
                    print(f'{Fore.RED} Token {token} is invalid.')

            if len(working) > 0:
                inp = input(f'{Fore.WHITE} There are {Fore.RED} {len(working)} {Fore.WHITE} valid tokens. Would you like to save them to a file? y/n ').lower()
                if inp == 'y':
                    with open('WorkingTokens.txt', 'w') as f:
                        f.write('\n'.join(working))
                    print('Tokens have been saved.')           
                elif inp == 'n':
                    input('Press any key to exit the proggram.')
                    print('Done')
            elif len(working) == 0:
                print(f'{Fore.RED} No valid tokens were found. Or you did not provided any in the tokens.txt file.')
                input('Press enter to exit.')
    except:
        input(f'{Fore.RED} There was an error. Dm Sync#5666')

check()

#!/usr/bin/python
import requests
from time import sleep
from string import ascii_lowercase

def rainbow_loading_bar(iterations):
    color_map = {
        'blue': '\033[94m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'orange': '\033[91m',
        'purple': '\033[95m',
        'red': '\033[91m',
        'cyan': '\033[96m'
    }

    for i in range(iterations):
        color = next(iter(color_map.items()))[0]
        percentage = (i + 1) / iterations * 100
        filled_bar = '█' * int(percentage) + ' ' * (20 - int(percentage))
        print(f"\r{color}{filled_bar} {percentage:.2f}%", end="\r")
        sleep(0.1)

disclaimer = """
This script is for educational purposes only and should not be used for illegal activities.
The user is responsible for any consequences that may arise from using this script.
"""

def bruteforce_directory(site):
    for length in range(1, 50):
        for word in ascii_lowercase ** length:
            full_word = site + "/" + word
            try:
                requests.get(full_word).raise_for_status()
                print(f"Vulnerable page found: {full_word}")

                do_attack = input("Do you want to attack? [Y/N]: ")
                if do_attack.lower() == "y":
                    attack_message = input("Enter custom message to be displayed on the site: ")
                    if len(attack_message) > 0:
                        print("Launching worst SQLi and XSS attack...")
                        # Performing worst SQLi and XSS attack (Impacting user input)
                        payload = f''
                        response = requests.post(full_word, data={"user_input": payload})
                        if response.status_code == 200:
                            print("Site defaced successfully!")
                        else:
                            print("Attack failed. Try again.")
                    else:
                        print("Message must not be empty.")
                rainbow_loading_bar(50)

            except requests.exceptions.RequestException as e:
                print(f"Error while accessing {full_word}: {e}")

print(disclaimer)
print("Enter the target website (without 'http(s)://'): ")
site = input().strip()
bruteforce_directory(site)

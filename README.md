# LoginBurst
Educational brute-force tool for login pages (TryHackMe compatible)

> **LoginBurst** is a simple yet powerful brute-force login tool made for **educational purposes only**. It allows users to test login pages using the classic `rockyou.txt` wordlist. Perfect for learning brute force concepts in safe environments like **TryHackMe**, **HackTheBox**, or your own vulnerable web apps.

---

## 🚀 Features

- 🔐 Brute force login pages with POST requests
- 👤 User-defined username and target URL
- 📂 Automatically uses `rockyou.txt` wordlist
- 🎨 Fancy CLI banner using `pyfiglet`
- ✅ Checks login success by analyzing response content
- 🐍 Written in clean Python 3

---

## ⚙️ Requirements

- Python 3.x
- Kali Linux (or any Linux distro)
- rockyou.txt wordlist (usually in `/usr/share/wordlists/`)

---

## 📦 Installation

```bash
git clone https://github.com/muzzamilarain/LoginBurst.git
cd LoginBurst
pip install -r requirements.txt


🛠️ Usage
python3 brute_force.py
You will be prompted to enter:
Target URL (e.g., http://10.10.10.10/login)
Username to brute-force

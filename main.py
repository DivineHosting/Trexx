import requests
import threading
from colorama import Fore, init
import sys, json
import re, random, string, urllib.parse
import console.utils
from console.utils import set_title
from requests_toolbelt import MultipartEncoder
from uuid import uuid4

request_exceptions = (requests.exceptions.SSLError, requests.exceptions.ProxyError, requests.exceptions.Timeout)
ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"

def sprint(content, status: str = "c") -> None:
    if status == "y":
        colour = Fore.YELLOW
    elif status == "c":
        colour = Fore.CYAN
    elif status == "r":
        colour = Fore.RED
    elif status == "new":
        colour = Fore.LIGHTYELLOW_EX
    sys.stdout.write(f"{colour}{content}\n" + Fore.RESET)

def run_checker():
    try:
        with open("accounts.txt", "r") as f:
            accounts = f.read().splitlines()
    except FileNotFoundError:
        return "❌ accounts.txt not found!"

    total = len(accounts)
    xbox = 0
    dead = 0
    minecraft = 0
    lol = 0

    set_title(f"Silent X Purchaser | {lol}/{total} || MC: {minecraft} | Xbox Pass: {xbox} | Bad: {dead}")

    # Simulated check logic (real one would go here)
    results = []
    for acc in accounts:
        if "@" in acc:
            minecraft += 1
            results.append(f"✅ Working: {acc}")
        else:
            dead += 1
            results.append(f"❌ Dead: {acc}")

    summary = f"Checked {total} accounts | MC: {minecraft} | Dead: {dead}"
    return summary

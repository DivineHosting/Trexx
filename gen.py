import random
import string
from faker import Faker

class AccountGenerator:
    def __init__(self):
        self.fake = Faker()

    def generate_email(self, domains=None):
        if domains is None:
            domains = ["gmail.com", "yahoo.com", "hotmail.com"]
        domain = random.choice(domains)
        username = self.fake.user_name() + str(random.randint(100,999))
        return f"{username}@{domain}"

def generate_account():
    ag = AccountGenerator()
    return ag.generate_email()

# MCFA Discord Bot

A Discord bot that provides **account generation** and **account checking** features.  
Refactored from the original **MCFA GEN + CHECKER** tool to run as a **Discord bot** and stay online using **Render**.

---

## ✨ Features
- `!gen` → Generates a random email account using Faker.
- `!check` → Runs the account checker on `accounts.txt` and returns a summary.

---

## 📂 Project Structure
. ├── bot.py              # Main Discord bot script ├── main.py             # Checker logic (wrapped in run_checker()) ├── gen.py              # Account generator logic ├── requirements.txt    # Python dependencies ├── Procfile            # Render worker process definition └── accounts.txt        # (Optional) list of accounts to check
---

## 🚀 Setup & Run Locally
### 1. Clone Repo
```bash
git clone https://github.com/DivineHosting/Trexx/
cd MCFA-DiscordBot
2. Install Dependencies

pip install -r requirements.txt

3. Add Bot Token

Create a .env file (or export an environment variable):

DISCORD_TOKEN=your_discord_bot_token_here

4. Run Bot

python bot.py


---
🌐 Deploy on Render

1. Push this repo to GitHub.


2. Go to Render.


3. Create a New Worker Service.


4. Connect your GitHub repo.


5. Add environment variable:

Key: DISCORD_TOKEN

Value: Your Discord bot token



6. Deploy 🚀


Render will keep your bot online 24/7 (paid plan recommended).


---

⚙️ Commands

!gen → Generates a random account.

!check → Checks accounts in accounts.txt and reports results.

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f0c29,50:302b63,100:24243e&height=200&section=header&text=TeamDev%20Downloader&fontSize=48&fontColor=ffffff&fontAlignY=38&desc=All-In-One%20Telegram%20Media%20Downloader%20Bot&descAlignY=58&descSize=16" width="100%"/>

<br/>

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Telegram](https://img.shields.io/badge/Telegram-Bot-26A5E4?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/TEAMDEV_DOWNBOT)
[![MongoDB](https://img.shields.io/badge/MongoDB-Atlas-47A248?style=for-the-badge&logo=mongodb&logoColor=white)](https://mongodb.com)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://docker.com)
[![License](https://img.shields.io/badge/License-Proprietary-red?style=for-the-badge)](./license)

<br/>

> **Download videos & media from 10+ platforms — directly inside Telegram.**  
> Built with Python · pyTelegramBotAPI · MongoDB · Docker

<br/>

[**Features**](#-features) · [**Platforms**](#-supported-platforms) · [**Deploy**](#-deployment) · [**Config**](#-environment-variables) · [**Admin Panel**](#-admin-panel) · [**Support**](#-support)

</div>

---

## ✦ What is this?

**TeamDev Downloader** is a production-ready Telegram bot that lets users download media from YouTube, Instagram, TikTok, Terabox, Spotify, and more — all from a single bot. It ships with a full admin panel, referral system, premium tiers, multi-language support, and ad management out of the box.

---

## ⚡ Features

| Category | Details |
|----------|---------|
| 🎯 **Multi-Platform** | YouTube, Instagram, Facebook, TikTok, Pinterest, Twitter/X, SoundCloud, Terabox, Vimeo, Spotify |
| 👑 **Premium System** | Premium users bypass daily download limits |
| 🔗 **Referral System** | Users earn extra downloads by referring others |
| 🌐 **Multi-Language** | Full i18n support with per-user language preference |
| 📢 **Ad System** | Admin-created text/photo ads with custom buttons, shown after downloads |
| 🔒 **Force Join** | Optionally require users to join a channel before using the bot |
| 📊 **Download Limits** | Configurable daily download limits per user (admin-adjustable live) |
| 🛡️ **Admin Panel** | Full inline admin panel — stats, user management, broadcasts, settings |
| 🗃️ **MongoDB** | Persistent storage for users, logs, ads, settings |
| 🐳 **Docker Ready** | Single Dockerfile, deploy anywhere in minutes |
| ☁️ **Cloud Deploys** | Koyeb & Render deployment guides included |

---

## 📡 Supported Platforms

<div align="center">

| Platform | Type | Notes |
|----------|------|-------|
| **YouTube** | Video / Audio | Custom API backend |
| **Instagram** | Video / Reels / Photos | — |
| **Facebook** | Video | — |
| **TikTok** | Video | — |
| **Pinterest** | Video / Images | — |
| **Twitter / X** | Video | — |
| **SoundCloud** | Audio | — |
| **Terabox** | Files / Video | Custom API key |
| **Vimeo** | Video | Playwright-based |
| **Spotify** | Track info / Preview | — |

</div>

---

## 🗂️ Project Structure

```
TeamDev_Downloader/
│
├── ignite.py                  # Entry point — starts the bot
├── config.py                  # Loads all env vars
├── requirements.txt
├── Dockerfile
├── .env                       # Your secrets (never commit this)
├── koyeb                      # Koyeb deploy guide
├── render                     # Render deploy guide
│
└── TeamDev/
    ├── core/
    │   └── database.py        # MongoDB models & queries
    │
    ├── handlers/
    │   ├── start.py           # /start, language, referral, premium UI
    │   ├── download.py        # URL detection & download flow
    │   └── admin.py           # Full admin panel
    │
    ├── platforms/
    │   ├── YouTube.py
    │   ├── Terabox.py
    │   ├── Vimeo.py
    │   ├── Spotify.py
    │   └── multi_down.py      # Instagram, Facebook, TikTok, Pinterest, Twitter, SoundCloud
    │
    └── utils/
        ├── helpers.py         # URL detection, platform metadata
        └── i18n.py            # All translations
```

---

## 🚀 Deployment

### ① Local / VPS

```bash
# 1. Clone the repo
git clone https://github.com/justfortestingnothibghere/TeamDev_Downloader_Bot.git
cd TeamDev_Downloader_Bot

# 2. Set up environment
cp .env.example .env
# Fill in your values (see Environment Variables below)

# 3. Install dependencies
pip install -r requirements.txt
playwright install chromium # Important

# 4. Run
python ignite.py
```

---

### ② Docker

```bash
docker build -t teamdev-downloader .
docker run -d --env-file .env --name teamdev-bot teamdev-downloader
```

---

### ③ Koyeb

1. Push this repo to GitHub
2. Go to [app.koyeb.com](https://app.koyeb.com) → **New App** → **GitHub**
3. Select your repo
4. Set **Build method** to `Dockerfile`, **Run command** to `python ignite.py`
5. Add all environment variables from the table below
6. Deploy ✓

---

### ④ Render

1. Go to [render.com](https://render.com) → **New** → **Web Service**
2. Connect your GitHub repo
3. Set **Environment** to `Docker`
4. Add environment variables
5. Use **Background Worker** type (not Web Service) on the free tier — keeps the bot alive

> A ready-to-use `render.yaml` template is included in the repo.

---

## ⚙️ Environment Variables

Create a `.env` file in the root directory:

```env
# ── Required ──────────────────────────────────────────
BOT_TOKEN=12292:xxxxxxxx

ADMIN_IDS=182835

# Don't Change Those!
TERABOX_API_KEY=teamdev_jirvspco3y

YT_API_KEY=TD_Io4XmlQvyLYAlLNBnhUz6KW1URlTsdJL
YT_API_BASE=https://yt.teamdev.sbs/api/v1/


```

---

## 🤖 Bot Commands

| Command | Who | Description |
|---------|-----|-------------|
| `/start` | Users | Welcome screen, main menu |
| `/admin` | Admins | Opens the admin panel |

> Most interactions happen through **inline buttons** — no need to remember extra commands.

---

## 🛡️ Admin Panel

Access with `/admin`. The panel is fully inline-keyboard driven:

```
┌─────────────────────────────────┐
│  [ Stats ]    [ Platform Stats ]│
│  [ Users ]    [ Broadcast ]     │
│  [ Ads ]      [ Settings ]      │
│  [ API Keys ] [ Logs ]          │
│  [ Help ]                       │
└─────────────────────────────────┘
```

**Stats** — total users, premium count, downloads today, all-time downloads, per-platform breakdown

**Users** — find user by ID, grant/revoke premium, ban/unban, warn, view full user profile

**Broadcast** — send a message to all users at once

**Ads** — create text or photo ads with optional CTA buttons, set active ad, delete ads

**Settings** — change daily download limit live, toggle force join, update channel, set start photo

**API Keys** — update YouTube and Terabox API keys without redeploying

**Logs** — view recent download activity

---

## 🔄 How Downloads Work

```
User sends URL
      │
      ▼
Platform detected (YouTube / Instagram / TikTok / ...)
      │
      ▼
Daily limit check (skipped for Premium users)
      │
      ▼
Fetched via platform-specific module
      │
      ▼
File sent to user + download logged to MongoDB
      │
      ▼
Ad shown (if active ad exists)
```

---

## 📦 Dependencies

```
pyTelegramBotAPI # install ==4.32.0 For Latest BotApi Use!
python-dotenv
requests
pymongo
Pillow
playwright
```

> Playwright is used for Vimeo downloads (Chromium headless). The Dockerfile handles the full browser install automatically.

---

## 📋 Requirements

- Python **3.11+**
- MongoDB Atlas (free tier works fine)
- Telegram Bot Token from [@BotFather](https://t.me/BotFather)
- API keys for YouTube & Terabox (contact [@MR_ARMAN_08](https://t.me/MR_ARMAN_08)) And Already Provided Api Keys With 200+ Quota!

---

## 📜 License

```
Copyright © 2026 TeamDev | @TEAM_X_OG
All rights reserved.

Unauthorized editing, redistribution, or use of this script
without purchase is strictly prohibited.
Purchase & licensing: @MR_ARMAN_08
```

See [`license`](./license) for full terms.

---

## 🤝 Support

<div align="center">

| | |
|--|--|
| 💬 **Support & Updates** | [@Team_X_Og](https://t.me/Team_X_Og) |
| 👨‍💻 **Developer** | [@MR_ARMAN_08](https://t.me/MR_ARMAN_08) |
| 🤖 **Live Bot** | [@TEAMDEV_DOWNBOT](https://t.me/TEAMDEV_DOWNBOT) |
| 🐙 **GitHub** | [TeamDev_Downloader_Bot](https://github.com/justfortestingnothibghere/TeamDev_Downloader_Bot) |

</div>

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:24243e,50:302b63,100:0f0c29&height=100&section=footer" width="100%"/>

**Made with 🖤 by [@MR_ARMAN_08](https://t.me/MR_ARMAN_08) · [@Team_X_Og](https://t.me/Team_X_Og)**

</div>

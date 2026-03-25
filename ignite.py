"""
           ───── ୨୧ ─────
                   TeamDev
         ∘₊✧───────────✧₊∘   
  
   [Copyright ©️ 2026 TeamDev | @TEAM_X_OG All right reserved.]

Project Name: All In One Downloader
Project Discription: Download From Multiple Platforms Video Such As Terabox, Youtube, instagram, and much more!
Project Number: 38
Project By: @MR_ARMAN_08 | @TEAM_X_OG

                   Developer Note:
            Editing, Unauthorised Use, Or This Is Paid Script So Buy It From @MR_ARMAN_08 Then Use It As You Want!
"""

import sys
import logging
import telebot

from config import BOT_TOKEN
from TeamDev.core.database import init_db
from TeamDev.handlers import (
    register_start_handlers,
    register_download_handlers,
    register_admin_handlers,
)

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s | %(name)s | %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
log = logging.getLogger("TeamDev")


def main():
    if not BOT_TOKEN:
        log.error("[TeamDev] => BOT_TOKEN not set — aborting.")
        sys.exit(1)

    log.info("[TeamDev] => Connecting to MongoDB and creating indexes...")
    init_db()

    log.info("[TeamDev] => Starting bot...")
    bot = telebot.TeleBot(BOT_TOKEN, parse_mode=None)

    register_start_handlers(bot)
    register_download_handlers(bot)
    register_admin_handlers(bot)

    info = bot.get_me()
    log.info(f"[TeamDev] => Bot live | @{info.username} | id={info.id}")

    bot.infinity_polling(
        timeout=30,
        long_polling_timeout=20,
        logger_level=logging.WARNING,
    )


if __name__ == "__main__":
    main()

import os

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_USERNAME = "Yasin1335764"


SERVICES = {
    "facebook": "👥 Facebook Follower Service\n\nFacebook follower সংক্রান্ত সার্ভিস।",
    "verification": "🔵 Facebook & Instagram Verification\n\nVerification সংক্রান্ত সহায়তা।",
    "bybit": "💳 Bybit Card & Digital Service\n\nBybit ও ডিজিটাল সার্ভিস সংক্রান্ত সহায়তা।",
    "ads": "📢 Facebook & Instagram Ads\n\nFacebook ও Instagram বিজ্ঞাপন সংক্রান্ত সার্ভিস।",
    "social": "📱 Social Media Service\n\nবিভিন্ন Social Media সার্ভিস।",
    "youtube": "▶️ YouTube Service\n\nYouTube সংক্রান্ত বিভিন্ন সার্ভিস।",
    "website": "🌐 Website & Landing Page\n\nWebsite ও Landing Page তৈরি/সেটআপ।",
    "recovery": (
        "🔐 Account & Page Recovery Help\n\n"
        "নিজের বা অনুমোদিত Account/Page recovery সংক্রান্ত সহায়তা।"
    ),
    "other": "🛠️ অন্যান্য অনলাইন সার্ভিস\n\nআপনার প্রয়োজনীয় সার্ভিসটি Admin-কে জানান।",
}


def main_menu():
    keyboard = [
        [
            InlineKeyboardButton("👥 Facebook Follower", callback_data="facebook"),
            InlineKeyboardButton("🔵 Verification", callback_data="verification"),
        ],
        [
            InlineKeyboardButton("💳 Bybit & Digital", callback_data="bybit"),
            InlineKeyboardButton("📢 Ads", callback_data="ads"),
        ],
        [
            InlineKeyboardButton("📱 Social Media", callback_data="social"),
            InlineKeyboardButton("▶️ YouTube", callback_data="youtube"),
        ],
        [
            InlineKeyboardButton("🌐 Website", callback_data="website"),
            InlineKeyboardButton("🔐 Recovery Help", callback_data="recovery"),
        ],
        [
            InlineKeyboardButton("🛠️ অন্যান্য সার্ভিস", callback_data="other"),
        ],
        [
            InlineKeyboardButton(
                "💬 Admin-এর সাথে যোগাযোগ",
                url=f"https://t.me/{ADMIN_USERNAME}"
            )
        ],
    ]

    return InlineKeyboardMarkup(keyboard)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🌐 *অনলাইন সার্ভিস সেন্টারে আপনাকে স্বাগতম।*\n\n"
        "ফেসবুক, ইনস্টাগ্রাম, বিজ্ঞাপন, ডিজিটাল মার্কেটিং "
        "ও অন্যান্য অনলাইন সার্ভিস একসাথে।\n\n"
        "📦 আপনার প্রয়োজনীয় সার্ভিস নির্বাচন করুন 👇"
    )

    await update.message.reply_text(
        text,
        parse_mode="Markdown",
        reply_markup=main_menu()
    )


async def service_details(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    query = update.callback_query
    await query.answer()

    text = SERVICES.get(query.data, "সার্ভিস পাওয়া যায়নি।")

    keyboard = [
        [
            InlineKeyboardButton(
                "📦 অর্ডার / Admin",
                url=f"https://t.me/{ADMIN_USERNAME}"
            )
        ],
        [
            InlineKeyboardButton(
                "🔙 মূল মেনু",
                callback_data="home"
            )
        ],
    ]

    await query.edit_message_text(
        text,
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def home(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    await query.edit_message_text(
        "🌐 *অনলাইন সার্ভিস সেন্টার*\n\n"
        "আপনার প্রয়োজনীয় সার্ভিস নির্বাচন করুন 👇",
        parse_mode="Markdown",
        reply_markup=main_menu()
    )


def main():
    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN environment variable is missing!")

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    app.add_handler(
        CallbackQueryHandler(home, pattern="^home$")
    )

    app.add_handler(
        CallbackQueryHandler(
            service_details,
            pattern="^(facebook|verification|bybit|ads|social|youtube|website|recovery|other)$"
        )
    )

    print("🤖 Online Seba User Bot is running...")

    app.run_polling()


if __name__ == "__main__":
    main()

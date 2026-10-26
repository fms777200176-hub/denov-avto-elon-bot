import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

TOKEN = os.getenv("BOT_TOKEN")

CHANNEL_URL = "https://t.me/denov_avto_savdo"
ADMIN_URL = "https://t.me/DAS_Admin"

SHARTLAR = (
    "📋 DENOV AVTO SAVDO — E'LON BERISH SHARTLARI\n\n"
    "✅ E'lon berish mutlaqo BEPUL!\n"
    "👥 Kanalimizga 5 ta a'zo qo'shing.\n"
    "🚗 E'loningizni joylashtirish uchun admin bilan bog'laning.\n\n"
    "⚠️ E'loningizdagi ma'lumotlar to'g'ri bo'lishi kerak."
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton(
                "✅ Ha, e'lon bermoqchiman",
                callback_data="elon"
            )
        ],
        [
            InlineKeyboardButton(
                "📢 Kanalga o'tish",
                url=CHANNEL_URL
            )
        ],
    ]

    await update.message.reply_text(
        "Assalomu alaykum! 👋\n\n"
        "🚗 DENOV AVTO SAVDO kanaliga e'lon bermoqchimisiz?\n\n"
        "🆓 E'lon joylash mutlaqo bepul!",
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


async def button_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    query = update.callback_query
    await query.answer()

    if query.data == "elon":
        keyboard = [
            [
                InlineKeyboardButton(
                    "📢 Kanalga o'tish",
                    url=CHANNEL_URL
                )
            ],
            [
                InlineKeyboardButton(
                    "👨‍💼 Admin bilan bog'lanish",
                    url=ADMIN_URL
                )
            ],
            [
                InlineKeyboardButton(
                    "🏠 Bosh menyu",
                    callback_data="menu"
                )
            ],
        ]

        await query.edit_message_text(
            SHARTLAR
            + "\n\n👇 Shartlar bilan tanishib chiqing.",
            reply_markup=InlineKeyboardMarkup(keyboard),
        )

    elif query.data == "menu":
        keyboard = [
            [
                InlineKeyboardButton(
                    "✅ Ha, e'lon bermoqchiman",
                    callback_data="elon"
                )
            ]
        ]

        await query.edit_message_text(
            "🚗 DENOV AVTO SAVDO\n\n"
            "E'lon berish mutlaqo bepul!",
            reply_markup=InlineKeyboardMarkup(keyboard),
        )


def main():
    if not TOKEN:
        raise RuntimeError("BOT_TOKEN sozlanmagan!")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    app.run_polling()


if __name__ == "__main__":
    main()

import os
import asyncio
import edge_tts
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

# BotFather থেকে পাওয়া আপনার আসল টোকেনটি এখানে বসান
TOKEN = "8350459258:AAEEDN6PcBj70hLroj_XURexdPS2D0OLluQ" 

async def handle_msg(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    file_name = "voice.mp3"
    
    try:
        # উন্নত মানের ব্রিটিশ কণ্ঠ ব্যবহার করা হচ্ছে
        communicate = edge_tts.Communicate(text, "en-GB-LibbyNeural")
        await communicate.save(file_name)
        
        # অডিও ফাইলটি টেলিগ্রামে পাঠানো
        with open(file_name, 'rb') as audio:
            await update.message.reply_voice(voice=audio)
            
        os.remove(file_name)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT, handle_msg))
    
    print("বটটি এখন চালু হচ্ছে...")
    app.run_polling()


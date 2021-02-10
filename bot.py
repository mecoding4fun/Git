import telebot
from telebot import types
bot = telebot.TeleBot("1642788628:AAExN4YFdDnZJfLk85DAsba8CY4BeaijBg0")

name = ''

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(commands=['members'])
def promote_User(message):
    # bot.kick_chat_member(message.chat.id, message.from_user.id)
    ChatMemberCount = bot.get_chat_members_count(message.chat.id)
    bot.send_message(message.chat.id, 'Members Present in chat: '+str(ChatMemberCount))

@bot.message_handler(commands=['diceroll'])
def Dice(message):
    bot.send_dice(message.chat.id)

@bot.message_handler(commands=['target'])
def target(message):
    bot.send_dice(message.chat.id,'🎯')

@bot.message_handler(commands=['goal'])
def ball(message):
    bot.send_dice(message.chat.id,'⚽️')

# @bot.message_handler(commands=['prom'])
# def perm(message):
#     bot.promote_chat_member(message.chat.id,message.from_user.id,True,False,None,False,True,True,True,False)
#     bot.send_message(message.chat.id,'Successfully promoted user, Now tell the user to give party')

# @bot.message_handler(commands=['demote'])
# def dem(message):
#     bot.promote_chat_member(message.chat.id,message.from_user.id,False,False,False,False,False,False,False,False)

@bot.message_handler(commands=['prom'])
def perm(message):
    
    bot.send_message(message.chat.id,Getid)

@bot.message_handler(commands=['id'])
def sendId(message):
    bot.send_message(message.chat.id,message.from_user.id)

@bot.message_handler(commands=['leave'])
def leave_User(message):
    bot.send_message(message.chat.id,'Bye Bye')
    bot.leave_chat(message.chat.id)    

# @bot.message_handler(commands=['tts'])
# def TTS(message):
#     name = message.text.split()
#     bot.send_voice(message.chat.id,)

@bot.message_handler(commands=['poll'])
def Polle(message):
    bot.send_poll(message.chat.id,'What you want?',['Nothing','Get lost','🎯'])

@bot.message_handler(commands=['chatname'])
def ChatPhot(message):
    name = message.text.split()
    if(name[1] != '' and name[2] ==' '):
        bot.set_chat_title(message.chat.id,name[1])  
    elif(name[1] != '' and name[2] !=' '):
         bot.set_chat_title(message.chat.id,name[1]+' '+name[2])   
    # keyboard = types.InlineKeyboardMarkup()
    # key_yes = types.InlineKeyboardButton(text='Commands', callback_data='yes')
    # key_no = types.InlineKeyboardButton(text='Details', callback_data='no')
    # keyboard.add(key_yes)
    # keyboard.add(key_no)
    bot.send_message(message.chat.id,'Lol bye bye '+str(message.from_user.id))
    # bot.send_message(message.chat.id,message.from_user.id,reply_markup=keyboard)

    


@bot.message_handler(commands=['mes'])
def ask(message):
    bot.send_message(message.chat.id,'Send a new name')
    bot.register_next_step_handler(message, get_name)

def get_name(message):
    global names
    names = message.text
    bot.send_message(message.chat.id,'Confirm?')
    bot.register_next_step_handler(message, get_confirm)

def get_confirm(message):
    global opi 
    opi = message.text
    global name
    if (opi == 'Yes' or opi == 'yes'):
        name = names
    elif (opi == 'No' or opi ==' no'):
        bot.register_next_step_handler(message, ask)

    
bot.polling()
#!/bin/python3

import sys
import telethon
import json


assert len(sys.argv) >= 2, "you have to set *.json file with creds as first argument of the program"


cred_filename = sys.argv[1]
cred_file = open(cred_filename, "r")
cred_obj = json.load(cred_file)
cred_file.close()


client_session_name = cred_obj["client_session_name"]
bot_session_name = cred_obj["bot_session_name"]

api_id = cred_obj["api_id"]
api_hash = cred_obj["api_hash"]
bot_token = cred_obj["bot_token"]


bot = telethon.TelegramClient(bot_session_name, api_id, api_hash).start(bot_token = bot_token)
client = telethon.TelegramClient(client_session_name, api_id, api_hash)


description = """
Hello, I'm a clear bot.
Just print /clear command for remove all history from the chat
"""


@bot.on(telethon.events.NewMessage(pattern = "/start"))
async def start(event):
  await event.respond(description)
  raise telethon.events.StopPropagation


@bot.on(telethon.events.NewMessage(pattern = "/clear"))
async def clear(event):
  try:
    chat_id = event.chat_id
    last_message_id = event.message.id
    current_user_id = int(event.from_id.user_id)


    # check that user is admin of the chat
    is_admin = False
    async for user in bot.iter_participants(entity = chat_id,
        filter = telethon.types.ChannelParticipantsAdmins):
      if (user.id == current_user_id):
        is_admin = True
        break

    if is_admin == False:
      await event.respond("sorry, but you are not admin of the chat")
      raise telethon.events.StopPropagation


    # check connection
    await client.connect()


    # get list message ids for removing
    list_for_remove = []
    async for message in client.iter_messages(chat_id):
      list_for_remove.append(message.id)


    # remove messages
    await client.delete_messages(entity = chat_id, message_ids = list_for_remove)


    # finish
    await event.respond("done")
    raise telethon.events.StopPropagation

  except telethon.events.StopPropagation:
    raise
  except:
    print(sys.exc_info())
    await event.respond("some error caused")
    raise


def main():
  # need for authorizate session
  with client:
    client.loop.run_until_complete(client.connect())

  # run the bot
  bot.run_until_disconnected()


main()

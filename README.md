# bot for removing messages in telegram chat


## Dependencies

- telethon
- Python JSON


## Usage

For using this scripts you need user permissions, so you have to authorize
user session. For it you need:

1. Create json creds file (see [template](creds.json.templete)) file with next properties:
  - `api_id` - get from [development](https://my.telegram.org)
  - `api_hash` - get with previous values
  - `client_session_name` - just a string, set it as you want
  - `bot_tokne` - need for bot usage, see below
  - `bot_session_name` - also need ofr bot usage

2. And authorize this session by [auth_session script](scripts/auth_session)


## Bot Usage

__NOTE__ you need authorized user session

1. Add to creds file next properties:
  - `bot_token` - get by bot father
  - `bot_session_name` - just a string, set it as you want

2. Start [clear_bot](scripts/clear_bot) with one argument: filename of your
config file

3. Add this bot to your chat

4. Print `/clear` command ( __NOTE__ you must be admin of the chat)


## Clear chat

__NOTE__ you need authorized user session
__NOTE__ you must be admin of the chat

Just start [clear_chat](scripts/clear_chat) with two args:
  - your creds file
  - chat name that you need clear



## Note

Telegram bot can't request chat history, so it a problem for removing messages
by bot. So I use user permission for removing chat history

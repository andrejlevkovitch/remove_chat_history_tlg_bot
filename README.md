# bot for removing messages in telegram chat

## Usage

1. Create json [config](config.json.templete) file with next properties:
  - `api_id` - get from [development](https://my.telegram.org)
  - `api_hash` - get with previous values
  - `bot_token` - get by bot father
  - `bot_session_name` - just a string, set it as you want
  - `client_session_name` - just a string, set it as you want

2. Start [program](main.py) with one argument: filename of your config file

3. If you start it at first time, then you need authenticate. Program print that
you need input your telephone number - put you telephon number and after it
you get verification code in you telegram. Type this code to the program. Note
that this user, by that you authorized, must has admin permission in target chat

4. Add this bot your chat

5 Print `/clear` command


## Note

Telegram bot can't request chat history, so it a problem for removing messages
by bot. So I use user permission for removing chat history

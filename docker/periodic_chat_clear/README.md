# Usage

1. Add to [creds](creds) directory you cred file. __NOTE__ that name of file
must be creds.json

2. Authorize your user session. __NOTE__ that session file must be also in creds
directory

3. Create .env file and set in it your chat name as:

```bash
CHAT_NAME="your chat name"
```

4. Start docker with command:

```bash
docker-compose -f periodic_chat_clear.yaml up
```

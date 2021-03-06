# Usage

1. [Authorize](../../scripts/auth_session) your user session.
__NOTE__ session file must be also in [creds](../../creds) directory
__NOTE__ cred file must be named as `creds.json`

2. Create .env file and set in it your chat name as:

```bash
CHAT_NAME="your chat name"
```

3. Start docker with command:

```bash
docker-compose -f periodic_chat_clear.yaml up
```

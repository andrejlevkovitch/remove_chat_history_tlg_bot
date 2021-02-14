# docker-compose scripts


## Authorization by docker

If you can't authorize on your system, you can authorize by docker container.
For it you need start docker container with authorization script and your creds.
Command looks like:

```bash
docker run -v /path/to/creds:/creds -v /path/to/auth_session:/bin/auth_session -w /creds -it container_name creds.json
```

You need set `/path/to/creds` as path to creds directory and `/path/to/auth_session`
as path to auth_session script. __NOTE__ that `-v` not accepts relative paths!
Also set valid container_name. After it you need input your telephone number
and special code from telegram


## Windows

__NOTE__ that if you try start docker images on windows you can have a problem
with `\r\n`. So you need convert files in `scripts` directory by `dos2unix`.

# Backuper

Backup a discord chat.

## Quick Start

Create a `.env` file containing the environment variables `DISCORD_PREFIX` and `DISCORD_TOKEN`. Then run:

```console
$ ./build.sh run
```

To backup a chat, run the command `!backup` in the chat you would like to backup. The bot will stop running and backup everything into the folder `assets` and `messages.json`.

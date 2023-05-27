# Backuper

<p align="center">
  <br>
    <img alt="logo" src="./backuper.png" height="272" />
  <br>
  Backup a discord chat
<p>

## Quick Start

Create a `.env` file containing the environment variables `DISCORD_PREFIX` and `DISCORD_TOKEN`. Then run:

```console
$ ./build.sh run
```

To backup a chat, run the command `!backup` in the chat you would like to backup. The bot will stop running and backup everything into the folder `assets` and `messages.json`.

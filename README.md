# YoutubeBot - a self-hosted Discord bot for playing YouTube videos
## Commands
- `.play {url or search}` - plays or queues a video, and joins VC if it's not already there.
    - alternate: `.p`
- `.skip {n}` - skips `n` videos. Without `n`, skips only once. `.skip all` will skip every song and leave the VC.
    - alternate: `.s`
- `.queue` - shows a list of titles queued for playback
    - alternate: `.q`

## Getting started
Recently, some of the major Discord bots designed to play YouTube videos (Rythm and Groovy to name a few) have been taken down by Google for copyright infringment. This means that I can't just give you a bot to add to your server, but I can give you the code to run on your own bot, which you can add to your server. Don't worry, this is a pretty straightforward process.

A word of warning before we start though: you'll need somewhere to host the bot. Something you can leave on - a Raspberry Pi connected to your home network, an AWS server, a home server, or something similar - would be ideal. A static IP is not required.

### Step 1: Creating an empty bot
1. First, head to Discord's [developer portal](https://discord.com/developers/applications).
2. Sign in if it asks you to, then you should see a screen with a "New Application" button in the top right corner. Click it.
3. Give your bot a name - I called mine "YoutubeBot", you can call yours whatever you want. This isn't super important, because you'll be giving it a username later.
4. After you hit "Create", you should see some general info about your bot. You can edit this if you want - give it a name, profile picture, about me, etc - use the profile picture in this repo if you want, or make your own, or don't bother.
5. Navigate to the "Bot" tab in the sidebar. From here you can give it a username - this is what it will show up as in your server.
6. On this page activate the "Message Content Intent" toggle. This is so the bot can read the content of the commands. Make sure to save your changes!

### Step 2: Adding it to your server
1. Now that you have a bot, it's time to add it to your server. Go to the "OAuth2" page from the same sidebar.
2. Under "URL generator" select the "bot" checkbox, then under "Bot Permissions" select "Administrator". The only reason it needs administrator privileges is to join private VCs if requested by someone in them. I promise the bot won't do anything spooky with these perms, and you can check the code for yourself if you want, but if you're okay with it not working in private VCs then you can choose "Send Messages", "Connect", and "Speak", which will allow it to join any VCs its role permits.
3. Hit "Copy" next to the URL that got generated and paste it into your browser, then select your server from the dropdown and complete the captcha.

### Step 3: Making it do stuff
1. You now have a bot, and it's in your server, but it's not doing much. You'll want to do this bit on something that can be left on all the time, as I mentioned earlier.
2. Download the code. You can do this by downloading the zip and unzipping it, or with a `git clone` command, or however you prefer to get GitHub content.
3. Make sure you have Python 3.8 or later installed.
4. Open up a console wherever you downloaded the code to (don't forget to unzip it if it's zipped), and run `pip install -r requirements.txt`
5. Create a copy of the ".env_example" file named ".env"
6. Head back to the "Bot" page. Click "Reset Token", then click "Copy". This will copy your bot's unique token so that the code can identify itself as the bot you've just created.
7. Edit ".env" and replace "your-token-goes-here" with the token you just copied.
8. Run `nohup ./youtubebot.py &` on Linux/Unix or `python youtube.py` on Windows (note that on Windows, if you close the console your bot will stop). For Linux/Unix: if you get an error along the lines of "permission denied" or "not executable", run `chmod +x youtubebot.py` to make it executable and try again.
9. The bot is now running. To stop it, run `pkill -f youtubebot.py` on Linux/Unix or press `ctrl+c` while clicked into your console on Windows.

Congrats! You should now be able to use the bot by joining a VC and using the commands above. If not, let me know and I'll try to help as best I can.

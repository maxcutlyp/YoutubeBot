## Integration with systemd

If you want to use the bot on your systemd machine you have to create a systemd unit for it. You can use the `youtubebot.service` example in this file.

Decide if you want to use it inside your user session or system session. 

User folder: `~/.config/systemd/user/youtubebot.service`  
System folder: `/etc/systemd/system/youtubebot.service`

## Using Python virtual env

If you are using a virtual environment for the bot change the ExecStart= so it points to the path of the virtualenv python binary. 

## Usage
If you use the system installation, don't use the `--user` parameter. 

### Starting
`systemctl --user start youtubebot.service`

### Stoping
`systemctl --user stop youtubebot.service` 

### Autostart
`systemctl --user enable youtubebot.service`

### View logs
`journactl --user youtubebot.service`



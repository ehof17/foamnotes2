
### I have 2 files..
```
ls ~/.cloudflared/config.yml
```

```
/etc/cloudflared/config.yml
```

### Check which one is actually being used
```
sudo systemctl status cloudflared
```

spat out

```
Loaded: loaded (/etc/systemd/system/cloudflared.service; enab>
     Active: active (running) since Mon 2026-04-27 02:37:17 BST; 1>
 Invocation: b0f9e55d8b964eb693b01af9838d682d
│   Main PID: 2899643 (cloudflared)
      Tasks: 11 (limit: 3918)
│        CPU: 3h 9min 18.903s
     CGroup: /system.slice/cloudflared.service
│             └─2899643 /usr/bin/cloudflared --no-autoupdate --conf>

Jun 04 19:52:35 raspberrypi cloudflared[2899643]: 2026-06-04T18:52>
Jun 04 19:52:35 raspberrypi cloudflared[2899643]: 2026-06-04T18:52>
Jun 04 19:52:37 raspberrypi cloudflared[2899643]: 2026-06-04T18:52>
Jun 04 19:52:37 raspberrypi cloudflared[2899643]: 2026-06-04T18:52>
Jun 04 19:52:37 raspberrypi cloudflared[2899643]: 2026-06-04T18:52>
Jun 04 19:52:50 raspberrypi cloudflared[2899643]: 2026-06-04T18:52>
Jun 04 19:52:50 raspberrypi cloudflared[2899643]: 2026-06-04T18:52>
Jun 05 02:37:17 raspberrypi cloudflared[2899643]: 2026-06-05T01:37>
lines 1-18
```

ehof@raspberrypi:~ $ sudo systemctl cat cloudflared
# /etc/systemd/system/cloudflared.service
[Unit]
Description=cloudflared
After=network-online.target
Wants=network-online.target
[Service]
TimeoutStartSec=15
Type=notify
ExecStart=/usr/bin/cloudflared --no-autoupdate --config /etc/cloudflared/config.yml tunnel run
Restart=on-failure
RestartSec=5s


So we know the file to edit is /etc/cloudflared/config.yml

- When trying to edit, /etc/cloudflared/config.yml
W10: Warning: Changing a readonly file


So i instead edited 
 ~/.cloudflared/config.yml

 But that didnt work
 so i just copied it over
 
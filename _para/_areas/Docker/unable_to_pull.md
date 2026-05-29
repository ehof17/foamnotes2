I was unable to pull image on my pi
Get "https://ghcr.io/token?scope=repository%3Ablakeblackshear%2Ffrigate%3Apull&service=ghcr.io": dial tcp: lookup ghcr.io on 192.168.0.1:53: no such host

Doing this
```
echo "nameserver 8.8.8.8" | sudo tee /etc/resolv.conf
```
router (192.168.0.1) was failing to resolve ghcr.io.
By writing 8.8.8.8 (Google's DNS) to /etc/resolv.conf, that tells the Pi to ask Google directly instead of asking router, which worked fine.

/etc/resolv.conf is just the file Linux checks to know "who do I ask when I need to look up a domain name."

Making the fix permananet: 
Update the network im on
```
nmcli con show
```
Melon              x  wifi      wlan0

nmcli con mod "Melon" ipv4.dns "8.8.8.8 1.1.1.1"
nmcli con up "Melon"
```


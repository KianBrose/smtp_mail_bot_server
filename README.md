
# Custom domain SMTP mail bot server

Long name isn't it, it's basically just a program meant to be able to read email contents from one of your custom domains/websites so that you can automate something with it, like a verification bot or something idk up to you


## Why

Long story short, refferal type giveaways were pissing me off since they're unfair to people with few friends when compared to influencers that abuse the refferal system, so a modified version of this was used to 

## [Full video about this project available here](https://youtu.be/UTqAF8VgBxM)
I made a video about this, you should watch it [here](https://youtu.be/UTqAF8VgBxM)
## Features

- Read mail from a custom domain
- Fully self hosted, no rate limits, payments or restrictions


## Deployment

To use this you need to buy a domain. Then add the following DNS records:

I'll assume that you are running this with

- Public ip: 210.210.210.210 (You can find yours here https://4.ident.me/)
- Localhost ip: 192.168.0.10 (Open a console and write `ip a` or `ifconfig` on mac/linux, and `ipconfig` on windows. It starts with 192.168 and is naer your public ip)
- Domain: example.com

### DNS records
Add the following DNS records on your registrar, I recommend [cloudflare](https://cloudflare.com/)
```bash
Type: A
Name: example.com
Content/Value: 210.210.210.210
TTL: Automatic
```

```bash
Type: MX
Name: example.com
Content/Value: example.com
Priority: 10
TTL: Automatic
```
### Port forwarding
On whatever computer you are running you will have to make sure your router is port forwarded for the port 25 and routes its traffic to the private ip of where the code will run. If it will run on 192.168.0.10, port forward 192.168.0.10 port 25. If you don't know how to do it your ISP might be blocking you or your router is just bad, there are tons of guides online, even on my channel.

### Code changes
In the `handle_RCPT` function, change the domain `kianbrose.com` to `example.com` (obviously yours in there)

At the bottom of the script, change the `hostname='192.168.x.x'` set it to your own private ipv4 ONLY IF 0.0.0.0 RESULTS IN PORT FORWARDING NOT WORKING (Sometimes some operating systems ask that you explicitly use the 192.168 address otherwise port forwarding does not work, like windows)

## Running
It will probably complain if you don't use sudo permissions, run as admin on windows or on mac/linux `sudo python main.py`
## Authors

- [KianBrose (YouTube)](https://www.youtube.com/KianBrose)


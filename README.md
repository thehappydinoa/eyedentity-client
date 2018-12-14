# eyedentity-client

The client for [thehappydinoa/eyedentity](https://github.com/thehappydinoa/eyedentity)

## Auto-Startup

```bash
cp -rp /home/pi/cache/ /home/pi/.cache;
cd /home/pi/eyedentity-client/;
git pull;
python3 render_frames.py;
cp -nrp /home/pi/.cache/ /home/pi/cache;
python3 client.py;
```

## Resources

![blink](blink.gif)

![bars](bars.gif)

![thank-you](thank-you.gif)

![error](error.gif)

# eyedentity-client

The client for [thehappydinoa/eyedentity](https://github.com/thehappydinoa/eyedentity)

## Auto-Startup

```bash
echo "Copying cache to .cache"
cp -nrp /home/pi/cache/ /home/pi/.cache;
cd /home/pi/eyedentity-client/;
echo "Pulling from GitHub"
git pull;
echo "Updating dependencies"
pip3 install -r requirements.txt
echo "Rendering frames"
python3 render_frames.py;
echo "Copying .cache to cache"
cp -nrp /home/pi/.cache/ /home/pi/cache;
echo "Starting client.py"
python3 client.py;
```

## Resources

![blink](blink.gif)

![bars](bars.gif)

![thank-you](thank-you.gif)

![error](error.gif)

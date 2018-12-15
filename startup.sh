echo "Copying cache to .cache";
cp -rp /home/pi/cache/ /home/pi/.cache;
cd /home/pi/eyedentity-client/;
echo "Pulling from GitHub";
git pull;
echo "Updating dependencies";
pip3 install -r requirements.txt
echo "Rendering frames";
python3 render_frames.py;
echo "Copying .cache to cache";
cp -nrp /home/pi/.cache/ /home/pi/cache;
echo "Starting client.py";
python3 client.py;

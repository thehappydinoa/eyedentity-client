import glob

import client

for gif in glob.glob("*.gif"):
    client.gif(gif)

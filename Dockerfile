from ubuntu

run apt-get update && apt-get install python3.8 python3-pip git  -y
#run apt-get update && apt-get install ffmpeg -y

#WORKDIR /mnt/host/source/mobot
#run pip3 install -r requirements.txt
run python3 -m pip install -U discord.py

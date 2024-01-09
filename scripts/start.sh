#!/bin/bash
cd /
cd /home/raati/rasp/mirror/
python app.py
# open info screen 
chromium-browser --kiosk http://127.0.0.1:5000/

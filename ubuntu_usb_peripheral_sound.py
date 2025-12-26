#!/usr/bin/env python3

import pyudev
import subprocess
import time

# Create a context to monitor USB devices
context = pyudev.Context()
monitor = pyudev.Monitor.from_netlink(context)
monitor.filter_by(subsystem='usb')

# Path to the sound you want to play
sound_file = "/usr/share/sounds/freedesktop/stereo/alarm-clock-elapsed.oga"

print("Listening for USB devices...")

# Loop specifically monitors for the 'usb_device' type to avoid 
# triggering multiple times for a single plugin (e.g., interfaces/endpoints)
for device in iter(monitor.poll, None):
    if device.action == 'add' and device.get('DEVTYPE') == 'usb_device':
        print(f"Device connected: {device.get('ID_MODEL', 'Unknown')}")
        # Use paplay (PulseAudio Play) for best compatibility
        subprocess.run(['paplay', sound_file])

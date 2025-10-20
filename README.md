# MIDICaptain_Nano4_PySwitchLooper
Custom Firmware for Nano 4 and Ableton Live Surface Script for looping

Firmware is based on PySwitch by Tunetown, it communicates with Albeton Live and correctly displays the current state of the Session Recording.

## Installation Ableton
1. Place MIDICaptain_Nano4_PySwitchLooper folder inside C:\Users\[User]\Documents\Ableton\User Library\Remote Scripts

## Installation MidiCaptain
1. Connect you device to your computer via USB and power it up. For PaintAudio MIDICaptain controllers, press and hold switch 1 while powering up to tell the controller to mount the USB drive.
2. On your computer, you should now see the USB drive of the device (named MIDICAPTAIN for Paintaudio controllers, CIRCUITPY for generic boards)
3. Delete the whole content of the USB drive. For PaintAudio devices, dont forget to save the contents on your hard drive (especially the license folder) if you perhaps want to restore the original manufacturer firmware later.
4. Copy everything inside the "content" folder of the project to the root folder on your device drive (named MIDICAPTAIN or CIRCUITPY).
5. Unmount the USB drive (important: wait until the drive really is unmounted, or it will sometimes forget everything again).
6. Reboot the device.

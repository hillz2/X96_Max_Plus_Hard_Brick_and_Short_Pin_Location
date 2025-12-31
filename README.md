# X96 Max Plus Hard Brick and Short Pin Location
X96 Max Plus Hard Brick and Short Pin Location

I once hard bricked my X96 Max Plus and I had to find the short pin location through trial & error. So I created this repository as a reminder for me if it happens again in the future.

## My X96 Max Plus board looks like this:

![X96 Max Plus Board](https://github.com/hillz2/X96_Air_Hard_Brick_and_Short_Pin_Location/blob/main/whole_board.jpg)

## The short pin location is squared in red below
![enter image description here](https://github.com/hillz2/X96_Air_Hard_Brick_and_Short_Pin_Location/blob/main/short%20pin%20location.jpg)

## Close up view of the short pin location
![enter image description here](https://github.com/hillz2/X96_Air_Hard_Brick_and_Short_Pin_Location/blob/main/short_pin_close_up.jpg)

## As you can see, my WiFi chipset is *AM7256D*. This is important if you wanna flash OpenWrt to EMMC, choose the right script that matches your board's wifi chipset

You can use a screwdriver or a tweezer to short the two pins. 
1. You don't have to connect the board with an a power adapter, just use a male to male USB cable connected to the USB 3.0 port of the board.
2. Tutorial on how to unbrick your device (In Indonesian) [Fix: X96 Max Plus Bricked](https://github.com/hillz2/X96_Air_Hard_Brick_and_Short_Pin_Location/blob/main/Fix%20X96%20Max%20Plus%20Bricked%20(Short%20Pin%20Tutorial).mp4) (Don't use the firmware in that video to flash your X96 Max Plus)
3. If you encounter ROMCODE error, follow this tutorial (In Indonesian) [Fix: ROMCODE Error X96 Max Plus](https://github.com/hillz2/X96_Air_Hard_Brick_and_Short_Pin_Location/blob/main/Fix%20HG680P%20%26%20X96%20Max%20Plus%20Error%20ROMCODE.mp4)
4. The firmware that I used is SlimBox ROM (X96 Max Plus A100), you can download it in the release page of this repository 
5. If later you wanna flash openwrt on X96 Max Plus, you can use RTA-WRT firmware, you can download it in the release page as well
6. All the tools can be downloaded in this repository.

Don't flash OpenWrt Firmware on your bricked X96 Max Plus right away! Flash the Android Firmware first then proceed to flash OpenWrt to your SD card

# UPDATE 04 SEPTEMBER 2023:
1. LAN port doesn't work, use a **USB to LAN** to connect to ethernet
2. USB 3.0 port is buggy with openwrt
3. You can use any openwrt firmware (I personally use RTA-WRT).
4. To install OpenWrt to EMMC:
   1. Make sure your device is installed with Android **NOT** OpenWrt
   2. Burn the openwrt image to an SD card then boot from it.
   3. Run `openwrt-install-amlogic`
   4. Choose `505:X96-Max+_A100:s905x3: 4GB-Mem,32G-Rom,Wifi-AM7256,100Mb-Nic`
   5. Choose to write mainline bootloader to EMMC
   6. After it's done then remove the SD card and unplug the power cable.
  
# UPDATE 26 DECEMBER 2025, OPENWRT INSTALLATION TUTORIAL:
1. Download RTA-WRT firmware from the release page
2. Extract it then burn the image to an SD card
3. *IMPORTANT*. If you wanna install RTA-WRT to the EMMC, do it from the terminal window, not from the Luci web interface, it'll brick your TV Box, here's how:
4. Run `openwrt-install-amlogic`
5. Choose `505:X96-Max+_A100:s905x3: 4GB-Mem,32G-Rom,Wifi-AM7256,100Mb-Nic`
6. Choose to write mainline bootloader to EMMC
7. Choose `btrfs` file system or `ext4`
8. After it's done then remove the SD card and unplug the power cable.

# DTB file that matches my TV Box:
You won't be able to boot to OpenWrt if you don't use the correct dtb file
```
root@at-home:~ #  cat /boot/uEnv.txt 
LINUX=/zImage
INITRD=/uInitrd
FDT=/dtb/amlogic/meson-sm1-x96-max-plus-a100.dtb
APPEND=root=UUID=8b4a8c39-0a98-4f3e-8ff0-d1979bbdfffb rootfstype=btrfs rootflags=compress=zstd:6 console=ttyAML0,115200n8 console=tty0 no_console_suspend consoleblank=0 fsck.fix=yes fsck.repair=yes net.ifnames=0 cgroup_enable=cpuset cgroup_memory=1 cgroup_enable=memory swapaccount=1
```
`meson-sm1-x96-max-plus-a100.dtb` can be downloaded in the repository

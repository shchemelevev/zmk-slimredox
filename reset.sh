#!/bin/bash

/Users/e_shchemelev/.pyenv/shims/python /Users/e_shchemelev/develop/zmk/syspass_gen.py > /Users/e_shchemelev/develop/zmk/app/include/syspass.h
cd /Users/e_shchemelev/develop/zmk
source /Users/e_shchemelev/.virtualenvs/zmk_keyring/bin/activate
cd /Users/e_shchemelev/develop/zmk/app
west build -p -b nice_nano_v2 -- -DSHIELD=settings_reset -DZMK_CONFIG=/Users/e_shchemelev/develop/zmk-slimredox/config
# west build -p -b nice_nano_v2 -S zmk-usb-logging  -- -DSHIELD=slimredox_left -DZMK_CONFIG=/Users/e_shchemelev/develop/zmk-slimredox/config

until [ -d /Volumes/NICENANO ]
do
  echo "not found"
     sleep 1
done
echo "Nice!Nano connected. Writing firmware..."
cp build/zephyr/zmk.uf2 ~/zmk/slimredox_reset.uf2
cp build/zephyr/zmk.uf2 /Volumes/NICENANO/slimredox_reset.uf2

rm /Users/e_shchemelev/develop/zmk/app/include/syspass.h
osascript -e 'display notification "build complete" with title "zmk"'

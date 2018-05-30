#!/bin/bash

dev_addr=$(udevadm info -q all /dev/swallow | grep DEVPATH |  grep -o "usb1/[0-9-]\+" | sed -e 's/usb1\///')
echo $dev_addr | tee /sys/bus/usb/drivers/usb/unbind
sleep 3
echo $dev_addr | tee /sys/bus/usb/drivers/usb/bind
echo "OK, don\`t forget to restart swallow-weewx service"

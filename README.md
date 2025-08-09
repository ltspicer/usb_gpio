# USBgpio

Add Python programmable GPIO pins to any computer with USBgpio.

![](https://github.com/ltspicer/usb_gpio/blob/main/media/logo_sm.jpg)

## How It Works

USBgpio provides 12 GPIO pins via a USB port on any modern computer. There is also an accompanying [Python library](https://github.com/ltspicer/usb_gpio/blob/main/usbgpio.py) that controls the GPIO pins with simple commands.

Available digital pins: 2 to 13

Available servo pins: 2 to 9

This brief example demonstrates the basics of using USBgpio (demo.py):

```(https://github.com/ltspicer/usb_gpio/blob/main/demo.py)```

The [firmware](https://github.com/ltspicer/usb_gpio/blob/main/usb_gpio_arduino/usb_gpio_arduino.ino) waits for serial data, which is received via USB and triggered by the Python program. The firmware then decodes the received data and performs the requested action, be it setting a pin direction or a voltage level or servo control. When a pin is read, the Arduino also sends this value back to the Python program via the serial connection (USB).

## Parts

- 1 x Arduino Nano
- 1 x USB-A to micro USB-B cable

## About the Author

[Nick A. Bild, MS](https://nickbild79.firebaseapp.com/#!/) forked by [spicer](https://www.ltspiceusers.ch/)

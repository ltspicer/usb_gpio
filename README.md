# USBgpio

Add Python programmable GPIO pins to any computer with USBgpio.

![](https://github.com/ltspicer/usb_gpio/blob/main/media/logo_sm.jpg)

## How It Works

USBgpio provides 12 GPIO pins via a USB port on any modern computer. There is also an accompanying [Python library](https://github.com/ltspicer/usb_gpio/blob/main/usbgpio.py) that controls the GPIO pins with simple commands.

Available digital pins: 2 to 13 (input or output)

Available servo pins: 2 to 9 (only output)

This brief example demonstrates the basics of using USBgpio (demo.py):

```python
from usbgpio import USBgpio
import time

# Establish a serial connection to the device.
gpio = USBgpio('/dev/ttyUSB0', 115200)
time.sleep(1)       # Important!!! --- Wichtig!!!

# Set GPIO pin as output
ledPIN = 13         # 13 is the onboard LED
gpio.set_output(ledPIN)

# Set GPIO pin as input
inputPIN = 3
gpio.set_input(inputPIN)

# Set servo pin & activate (attach) it
servoPIN = 8
gpio.servo_attach(servoPIN)

while True:
    # Alternate between high and low voltage levels to blink an LED
    # Toggle servo from 0° to 180°
    gpio.digital_write(ledPIN, "HIGH")  # LED on
    gpio.servo_write(servoPIN, 0)       # Move servo to 0°
    time.sleep(1)
    gpio.digital_write(ledPIN, "LOW")   # LED off
    gpio.servo_write(servoPIN, 180)     # Move servo to 180°
    time.sleep(1)

    # Read the value of a pin and print the result.
    print(gpio.digital_read(inputPIN))

# Detach servo
gpio.servo_detach(servoPIN)
```

The [firmware](https://github.com/ltspicer/usb_gpio/blob/main/usb_gpio_arduino/usb_gpio_arduino.ino) waits for serial data, which is received via USB and triggered by the Python program. The firmware then decodes the received data and performs the requested action, be it setting a pin direction or a voltage level or servo control. When a pin is read, the Arduino also sends this value back to the Python program via the serial connection (USB).

The library usbgpio.py must be in the same directory than the Python code.

## Use

Connect the "Arduino Nano" **via USB to PC**. Flash the [firmware](https://github.com/ltspicer/usb_gpio/blob/main/usb_gpio_arduino/usb_gpio_arduino.ino) to the "Arduino nano" device with **Arduino IDE**

and have fun

## Parts

- 1 x Arduino Nano ( https://de.aliexpress.com/item/1005006472746115.html >> less than 3$ )

## About the Author

[Nick A. Bild, MS](https://nickbild79.firebaseapp.com/#!/) forked by [spicer](https://www.ltspiceusers.ch/)

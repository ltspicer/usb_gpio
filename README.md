# USBgpio

Add Python programmable GPIO pins to any computer with USBgpio.

![](https://github.com/ltspicer/usb_gpio/blob/main/media/logo_sm.jpg)

## How It Works

USBgpio provides 12 GPIO pins via a USB port on any modern computer. There is also an accompanying [Python library](https://github.com/ltspicer/usb_gpio/blob/main/usbgpio.py) that controls the GPIO pins with simple commands.

Available digital pins: 2 to 13

Available servo pins: 2 to 9

This brief example demonstrates the basics of using USBgpio:

```python
from usbgpio import USBgpio
import time


# Establish a serial connection to the device.
gpio = USBgpio('/dev/ttyUSB0', 115200)
time.sleep(1)       # Important!!! --- Wichtig!!!

# Set GPIO direction & set as output
ledPIN = 2
gpio.set_output(ledPIN)

# Set input pin
inputPIN = 3
gpio.set_input(inputPIN)

# Activate servo & set pin
servoPIN = 8
gpio.servo_attach(servoPIN)

while True:
    # Alternate between high and low voltage levels to blink an LED
    # Toggle servo from 0° to 180°
    gpio.digital_write(ledPIN, "HIGH")
    gpio.servo_write(servoPIN, 0)     # Set servo to 0°
    time.sleep(1)
    gpio.digital_write(ledPIN, "LOW")
    gpio.servo_write(servoPIN, 180)   # Set servo to 180°
    time.sleep(1)

    # Read the value of a pin and print the result.
    print(gpio.digital_read(inputPIN))
gpio.servo_detach(servoPIN)
```

The [firmware](https://github.com/ltspicer/usb_gpio/blob/main/usb_gpio_arduino/usb_gpio_arduino.ino) waits for serial data, which is received via USB and triggered by the Python program. The firmware then decodes the received data and performs the requested action, be it setting a pin direction or a voltage level or servo control. When a pin is read, the Arduino also sends this value back to the Python program via the serial connection.

## Parts

- 1 x Arduino Nano
- 1 x USB-A to micro USB-B cable

## About the Author

[Nick A. Bild, MS](https://nickbild79.firebaseapp.com/#!/) forked by [spicer](https://www.ltspiceusers.ch/)

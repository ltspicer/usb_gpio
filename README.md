# USBgpio

Add Python programmable GPIO pins to any computer with USBgpio.

![](https://raw.githubusercontent.com/nickbild/usb_gpio/main/media/logo_sm.jpg)

## How It Works

USBgpio is a physical device with 12 header pins (10 GPIO, 3.3V, GND) that hooks up to any modern computer via a USB port. There is also an accompanying [Python library](https://github.com/nickbild/usb_gpio/blob/main/usbgpio.py) that controls the GPIO pins with simple commands.

Available pins: 2 to 13

Available servo pins: 2 to 9

This brief example demonstrates the basics of using USBgpio:

```python
from usbgpio import USBgpio
import time


# Establish a serial connection to the device.
gpio = USBgpio('/dev/ttyUSB0', 115200)

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
```

Inside the device's case, there is an Arduino Nano 33 IoT. Header pins on the device are internally connected to pins on the Arduino. This microcontroller development board runs [firmware](https://github.com/nickbild/usb_gpio/blob/main/usb_gpio_arduino/usb_gpio_arduino.ino) that listens for serial data coming in over USB, as triggered by the Python program. The firmware then decodes the data it receives and takes the requested action, whether it be to set a pin direction or voltage level. If a pin is being read, the Arduino also sends that value back to the Python program via the serial connection.

USBgpio is a quick and easy way to do some prototyping without getting out your development boards, setting them up, connecting to a network, remotely accessing them, etc. It is pretty fast at ~54 microseconds to change a pin state, so it will work for many use cases. However, an Arduino UNO, for example, is about 16 times faster, so for high-speed applications, USBgpio would not be appropriate. That is not the intended use case for this device, however — USBgpio is meant for convenience, not squeezing out every last ounce of performance.

This trace shows a pin flipping between high and low voltages in a tight loop:

![](https://raw.githubusercontent.com/nickbild/usb_gpio/main/media/usbgpio.png)

## Media

[Demo Video](https://www.youtube.com/watch?v=I5nCYR48eAI)

![](https://raw.githubusercontent.com/nickbild/usb_gpio/main/media/front1_sm.jpg)

![](https://raw.githubusercontent.com/nickbild/usb_gpio/main/media/front2_sm.jpg)

Blinking an LED with USBgpio:

![](https://raw.githubusercontent.com/nickbild/usb_gpio/main/media/blink_sm.jpg)

The back of the unit:

![](https://raw.githubusercontent.com/nickbild/usb_gpio/main/media/rear_sm.jpg)

The wires that run from the header to the Arduino:

![](https://raw.githubusercontent.com/nickbild/usb_gpio/main/media/wires_sm.jpg)

The Arduino with a header designed to fit in the case:

![](https://raw.githubusercontent.com/nickbild/usb_gpio/main/media/arduino_sm.jpg)

Testing the device:

![](https://raw.githubusercontent.com/nickbild/usb_gpio/main/media/testing_sm.jpg)

## Bill of Materials

- 1 x Arduino Nano 33 IoT
- 1 x USB-A to micro USB-B cable
- 1 x 3D-printed case
- 12 x Header pins, wires, DuPont connectors

## About the Author

[Nick A. Bild, MS](https://nickbild79.firebaseapp.com/#!/)

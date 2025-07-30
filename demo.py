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

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
    gpio.digital_write(ledPIN, "HIGH")  # LED on. Can also be "HIGH", "high", "High" or 1
    gpio.servo_write(servoPIN, 0)       # Move servo to 0°
    time.sleep(1)
    gpio.digital_write(ledPIN, 0)       # LED off Can also be "LOW", "low", "Low" or 0
    gpio.servo_write(servoPIN, 180)     # Move servo to 180°
    time.sleep(1)

    # Read the value of a pin and print the result.
    print(gpio.digital_read(inputPIN))

# Detach servo
gpio.servo_detach(servoPIN)

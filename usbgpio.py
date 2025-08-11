import serial
import time

class USBgpio:
    def __init__(self, device, speed):
        self.ser = serial.Serial(device, speed, timeout=1)
        time.sleep(1) 
        return

    # Set pin mode to input.
    def set_input(self, pin):
        if pin == 2:
            self.ser.write(b"a")
        elif pin == 3:
            self.ser.write(b"b")
        elif pin == 4:
            self.ser.write(b"c")
        elif pin == 5:
            self.ser.write(b"d")
        elif pin == 6:
            self.ser.write(b"e")
        elif pin == 7:
            self.ser.write(b"f")
        elif pin == 8:
            self.ser.write(b"g")
        elif pin == 9:
            self.ser.write(b"h")
        elif pin == 10:
            self.ser.write(b"i")
        elif pin == 11:
            self.ser.write(b"j")
        elif pin == 12:
            self.ser.write(b"N")
        elif pin == 13:
            self.ser.write(b"I")
        return

    # Set pin mode to output.
    def set_output(self, pin):
        if pin == 2:
            self.ser.write(b"k")
        elif pin == 3:
            self.ser.write(b"l")
        elif pin == 4:
            self.ser.write(b"m")
        elif pin == 5:
            self.ser.write(b"n")
        elif pin == 6:
            self.ser.write(b"o")
        elif pin == 7:
            self.ser.write(b"p")
        elif pin == 8:
            self.ser.write(b"q")
        elif pin == 9:
            self.ser.write(b"r")
        elif pin == 10:
            self.ser.write(b"s")
        elif pin == 11:
            self.ser.write(b"t")
        elif pin == 12:
            self.ser.write(b"O")
        elif pin == 13:
            self.ser.write(b"L")
        return

    # Write to pin.
    def digital_write(self, pin, level):
        if str(level) == "1" or str(level).upper() == "HIGH":
            if pin == 2:
                self.ser.write(b"u")
            elif pin == 3:
                self.ser.write(b"v")
            elif pin == 4:
                self.ser.write(b"w")
            elif pin == 5:
                self.ser.write(b"x")
            elif pin == 6:
                self.ser.write(b"y")
            elif pin == 7:
                self.ser.write(b"z")
            elif pin == 8:
                self.ser.write(b"0")
            elif pin == 9:
                self.ser.write(b"1")
            elif pin == 10:
                self.ser.write(b"2")
            elif pin == 11:
                self.ser.write(b"3")
            elif pin == 12:
                self.ser.write(b"P")
            elif pin == 13:
                self.ser.write(b"H")
        elif str(level) == "0" or str(level).upper() == "LOW":
            if pin == 2:
                self.ser.write(b"4")
            elif pin == 3:
                self.ser.write(b"5")
            elif pin == 4:
                self.ser.write(b"6")
            elif pin == 5:
                self.ser.write(b"7")
            elif pin == 6:
                self.ser.write(b"8")
            elif pin == 7:
                self.ser.write(b"9")
            elif pin == 8:
                self.ser.write(b"!")
            elif pin == 9:
                self.ser.write(b"@")
            elif pin == 10:
                self.ser.write(b"#")
            elif pin == 11:
                self.ser.write(b"$")
            elif pin == 12:
                self.ser.write(b"Q")
            elif pin == 13:
                self.ser.write(b"M")

    # Read from pin.
    def digital_read(self, pin):
        if pin == 2:
            self.ser.write(b"%")
        elif pin == 3:
            self.ser.write(b"^")
        elif pin == 4:
            self.ser.write(b"&")
        elif pin == 5:
            self.ser.write(b"*")
        elif pin == 6:
            self.ser.write(b"(")
        elif pin == 7:
            self.ser.write(b")")
        elif pin == 8:
            self.ser.write(b"-")
        elif pin == 9:
            self.ser.write(b"=")
        elif pin == 10:
            self.ser.write(b",")
        elif pin == 11:
            self.ser.write(b".")
        elif pin == 12:
            self.ser.write(b"R")
        elif pin == 13:
            self.ser.write(b"?")
        if self.ser.read() == b'\x00':
            return 0
        else:
            return 1

    # ----------- Servo-Commands -----------

    def servo_attach(self, pin):
        # Pin als einzelne Ziffer senden (z.B. 8 -> b'A8')
        cmd = b'A' + str(pin).encode()
        self.ser.write(cmd)
        time.sleep(0.2)  # Kurze Pause für Arduino

    def servo_write(self, pin, angle):
        # z.B. Pin 8, Winkel 90 -> b'B890'
        cmd = b'B' + str(pin).encode() + str(int(angle)).encode()
        self.ser.write(cmd)
        time.sleep(0.2)

    def servo_detach(self, pin):
        cmd = b'C' + str(pin).encode()
        self.ser.write(cmd)
        time.sleep(0.2)


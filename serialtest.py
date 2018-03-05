import time
import serial
print "Starting program"
ser = serial.Serial('/dev/ttyS0', baudrate=9600,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS
                    )

try:
    print 'Starting sending data from uart.'
    while True:
        time.sleep(1)
        ser.write('Hello World From Raspberry Pi\r\n')
        if ser.inWaiting() > 0:
            data = ser.readline()
            print data

except KeyboardInterrupt:
    print "Exiting Program"

except:
    print "Error Occurs, Exiting Program"

finally:
    ser.close()
    pass

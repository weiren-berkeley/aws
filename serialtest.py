import time
import serial
import random
print "Starting program"
ser = serial.Serial('/dev/ttyS0', baudrate=115200,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_TWO,
                    bytesize=serial.EIGHTBITS
                    )

try:
    print 'Starting sending data from uart.'
    while True:
        time.sleep(1)
        angle1 = random.random()
        ser.write('Angle1 = '+ str(angle1); + '\r\n')
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

#!/usr/bin/python

import MySQLdb
import serial
import time

DEFAULT_PORT = '/dev/ttyUSB0'
BAUDRATE = 115200
INTERVAL = 10

DB_HOST = 'bee-db'
DB_USER = 'beedb'
DB_PASS = 'beedb'
DB_BASENAME = 'beedb'


def main():
    serial_port = serial.Serial(DEFAULT_PORT,
                                BAUDRATE,
                                parity=serial.PARITY_NONE,
                                stopbits=serial.STOPBITS_ONE,
                                bytesize=serial.EIGHTBITS)

    header = ''
    data_string = ''
    started = False
    data_ready = False
    weather = {}

    while True:
        try:
            while serial_port.in_waiting > 0:
                byte = serial_port.read()

                if not started:
                    header = header + byte
                    if '<\r\n' in header:
                        header = ''
                        data_string = ''
                        started = True
                        continue

                if (started):
                    if (byte == '>'):
                        started = False
                        data_ready = True
                        break

                    data_string = data_string + byte

            if not data_ready:
                continue

            data_ready = False

            strings = [filter(None,string.split(' ')) for string in data_string.split('\r\n')] 

            for line in strings:
                if len(line) >= 2:
                    weather[line[0][:-1]] = line[1]

            for key, value in weather.items():
                print (key, value)
            print('\r\n')

            db = MySQLdb.connect(DB_HOST, DB_USER, DB_PASS, DB_BASENAME)
            curs = db.cursor()
            curs.execute('INSERT INTO weather (address,temp1,temp2,humi1,humi2,light,pressure) \
                          VALUES(%d, %f, %f, %d, %d, %d, %d)' %
                         (int(weather['address'], 0),
                          float(weather['temp1']),
                          float(weather['temp2']),
                          int(weather['humi1']),
                          int(weather['humi2']),
                          int(weather['light']),
                          int(weather['pressure'])))
            curs.execute('INSERT INTO info (address, rssi, voltage, acc_voltage, power, current) \
                          VALUES(%d, %d, %d, %d, %d, %d)' %
                         (int(weather['address'], 0),
                          int(weather['RSSI']),
                          int(weather['voltage']),
                          int(weather['acc_voltage']),
                          int(weather['power']),
                          int(weather['current'])))
            db.commit()
            db.close()

            time.sleep(INTERVAL)

        except KeyboardInterrupt:
            print 'exit'
            break
    # Run the bot until the you presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    # updater.idle()

if __name__ == '__main__':
    main()

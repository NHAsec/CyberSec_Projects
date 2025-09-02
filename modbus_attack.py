#!/usr/bin/env python3

import sys
import time
from pymodbus.client.sync import ModbusTcpClient as ModbusClient
from pymodbus.exceptions import ConnectionException

ip = sys.argv[1]
client = ModbusClient(ip, port=502)
client.connect()
while True:
  client.write_register(1, 1)   # Start the feed_pump
  client.write_register(3, 1)   # Stop release valve from opening
  client.write_register(4, 0)   # Stop seperator valve
  client.write_register(8, 1)   # Keep waste water valve open
  client.write_register(7,2000) # Set processed oil counter value to 2000

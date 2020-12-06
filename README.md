# Neopixel Christmas Lights

This project is an attempt to create a programmable Christmas tree (tree not included)


## Setup

We suggest you use a virtual environment of some sort to manage all the packages.

Required packages (`pip install`):

- `numpy`
- `flask`
- `adafruit-circuitpython-neopixel`
- `pygame` (if you use the fake tree interface)


## Network Configuration

Flask default port is 5000.  Find the IP address of the Raspberry Pi by typing `ifconfig` in the terminal.

In a browser navigate to the address of the Pi and port 5000.  If the Pi gets the first IP address on the subnet, it might look something like

```
http://192.168.0.1:5000/
```


## Other

[Similar project](https://learn.adafruit.com/micropython-smart-holiday-lights) (that we didn't find until later)

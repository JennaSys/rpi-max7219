# rpi-max7219
**Raspberry Pi driver for MAX7219 with 7-segment modules**

* Utilizes hardware SPI (spidev library is required)
* Supports cascading MAX7219 devices
* Number of digits per MAX7219 device can be specified

max7219.py uses an internal buffer (array) that is a direct representation of the display when flushed.  So buffer[0] is the leftmost digit in the display and buffer[digits] is the rightmost.  Also digit0 is the leftmost and digit7 is rightmost for each MAX7219 device.  Cascaded devices add additional digits to the right.  If less than 8 digits are connected to the MAX7219, set the scan_digits parameter when initializing so that the code propery handles text value inputs and cascading.  The digits initialization value represents the total number of digits across all cascaded devices.

seven_segment_ascii.py maps ascii characters to their segment representations.  **get_char()** uses a *DP-G-F-E-D-C-B-A* bit order and **get_char2()** uses a *DP-A-B-C-D-E-F-G* bit order (which is what the MAX7219 specifies).


## Installation
To install the library directly from github, you can enter the following from a command prompt on your Raspberry Pi:
```bash
pip3 install git+https://github.com/JennaSys/rpi-max7219.git
```


## Raspberry Pi Examples

```python
import max7219
display = max7219.SevenSegment()
display.text("ABCDEF")
display.number(3.14159)
display.message("Hello World")
display.clear()
```

## Connections

Raspberry Pi     | MAX7219 LED Driver
---------------- | ----------------------
5V               | VCC 
GND              | GND
SPI0_MOSI        | DIN
SPI0_CE0         | CS
SPI0_SCLK        | CLK

*NOTE: A level shifter (i.e. 2N7000) may be required on the data lines going to the MAX7219 to change the 3.3V logic to 5V*


## Credits
This library is based on:
* [rm-hull's max7219.py (pre-2017 version)](https://github.com/rm-hull/max7219) for the Raspberry Pi ([PyPI Project](https://pypi.org/project/max7219/))
* [dmadison's Segmented LED Display - ASCII Library](https://github.com/dmadison/LED-Segment-ASCII)


## License

Licensed under the [MIT License](http://opensource.org/licenses/MIT).

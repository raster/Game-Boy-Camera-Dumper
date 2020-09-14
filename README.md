### Game Boy Camera Dumper

This script captures serial data sent from a Game Boy and saves it to disk.

On macOS I typically type the following:

`python3 gbcdumper.py /dev/tty.wchusbserialfa440`

The /dev/tty.wchusbserialfa440 specifies the USB port. This will be different depending on your Arduino, different on different machines, and even more different on Windows or Linux.

When the script runs it will show the output in the terminal, and also dump the data to a file named `gbc-output.txt`

When you are done with all your transfers just hit `Ctrl C` to end the script.

You can then open `gbc-output.txt` and copy the contents to paste into the [decoder](https://github.com/mofosyne/arduino-gameboy-printer-emulator/tree/master/gbp_decoder)

*Note:* The decoder above seems to have broken for me recently, and no longer supports multiple images properly. I'll probably add my copy that does work to this repository soon.

*Note 2:* Ah, there was a format change in the code that broke things... I'll fix it.



--- 

Pete Prodoehl

<pete@2xlnetworks.com>



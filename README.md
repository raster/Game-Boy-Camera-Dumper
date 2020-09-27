# Game Boy Camera Dumper

This Python script captures serial data sent from a Game Boy and saves it to disk.

On macOS I typically type the following:

`python3 gbcdumper.py /dev/tty.wchusbserialfa440`

The /dev/tty.wchusbserialfa440 specifies the USB port. This will be different depending on your Arduino, different on different machines, and even more different on Windows or Linux.

When the script runs it will show the output in the terminal, and also dump the data to a file named `gbc-output.txt`

When you are done with all your transfers just hit `Ctrl C` to end the script.

You can then open `gbc-output.txt` and copy the contents to paste into the [decoder](https://github.com/mofosyne/arduino-gameboy-printer-emulator/tree/master/gbp_decoder)

The file `gbc-output.txt` can be deleted when you are done and it will be created fresh the next time you run the script. If you don't delete it, it will just keep appending data each time you run the script. Do what you want.


--- 

Pete Prodoehl

Game Boy Camera Photos: http://photos.rasterweb.net/

<pete@2xlnetworks.com>



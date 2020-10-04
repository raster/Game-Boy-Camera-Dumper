# Game Boy Camera Dumper

## What is it?

If you've got an [Arduino Gameboy Printer Emulator](https://github.com/mofosyne/arduino-gameboy-printer-emulator#quick-start) this Python script can capture the serial data sent from the Game Boy/Arduino and save it to a file on your computer.

## How Does it Work?

Game Boy Camera Dumper opens a serial (USB) port and waits for data that is sent when you choose to "print" the photo from your Game Boy Camera. 

When the script runs it will show the output in the terminal, and also dump the data to a file named `gbc-output.txt`

Once the data is saved into a text file you can then decode it and get your images.

## How do I use it?

On macOS I typically type the following:

`python3 gbc-dumper.py /dev/tty.wchusbserialfa440`

The /dev/tty.wchusbserialfa440 specifies the USB port. This will be different depending on your Arduino, different on different machines, and even more different on Windows or Linux.

When you are done with all your transfers just hit `Ctrl C` to end the script.

You can then open `gbc-output.txt` in your favorite text editor and copy the contents to paste into the [decoder](https://github.com/mofosyne/arduino-gameboy-printer-emulator/tree/master/gbp_decoder).

The file `gbc-output.txt` can be deleted when you are done and it will be created fresh the next time you run the script. If you don't delete it, it will just keep appending data each time you run the script. Do what you want with that feature... the choice is yours. :)

## More Info

I've written up a blog post that helps explain the process here: http://rasterweb.net/raster/2020/10/03/game-boy-camera-dumper/ 

--- 

**Pete Prodoehl**

GBC Photos: http://photos.rasterweb.net/

Contact: <pete@2xlnetworks.com>



# MidiforArduino

First, run buzzer.ino on your arduino. Design the circuit how you'd like, and adjust the pins in the .ino file to match your setup. The waitFor function will run until it hears from the python script. 

converter.py will find the serial port your arduino is connected to and send over the notes in their natural frequency (s). The notes should play once converter.py stops talking over the serial. This is indicated by the character 'k' once its done with each channel.  

The current .ino file only supports one channel. The UNO I used only had 1 internal clock, so it wasn't possible for me to play chords.

Usage: 

python converter.py "name of midi file"

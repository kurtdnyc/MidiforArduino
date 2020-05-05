import time,sys, os, fnmatch, midi, serial


errors = {
    'program': 'Bad input, please refer this spec-\n'
               'http://www.electronics.dit.ie/staff/tscarff/Music_technology/midi/program_change.htm',
    'notes': 'Bad input, please refer this spec-\n'
             'http://www.electronics.dit.ie/staff/tscarff/Music_technology/midi/midi_note_numbers_for_octaves.htm'
}
NOTES = ['C', 'CS', 'D', 'DS', 'E', 'F', 'FS', 'G', 'GS', 'A', 'AS', 'B']
OCTAVES = list(range(11))
NOTES_IN_OCTAVE = len(NOTES)

args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]

def count(ticks,notes):
    breakMe = True
    res = []
    for i in ticks:
        if i not in res:
            res.append(i)
    counts = [(ticks.count(x)) for x in res]
    ch0,ch1,ch2,ch3, = ([] for i in range(4))
    final = [ch3,ch2,ch1,ch0]
    notesidx = 0
    countsidx = -1
    stididx=0

    while breakMe:
        countsidx += 1
        stididx += 1
        if stididx == len(notes):
            return final
            breakMe = False
        for finalidx, vchan in enumerate(final):

            if int(finalidx) >= counts[countsidx]:
                vchan.append(0)
                stupididx+=1
            else:
                vchan.append(notes[notesidx])
                stupididx +=1
                notesidx += 1
            if stididx == len(notes):
            if notesidx == len(notes):
                return final
                breakMe = False
    return final

def convertTuple(tup):
    mystr =  ''.join(tup)
    return 'NOTE_' + mystr

def number_to_note(number: int) -> tuple:
    octave = number // NOTES_IN_OCTAVE
    assert octave in OCTAVES, errors['notes']
    assert 0 <= number <= 127, errors['notes']
    note = NOTES[number % NOTES_IN_OCTAVE]
    return str(note),str(octave-1)

def sendData(midiname):
    song = midi.read_midifile(midiname)
    song.make_ticks_abs()
    tracks = []
    trackNotes = []
    trackTicks = []
    for track in song:
        notes = [note for note in track if note.name == 'Note On']
        notes2 = [note for note in track if note.name == 'Note Off']
        pitch = [str(convertTuple(number_to_note(note.pitch))) for note in notes]
        tick = [note.tick for note in notes]
        tracks += [tick, pitch]
        trackNotes += pitch
        trackTicks += tick

    channels = count(trackTicks, trackNotes)
    for i,v in enumerate(channels):
        print( 'Channel' + str(i +1) + " == " + str(v))
    for i in channels:
        for j in i:
            sercmd = j
            ser.write(sercmd.encode())


os.system("cd")
inDIR = '/dev'
pattern = 'cu.usb*'
fileList = []
# Walk through directory to find serial port
for dName, sdName, fList in os.walk(inDIR):
    for fileName in fList:
        if fnmatch.fnmatch(fileName, pattern): # Match search string
            fileList.append(os.path.join(dName, fileName))
SerialDir = fileList
ser = serial.Serial(SerialDir[0], 9600)
time.sleep(3)

if args is None:
    raise SystemExit(f"Please specify a filename. Usage: {sys.argv[0]} <midi filename>")
else:
    sendData(args[0])



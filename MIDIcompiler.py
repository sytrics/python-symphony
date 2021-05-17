from midiutil.MidiFile import MIDIFile
from Visitor import visitor
import Node


class MIDIcompiler(visitor) : 
    """
    visiteur permettant la génération d'un fichier MIDI a partir de la structure d'un code python
    """ 

    def __init__(self, verbosity) : 
        visitor.__init__(self,verbosity)
        self.mf = MIDIFile(1)     # only 1 track
        self.track = 0   # the only track
        self.time = 0    # start at the beginning
        self.channel = 0 # channel 
        self.volume = 100 # define volume here 
        self.pitch = 60 #defines the note
        self.duration = 1 # duration of the note
        self.mf.addTrackName(self.track, self.time, "Sample Track")
        self.mf.addTempo(self.track, self.time, 120)
        
    
    def visitStatement(self, StatementNode) :
        if self.verbosity : 
            print("visitStatement")
        for i in StatementNode.children : 
            i.accept(self)
        

    def visitNode(self, Node) : 
        if self.verbosity : 
            print("visit Node :" + Node.token.valeur)

        if Node.token.type == 'INT': 
            self.pitch = int(Node.token.valeur)
            self.volume = 100 - int(Node.token.ligne)
            self.duration = 1
            self.mf.addNote(self.track, self.channel, self.pitch, self.time, self.duration, self.volume)
            self.time += 2
        elif Node.token.type == 'IF': 
            self.pitch = 56
            self.mf.addNote(self.track, self.channel, self.pitch, self.time, self.duration, self.volume)
            self.time += 2
        

    def compile(self, file) : 
        
        with open(file, 'wb') as outf:
            self.mf.writeFile(outf)
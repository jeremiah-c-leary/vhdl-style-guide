import re
import line

class vhdlFile():

    def __init__(self, filename):
        self.filename = filename
        self.lines = [line.line('')]
        self._processFile(filename)

    def _processFile(self, filename):
        with open (filename) as oFile:
            for sLine in oFile:
                oLine = line.line(sLine.rstrip())
                # Check for blank lines
                if re.match('^\s*$', oLine.line):
                    oLine.isBlank = True
                # Check for library lines
                if re.match('^\s*library', oLine.lineLower):
                    oLine.isLibrary = True
                    oLine.indentLevel = 0
                # Check for library use lines
                if re.match('^\s*use', oLine.lineLower):
                    oLine.isLibraryUse = True
                    oLine.indentLevel = 1

                # Add line to file
                self.lines.append(oLine)


import re
import line

class vhdlFile():

    def __init__(self, filename):
        self.filename = filename
        self.lines = [line.line('')]
        self._processFile(filename)

    def _processFile(self, filename):
        fInsideEntity = False
        fInsidePortMapDeclaration = False
        fInsideGenericMapDeclaration = False
        fInsideArchitecture = False
        iOpenParenthesis = 0;
        iCloseParenthesis = 0;
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
                # Check for entity
                if re.match('^\s*entity', oLine.lineLower):
                    fInsideEntity = True
                    oLine.isEntityDeclaration = True
                # Assign inside entity attribute
                if fInsideEntity:
                    oLine.insideEntity = True
                    if oLine.isEntityDeclaration:
                        oLine.indentLevel = 0
                    else:
                        oLine.indentLevel = 1
                # Check for the end of the entity
                if re.match('^\s*end\s+entity', oLine.lineLower):
                    fInsideEntity = False
                    oLine.isEndEntityDeclaration = True
                    oLine.indentLevel = 0

                # Check port map declarations
                if fInsideEntity:
                    if re.match('^\s*port', oLine.lineLower) and not fInsidePortMapDeclaration:
                        fInsidePortMapDeclaration = True
                        oLine.isPortKeyword = True
                        oLine.indentLevel = 1
                    if fInsidePortMapDeclaration:
                        oLine.insidePortMap = True
                        if re.match('^\s*\S+.*:', oLine.line):
                            oLine.isPortDeclaration = True
                            oLine.indentLevel = 2
                        iOpenParenthesis += oLine.line.count('(')
                        iCloseParenthesis += oLine.line.count(')')
                        if iOpenParenthesis == iCloseParenthesis:
                            oLine.indentLevel = 1
                            fInsidePortMapDeclaration = False
                            iOpenParenthesis = 0
                            iCloseParenthesis = 0
                            oLine.isEndPortMap = True

                # Check generic map declarations
                if fInsideEntity:
                    if re.match('^\s*generic', oLine.lineLower) and not fInsideGenericMapDeclaration:
                        fInsideGenericMapDeclaration = True
                        oLine.isGenericKeyword = True
                        oLine.indentLevel = 1
                    if fInsideGenericMapDeclaration:
                        oLine.insideGenericMap = True
                        if re.match('^\s*\S+.*:', oLine.line):
                            oLine.isGenericDeclaration = True
                            oLine.indentLevel = 2
                        iOpenParenthesis += oLine.line.count('(')
                        iCloseParenthesis += oLine.line.count(')')
                        if iOpenParenthesis == iCloseParenthesis:
                            oLine.indentLevel = 1
                            fInsideGenericMapDeclaration = False
                            iOpenParenthesis = 0
                            iCloseParenthesis = 0
                            oLine.isEndGenericMap = True

                # Check architecture declarations
                if re.match('^\s*architecture', oLine.lineLower) and not fInsideArchitecture:
                    fInsideArchitecture = True
                    oLine.isArchitectureKeyword = True
                    oLine.indentLevel = 0
                if fInsideArchitecture:
                    oLine.insideArchitecture = True
                    if re.match('^\s*begin', oLine.lineLower):
                        oLine.isArchitectureBegin = True
                        oLine.indentLevel = 0
                    if re.match('^\s*end\s+architecture', oLine.lineLower):
                        fInsideArchitecture = False
                        oLine.isEndArchitecture = True
                        oLine.indentLevel = 0

                # Check Signal declarations
                if fInsideArchitecture:
                    if re.match('^\s*signal', oLine.lineLower):
                        oLine.isSignal = True
                        oLine.indentLevel = 1


                # Add line to file
                self.lines.append(oLine)


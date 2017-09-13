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
        fFoundArchitectureBegin = False
        fInsideProcess = False
        fFoundProcessBegin = False
        fInsideConcurrent = False
        fInsideSensitivityList = False

        fInsideIfStatement = False

        fInsideCase = False
        fInsideCaseWhen = False


        iOpenParenthesis = 0;
        iCloseParenthesis = 0;

        iCurrentIndentLevel = 0;

        with open (filename) as oFile:
            for sLine in oFile:
                oLine = line.line(sLine.rstrip())
                # Check for blank lines
                if re.match('^\s*$', oLine.line):
                    oLine.isBlank = True
                # Check for comment lines
                if re.match('^\s*--', oLine.line):
                    oLine.isComment = True
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
                    if re.match('^\s*begin', oLine.lineLower) and not fFoundArchitectureBegin:
                        fFoundArchitectureBegin = True
                        oLine.isArchitectureBegin = True
                        oLine.indentLevel = 0
                    if re.match('^\s*end\s+architecture', oLine.lineLower):
                        fInsideArchitecture = False
                        fFoundArchitectureBegin = False
                        oLine.isEndArchitecture = True
                        oLine.indentLevel = 0

                # Check Signal declarations
                if fInsideArchitecture:
                    if re.match('^\s*signal', oLine.lineLower):
                        oLine.isSignal = True
                        oLine.indentLevel = 1

                # Check Constant declarations
                if fInsideArchitecture:
                    if re.match('^\s*constant', oLine.lineLower):
                        oLine.isConstant = True
                        oLine.indentLevel = 1

                # Check process declarations
                if fInsideArchitecture:
                    if re.match('^\s*process', oLine.lineLower) or re.match('^\s*\S+\s*:\s*process', oLine.lineLower):
                        fInsideProcess = True
                        oLine.isProcessKeyword = True
                        oLine.indentLevel = 1
                    if fInsideProcess == True:
                        oLine.insideProcess = True
                        # Check sensitivity list
                        if '(' in oLine.line and not fInsideSensitivityList and not fFoundProcessBegin:
                            fInsideSensitivityList = True
                            oLine.isSensitivityListBegin = True
                        if fInsideSensitivityList:
                            oLine.insideSensitivityList = True
                            iOpenParenthesis += oLine.line.count('(')
                            iCloseParenthesis += oLine.line.count(')')
                            if iOpenParenthesis == iCloseParenthesis:
                                fInsideSensitivityList = False
                                oLine.isSensitivityListEnd = True
                                iOpenParenthesis = 0
                                iCloseParenthesis = 0
                                iCurrentIndentLevel = 2
                        if re.match('^.*\s+begin', oLine.lineLower) or re.match('^\s*begin', oLine.lineLower):
                            oLine.indentLevel = 1
                            oLine.isProcessBegin = True
                            fFoundProcessBegin = True
                            iCurrentIndentLevel = 2
                        if re.match('^\s*end\s+process', oLine.lineLower):
                            fInsideProcess = False
                            oLine.indentLevel = 1
                            oLine.isEndProcess = True
                            fFoundProcessBegin = False
                            iCurrentIndentLevel = 1


                # Check concurrent declarations
                if fInsideArchitecture and not fInsideProcess:
                    if re.match('^\s*\w+\s*<=', oLine.line) or re.match('^\s*\w+\s*:\s*\w+\s*<=', oLine.line):
                        fInsideConcurrent = True
                        oLine.indentLevel = 1
                        oLine.isConcurrentBegin = True
                    if fInsideConcurrent:
                        oLine.insideConcurrent = True
                        if re.match('.*;', oLine.line):
                            fInsideConcurrent = False
                            oLine.isEndConcurrent = True

                # Check if statements
                if fInsideProcess:
                    if re.match('^\s*if', oLine.lineLower):
                        oLine.isIfKeyword = True
                        fInsideIfStatement = True
                        oLine.indentLevel = iCurrentIndentLevel
                        iCurrentIndentLevel += 1
                    if re.match('^\s*elsif', oLine.lineLower):
                        oLine.isElseIfKeyword = True
                        fInsideIfStatement = True
                        oLine.indentLevel = iCurrentIndentLevel - 1
                    if re.match('^\s*end\s+if', oLine.lineLower):
                        oLine.isEndIfKeyword = True
                        iCurrentIndentLevel -= 1
                        oLine.indentLevel = iCurrentIndentLevel
                    if fInsideIfStatement:
                        oLine.insideIf = True
                    if fInsideIfStatement and 'then' in oLine.lineLower:
                        oLine.isThenKeyword = True
                        fInsideIfStatement = False
                    if re.match('^\s*else', oLine.lineLower):
                        oLine.isElseKeyword = True
                        oLine.indentLevel = iCurrentIndentLevel - 1

                # Check case statements
                if fInsideProcess:
                    if re.match('^\s*case\s', oLine.lineLower):
                        oLine.isCaseKeyword = True
                        oLine.indentLevel = iCurrentIndentLevel
                        iCurrentIndentLevel += 2
                        fInsideCase = True
                    if fInsideCase:
                        if re.match('^\s*.*\sis\s', oLine.lineLower) or re.match('^\s*.*\sis$', oLine.lineLower):
                            oLine.isCaseIsKeyword = True
                            fInsideCase = False
                    if re.match('^\s*when\s', oLine.lineLower):
                        oLine.isCaseWhenKeyword = True
                        oLine.indentLevel = iCurrentIndentLevel - 1
                        fInsideCaseWhen = True
                    if fInsideCaseWhen:
                        oLine.insideCaseWhen = True
                        if re.match('^\s*.*=>', oLine.line):
                            fInsideCaseWhen = False
                            oLine.isCaseWhenEnd = True
                    if re.match('^\s*end\s+case', oLine.lineLower):
                        oLine.isEndCaseKeyword = True
                        oLine.indentLevel = iCurrentIndentLevel - 2

                # Add line to file
                self.lines.append(oLine)


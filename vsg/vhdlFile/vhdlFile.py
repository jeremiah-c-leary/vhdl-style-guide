import re
from vsg import line


def update_inside_attributes(oPreviousLine, oCurrentLine):

    if oPreviousLine.insideEntity and not oPreviousLine.isEndEntityDeclaration:
        oCurrentLine.insideEntity = True

    if oPreviousLine.insidePortMap and not oPreviousLine.isEndPortMap:
        oCurrentLine.insidePortMap = True
   
    if oPreviousLine.insideGenericMap and not oPreviousLine.isEndGenericMap:
        oCurrentLine.insideGenericMap = True

    if oPreviousLine.insideArchitecture and not oPreviousLine.isEndArchitecture:
        oCurrentLine.insideArchitecture = True

    if oPreviousLine.insideProcess and not oPreviousLine.isEndProcess:
        oCurrentLine.insideProcess = True

    if oPreviousLine.insideConcurrent and not oPreviousLine.isEndConcurrent:
        oCurrentLine.insideConcurrent = True

    if oPreviousLine.insideSensitivityList and not oPreviousLine.isSensitivityListEnd:
        oCurrentLine.insideSensitivityList = True

    if oPreviousLine.insideIf and not (oPreviousLine.isEndIfKeyword or oPreviousLine.isThenKeyword):
        oCurrentLine.insideIf = True

    if oPreviousLine.insideType and not oPreviousLine.isTypeEnd:
        oCurrentLine.insideType = True

    if oPreviousLine.insideCase and not oPreviousLine.isCaseIsKeyword:
        oCurrentLine.insideCase = True

    if oPreviousLine.insideCaseWhen and not oPreviousLine.isCaseWhenEnd:
        oCurrentLine.insideCaseWhen = True

    if oPreviousLine.insideSequential and not oPreviousLine.isSequentialEnd:
        oCurrentLine.insideSequential = True

    if oPreviousLine.insideVariableAssignment and not oPreviousLine.isVariableAssignmentEnd:
        oCurrentLine.insideVariableAssignment = True

    if oPreviousLine.insideComponent and not oPreviousLine.isComponentEnd:
        oCurrentLine.insideComponent = True

    if oPreviousLine.insideInstantiation and not oPreviousLine.isInstantiationPortEnd:
        oCurrentLine.insideInstantiation = True

    if oPreviousLine.insideInstantiationPortMap and not oPreviousLine.isInstantiationPortEnd:
        oCurrentLine.insideInstantiationPortMap = True

    if oPreviousLine.insideInstantiationGenericMap and not oPreviousLine.isInstantiationGenericEnd:
        oCurrentLine.insideInstantiationGenericMap = True

    if oPreviousLine.insidePackage and not oPreviousLine.isPackageEnd:
        oCurrentLine.insidePackage = True

    if oPreviousLine.insidePackageBody and not oPreviousLine.isPackageBodyEnd:
        oCurrentLine.insidePackageBody = True

    if oPreviousLine.insideFunction and not oPreviousLine.isFunctionEnd:
        oCurrentLine.insideFunction = True

    if oPreviousLine.insideGenerate and not oPreviousLine.isGenerateEnd:
        oCurrentLine.insideGenerate = True

    if oPreviousLine.insideForLoop and not oPreviousLine.isForLoopEnd:
        oCurrentLine.insideForLoop = True


class vhdlFile():

    def __init__(self, filename):
        self.filename = filename
        self.lines = [line.line('')]
        self.hasArchitecture = False
        self.hasEntity = False
        self._processFile()

    def write(self):
        with open(self.filename, 'w') as oFile:
            for oLine in self.lines[1:]:
                oFile.write(oLine.line + '\n')
        oFile.close()

    def _processFile(self):
        fFoundArchitectureBegin = False
        fFoundProcessBegin = False
        fSensitivityListFound = False

        fGenerateBeginFound = False

        iOpenParenthesis = 0
        iCloseParenthesis = 0

        iCurrentIndentLevel = 0

        with open(self.filename) as oFile:
            for sLine in oFile:
                sLine = sLine.replace('\t', '  ')
                oLine = line.line(sLine.rstrip())
                update_inside_attributes(self.lines[-1], oLine)
                # Check for blank lines
                if re.match('^\s*$', oLine.line):
                    oLine.isBlank = True
                # Check for comment lines
                if '--' in oLine.line:
                    oLine.hasComment = True
                    oLine.commentColumn = oLine.line.find('--')
                if re.match('^\s*--', oLine.line):
                    oLine.isComment = True
                    oLine.indentLevel = iCurrentIndentLevel
                # Check for null statements
                if re.match('^\s*null\s*;', oLine.lineLower):
                    oLine.indentLevel = iCurrentIndentLevel
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
                    self.hasEntity = True
                    oLine.isEntityDeclaration = True
                    iCurrentIndentLevel = 1
                    oLine.indentLevel = 0
                    oLine.insideEntity = True
                # Check for the end of the entity
                if re.match('^\s*end', oLine.lineLower) and not oLine.insidePortMap and not oLine.insideGenericMap and oLine.insideEntity:
                    oLine.isEndEntityDeclaration = True
                    oLine.indentLevel = 0
                    iCurrentIndentLevel = 0

                # Check port map declarations
                if oLine.insideEntity or oLine.insideComponent:
                    if re.match('^\s*port', oLine.lineLower) and not oLine.insidePortMap:
                        oLine.isPortKeyword = True
                        oLine.insidePortMap = True
                        if oLine.insideEntity:
                            oLine.indentLevel = 1
                            iCurrentIndentLevel = 2
                        else:
                            oLine.indentLevel = 2
                            iCurrentIndentLevel = 3

                    if oLine.insidePortMap:
                        if re.match('^\s*\w+.*:', oLine.line) and not oLine.isComment and not oLine.isPortKeyword:
                            oLine.isPortDeclaration = True
                            if oLine.insideEntity:
                                oLine.indentLevel = 2
                            else:
                                oLine.indentLevel = 3
                        iOpenParenthesis += oLine.line.count('(')
                        iCloseParenthesis += oLine.line.count(')')
                        if iOpenParenthesis == iCloseParenthesis:
                            iOpenParenthesis = 0
                            iCloseParenthesis = 0
                            oLine.isEndPortMap = True
                            if oLine.insideEntity:
                                oLine.indentLevel = 1
                                iCurrentIndentLevel = 1
                            else:
                                oLine.indentLevel = 2
                                iCurrentIndentLevel = 2

                # Check generic map declarations
                if oLine.insideEntity or oLine.insideComponent:
                    if re.match('^\s*generic', oLine.lineLower) and not oLine.insideGenericMap:
                        oLine.isGenericKeyword = True
                        oLine.insideGenericMap = True
                        oLine.indentLevel = iCurrentIndentLevel
                        iCurrentIndentLevel += 1
                    if oLine.insideGenericMap:
                        if re.match('^\s*\S+.*:', oLine.line):
                            oLine.isGenericDeclaration = True
                            if not oLine.isGenericKeyword:
                                oLine.indentLevel = iCurrentIndentLevel
                        iOpenParenthesis += oLine.line.count('(')
                        iCloseParenthesis += oLine.line.count(')')
                        if iOpenParenthesis == iCloseParenthesis:
                            oLine.indentLevel = iCurrentIndentLevel - 1
                            iOpenParenthesis = 0
                            iCloseParenthesis = 0
                            oLine.isEndGenericMap = True
                            iCurrentIndentLevel = iCurrentIndentLevel - 2

                # Check architecture declarations
                if re.match('^\s*architecture', oLine.lineLower) and not oLine.insideArchitecture:
                    self.hasArchitecture = True
                    oLine.isArchitectureKeyword = True
                    oLine.insideArchitecture = True
                    oLine.indentLevel = 0
                    iCurrentIndentLevel = 1
                if oLine.insideArchitecture:
                    if re.match('^\s*begin', oLine.lineLower) and not fFoundArchitectureBegin and not oLine.insideFunction:
                        fFoundArchitectureBegin = True
                        oLine.isArchitectureBegin = True
                        oLine.indentLevel = 0
                        iCurrentIndentLevel = 1
                    if not oLine.insideProcess and not oLine.insideCase and not oLine.insideComponent and not oLine.insideGenerate and not oLine.insideFunction and not oLine.insideForLoop:
                        if re.match('^\s*end', oLine.lineLower):
                            fFoundArchitectureBegin = False
                            oLine.isEndArchitecture = True
                            oLine.indentLevel = 0
                            iCurrentIndentLevel = 0

                # Check package body declarations
                if re.match('^\s*package\s+body', oLine.lineLower) and not oLine.insidePackageBody:
                    oLine.isPackageBodyKeyword = True
                    oLine.insidePackageBody = True
                    oLine.indentLevel = 0
                    iCurrentIndentLevel = 1
                if oLine.insidePackageBody:
                    if not oLine.insideProcess and not oLine.insideCase and not oLine.insideComponent:
                        if re.match('^\s*end\s+', oLine.lineLower):
                            oLine.isPackageBodyEnd = True
                            oLine.indentLevel = 0
                            iCurrentIndentLevel = 0

                # Check package declarations
                if re.match('^\s*package', oLine.lineLower) and not oLine.insidePackage and not oLine.insidePackageBody:
                    oLine.isPackageKeyword = True
                    oLine.insidePackage = True
                    oLine.indentLevel = 0
                    iCurrentIndentLevel = 1
                if oLine.insidePackage:
                    if not oLine.insideProcess and not oLine.insideCase and not oLine.insideComponent:
                        if re.match('^\s*end\s+', oLine.lineLower):
                            oLine.isPackageEnd = True
                            oLine.indentLevel = 0
                            iCurrentIndentLevel = 0

                # Check Component declarations
                if re.match('^\s*component', oLine.lineLower) and not oLine.insideComponent:
                    oLine.isComponentDeclaration = True
                    oLine.insideComponent = True
                    oLine.indentLevel = 1
                    iCurrentIndentLevel += 1

                if oLine.insideComponent:
                    if re.match('^\s*end\s+component', oLine.lineLower):
                        oLine.isComponentEnd = True
                        oLine.indentLevel = 1
                        iCurrentIndentLevel -= 1

                # Check Signal declarations
                if oLine.insideArchitecture:
                    if re.match('^\s*signal', oLine.lineLower):
                        oLine.isSignal = True
                        oLine.indentLevel = 1

                # Check Constant declarations
                if oLine.insideArchitecture or oLine.insidePackage:
                    if re.match('^\s*constant', oLine.lineLower):
                        oLine.isConstant = True
                        oLine.indentLevel = 1

                # Check Variable declarations
                if oLine.insideArchitecture:
                    if re.match('^\s*variable', oLine.lineLower):
                        oLine.isVariable = True
                        oLine.indentLevel = iCurrentIndentLevel

                # Check process declarations
                if oLine.insideArchitecture:
                    if re.match('^\s*process', oLine.lineLower) or re.match('^\s*\S+\s*:\s*process', oLine.lineLower) and not oLine.isComment:
                        oLine.isProcessKeyword = True
                        oLine.insideProcess = True
                        oLine.indentLevel = iCurrentIndentLevel
                    if oLine.insideProcess:
                        # Check sensitivity list
                        if '(' in oLine.line and not oLine.insideSensitivityList and not fFoundProcessBegin and not fSensitivityListFound:
                            oLine.isSensitivityListBegin = True
                            oLine.insideSensitivityList = True
                            fSensitivityListFound = True
                        if oLine.insideSensitivityList:
                            iOpenParenthesis += oLine.line.count('(')
                            iCloseParenthesis += oLine.line.count(')')
                            if iOpenParenthesis == iCloseParenthesis:
                                oLine.isSensitivityListEnd = True
                                iOpenParenthesis = 0
                                iCloseParenthesis = 0
                                iCurrentIndentLevel += 1
                        if re.match('^.*\s+begin', oLine.lineLower) or re.match('^\s*begin', oLine.lineLower):
                            oLine.indentLevel = iCurrentIndentLevel - 1
                            oLine.isProcessBegin = True
                            fFoundProcessBegin = True
                        if re.match('^\s*end\s+process', oLine.lineLower):
                            oLine.indentLevel = iCurrentIndentLevel - 1
                            oLine.isEndProcess = True
                            fFoundProcessBegin = False
                            iCurrentIndentLevel = iCurrentIndentLevel - 1
                            fSensitivityListFound = False

                # Check generate declarations
                if oLine.insideArchitecture:
                    if re.match('^\s*\w+\s*:\s*if', oLine.lineLower) or re.match('^\s*\w+\s*:\s*for\s.*\sgenerate', oLine.lineLower):
                        oLine.insideGenerate = True
                    if oLine.insideGenerate:
                        if re.match('^\s*\w+\s*:\s*if\s.*\sgenerate', oLine.lineLower) or re.match('^\s*\w+\s*:\s*for\s.*\sgenerate', oLine.lineLower):
                            oLine.isGenerateKeyword = True
                            oLine.indentLevel = iCurrentIndentLevel
                            iCurrentIndentLevel += 1
                        if re.match('^\s*begin', oLine.lineLower):
                            oLine.isGenerateBegin = True
                            oLine.indentLevel = iCurrentIndentLevel - 1
                            fGenerateBeginFound = True
                        if re.match('^\s*end\s+generate', oLine.lineLower):
                            oLine.isGenerateEnd = True
                            iCurrentIndentLevel -= 1
                            oLine.indentLevel = iCurrentIndentLevel
                            fGenerateBeginFound = False

                # Check concurrent declarations
                if oLine.insideArchitecture and not oLine.insideProcess:
                    if re.match('^\s*\w+\s*<=', oLine.line) or re.match('^\s*\w+\s*:\s*\w+\s*<=', oLine.line):
                        oLine.indentLevel = iCurrentIndentLevel
                        oLine.isConcurrentBegin = True
                        oLine.insideConcurrent = True
                    if oLine.insideConcurrent:
                        if re.match('.*;', oLine.line):
                            oLine.isEndConcurrent = True

                # check for loop statements
                if oLine.insideArchitecture:
                    if re.match('^\s*for\s.*\sin\s.*\sloop', oLine.lineLower):
                        oLine.isForLoopKeyword = True
                        oLine.insideForLoop = True
                        oLine.indentLevel = iCurrentIndentLevel
                        iCurrentIndentLevel += 1
                    if re.match('^\s*end\s+loop', oLine.lineLower):
                        oLine.isForLoopEnd = True
                        iCurrentIndentLevel -= 1
                        oLine.indentLevel = iCurrentIndentLevel

                # Check if statements
                if oLine.insideProcess or oLine.insideFunction:
                    if re.match('^\s*if', oLine.lineLower):
                        oLine.isIfKeyword = True
                        oLine.insideIf = True
                        oLine.indentLevel = iCurrentIndentLevel
                        iCurrentIndentLevel += 1
                    if re.match('^\s*elsif', oLine.lineLower) or re.match('^.*\selsif', oLine.lineLower):
                        oLine.isElseIfKeyword = True
                        oLine.insideIf = True
                        oLine.indentLevel = iCurrentIndentLevel - 1
                    if oLine.insideIf and 'then' in oLine.lineLower:
                        oLine.isThenKeyword = True
                    if re.match('^\s*else', oLine.lineLower) or re.match('^.*\selse', oLine.lineLower):
                        oLine.isElseKeyword = True
                        oLine.indentLevel = iCurrentIndentLevel - 1
                    if re.match('^\s*end\s+if', oLine.lineLower) or re.match('^.*\send\s+if', oLine.lineLower):
                        oLine.isEndIfKeyword = True
                        iCurrentIndentLevel -= 1
                        oLine.indentLevel = iCurrentIndentLevel

                # Check case statements
                if oLine.insideProcess or oLine.insideFunction:
                    if re.match('^\s*case[\s|\(]', oLine.lineLower):
                        oLine.isCaseKeyword = True
                        oLine.insideCase = True
                        oLine.indentLevel = iCurrentIndentLevel
                        iCurrentIndentLevel += 2
                    if oLine.insideCase:
                        if re.match('^\s*.*[\s|\)]is\s', oLine.lineLower) or re.match('^\s*.*[\s|\)]is$', oLine.lineLower):
                            oLine.isCaseIsKeyword = True
                    if re.match('^\s*when\s', oLine.lineLower):
                        oLine.isCaseWhenKeyword = True
                        oLine.insideCaseWhen = True
                        oLine.indentLevel = iCurrentIndentLevel - 1
                        if self.lines[-1].isComment:
                            self.lines[-1].indentLevel -= 1
                    if oLine.insideCaseWhen:
                        if re.match('^\s*.*=>', oLine.line):
                            oLine.isCaseWhenEnd = True
                    if re.match('^\s*end\s+case', oLine.lineLower):
                        oLine.isEndCaseKeyword = True
                        oLine.indentLevel = iCurrentIndentLevel - 2
                        iCurrentIndentLevel -= 2

                # Check function declarations
                if oLine.insideArchitecture:
                    if re.match('^\s*function\s', oLine.lineLower) or re.match('^\s*impure\s', oLine.lineLower):
                        oLine.isFunctionKeyword = True
                        oLine.insideFunction = True
                        oLine.indentLevel = iCurrentIndentLevel
                        iCurrentIndentLevel += 1
                    if oLine.insideFunction:
                        if re.match('^\s*begin', oLine.lineLower):
                            oLine.isFunctionBegin = True
                            oLine.indentLevel = iCurrentIndentLevel - 1
                        if re.match('^\s*return', oLine.lineLower):
                            oLine.isFunctionReturn = True
                            oLine.indentLevel = iCurrentIndentLevel
                        if re.match('^\s*end', oLine.lineLower) and not oLine.isEndIfKeyword and not oLine.isEndCaseKeyword and not oLine.isForLoopEnd:
                            oLine.isFunctionEnd = True
                            oLine.indentLevel = iCurrentIndentLevel - 1
                            iCurrentIndentLevel -= 1

                # Check type declarations
                if oLine.insideArchitecture or oLine.insidePackage:
                    if re.match('^\s*type\s', oLine.lineLower):
                        oLine.isTypeKeyword = True
                        oLine.insideType = True
                        oLine.indentLevel = iCurrentIndentLevel
                        iCurrentIndentLevel += 1
                    if oLine.insideType:
                        if not oLine.isTypeKeyword and not oLine.isBlank:
                            oLine.indentLevel = iCurrentIndentLevel
                        if ';' in oLine.line:
                            oLine.isTypeEnd = True
                            iCurrentIndentLevel -= 1
                            if re.match('^\s*\)\s*;', oLine.line):
                                oLine.indentLevel = iCurrentIndentLevel

                # Check sequential statements
                if oLine.insideProcess:
                    if re.match('^.*<=', oLine.line) and not oLine.isComment and not oLine.insideIf and not oLine.isElseKeyword:
                        oLine.isSequential = True
                        oLine.insideSequential = True
                        oLine.indentLevel = iCurrentIndentLevel
                        oLine.sequentialAlignmentColumn = oLine.line.find('<=')
                    if oLine.insideSequential:
                        if ';' in oLine.line:
                            oLine.isSequentialEnd = True

                # Check variable assignment statements
                if oLine.insideProcess:
                    if re.match('^.*:=', oLine.line) and not oLine.isComment and not oLine.insideIf and not oLine.isElseKeyword and not oLine.isVariable:
                        oLine.isVariableAssignment = True
                        oLine.insideVariableAssignment = True
                        oLine.indentLevel = iCurrentIndentLevel
                        oLine.variableAssignmentAlignmentColumn = oLine.line.find(':=')
                    if oLine.insideVariableAssignment:
                        if ';' in oLine.line:
                            oLine.isVariableAssignmentEnd = True

                # Check instantiation statements
                if oLine.insideArchitecture and not oLine.insideProcess and not oLine.isConcurrentBegin and not oLine.insideComponent and not oLine.isGenerateKeyword and not oLine.insideFunction:
                    if re.match('^\s*\w+\s*:\s*\w+', oLine.line):
                        oLine.isInstantiationDeclaration = True
                        oLine.insideInstantiation = True
                        oLine.indentLevel = iCurrentIndentLevel
                        iCurrentIndentLevel += 1
                if oLine.insideInstantiation:
                    if re.match('^.*\s*port\s+map', oLine.lineLower):
                        if not oLine.indentLevel:
                            oLine.indentLevel = iCurrentIndentLevel
                        iCurrentIndentLevel += 1
                        oLine.isInstantiationPortKeyword = True
                        oLine.insideInstantiationPortMap = True
                    if re.match('^.*\s*generic\s+map', oLine.lineLower):
                        if not oLine.indentLevel:
                            oLine.indentLevel = iCurrentIndentLevel
                        oLine.insideInstantiationGenericMap = True
                        iCurrentIndentLevel += 1
                        oLine.isInstantiationGenericKeyword = True
                    if re.match('^.*=>', oLine.line):
                        if not oLine.indentLevel:
                            oLine.indentLevel = iCurrentIndentLevel
                        if oLine.insideInstantiationPortMap:
                            oLine.isInstantiationPortAssignment = True
                        else:
                            oLine.isInstantiationGenericAssignment = True
                    if ');' in oLine.line and oLine.insideInstantiationPortMap:
                        oLine.isInstantiationPortEnd = True
                        if not oLine.indentLevel:
                            oLine.indentLevel = iCurrentIndentLevel - 1
                        iCurrentIndentLevel -= 2
                    if ')' in oLine.line and oLine.insideInstantiationGenericMap:
                        oLine.isInstantiationGenericEnd = True
                        if not oLine.indentLevel:
                            oLine.indentLevel = iCurrentIndentLevel - 1
                        iCurrentIndentLevel -= 1

                # Add line to file
                self.lines.append(oLine)

        oFile.close()

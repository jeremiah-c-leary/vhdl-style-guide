import re
import line

class vhdlFile():

    def __init__(self, filename):
        self.filename = filename
        self.lines = [line.line('')]
        self.hasArchitecture = False
        self.hasEntity = False
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
        fSensitivityListFound = False

        fInsideIfStatement = False

        fInsideType = False

        fInsideCase = False
        fInsideCaseWhen = False

        fInsideSequential = False

        fInsideVariableAssignment = False

        fInsideComponent = False

        fInsideInstantiation = False
        fInsideInstantiationPortMap = False
        fInsideInstantiationGenericMap = False

        fInsidePackage = False
        fInsidePackageBody = False

        fInsideGenerate = False
        fGenerateBeginFound = False

        fInsideFunction = False

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
                    fInsideEntity = True
                    oLine.isEntityDeclaration = True
                    iCurrentIndentLevel = 1
                    oLine.indentLevel = 0
                # Assign inside entity attribute
                if fInsideEntity:
                    oLine.insideEntity = True
                # Check for the end of the entity
                if re.match('^\s*end', oLine.lineLower) and not fInsidePortMapDeclaration and not fInsideGenericMapDeclaration and fInsideEntity:
                    fInsideEntity = False
                    oLine.isEndEntityDeclaration = True
                    oLine.indentLevel = 0
                    iCurrentIndentLevel = 0

                # Check port map declarations
                if fInsideEntity or fInsideComponent:
                    if re.match('^\s*port', oLine.lineLower) and not fInsidePortMapDeclaration:
                        fInsidePortMapDeclaration = True
                        oLine.isPortKeyword = True
                        if fInsideEntity:
                            oLine.indentLevel = 1
                            iCurrentIndentLevel = 2
                        else:
                            oLine.indentLevel = 2
                            iCurrentIndentLevel = 3

                    if fInsidePortMapDeclaration:
                        oLine.insidePortMap = True
                        if re.match('^\s*\w+.*:', oLine.line) and not oLine.isComment and not oLine.isPortKeyword:
                            oLine.isPortDeclaration = True
                            if fInsideEntity:
                                oLine.indentLevel = 2
                            else:
                                oLine.indentLevel = 3
                        iOpenParenthesis += oLine.line.count('(')
                        iCloseParenthesis += oLine.line.count(')')
                        if iOpenParenthesis == iCloseParenthesis:
                            fInsidePortMapDeclaration = False
                            iOpenParenthesis = 0
                            iCloseParenthesis = 0
                            oLine.isEndPortMap = True
                            if fInsideEntity:
                                oLine.indentLevel = 1
                                iCurrentIndentLevel = 1
                            else:
                                oLine.indentLevel = 2
                                iCurrentIndentLevel = 2

                # Check generic map declarations
                if fInsideEntity or fInsideComponent:
                    if re.match('^\s*generic', oLine.lineLower) and not fInsideGenericMapDeclaration:
                        fInsideGenericMapDeclaration = True
                        oLine.isGenericKeyword = True
                        oLine.indentLevel = iCurrentIndentLevel
                        iCurrentIndentLevel += 1
                    if fInsideGenericMapDeclaration:
                        oLine.insideGenericMap = True
                        if re.match('^\s*\S+.*:', oLine.line):
                            oLine.isGenericDeclaration = True
                            if not oLine.isGenericKeyword:
                                oLine.indentLevel = iCurrentIndentLevel
                        iOpenParenthesis += oLine.line.count('(')
                        iCloseParenthesis += oLine.line.count(')')
                        if iOpenParenthesis == iCloseParenthesis:
                            oLine.indentLevel = iCurrentIndentLevel - 1
                            fInsideGenericMapDeclaration = False
                            iOpenParenthesis = 0
                            iCloseParenthesis = 0
                            oLine.isEndGenericMap = True
                            iCurrentIndentLevel = iCurrentIndentLevel - 2

                # Check architecture declarations
                if re.match('^\s*architecture', oLine.lineLower) and not fInsideArchitecture:
                    self.hasArchitecture = True
                    fInsideArchitecture = True
                    oLine.isArchitectureKeyword = True
                    oLine.indentLevel = 0
                    iCurrentIndentLevel = 1
                if fInsideArchitecture:
                    oLine.insideArchitecture = True
                    if re.match('^\s*begin', oLine.lineLower) and not fFoundArchitectureBegin and not fInsideFunction:
                        fFoundArchitectureBegin = True
                        oLine.isArchitectureBegin = True
                        oLine.indentLevel = 0
                        iCurrentIndentLevel = 1
                    if not fInsideProcess and not fInsideCase and not fInsideComponent and not fInsideGenerate and not fInsideFunction:
                        if re.match('^\s*end', oLine.lineLower):
                            fInsideArchitecture = False
                            fFoundArchitectureBegin = False
                            oLine.isEndArchitecture = True
                            oLine.indentLevel = 0
                            iCurrentIndentLevel = 0

                # Check package body declarations
                if re.match('^\s*package\s+body', oLine.lineLower) and not fInsidePackageBody:
                    fInsidePackageBody = True
                    oLine.isPackageBodyKeyword = True
                    oLine.indentLevel = 0
                    iCurrentIndentLevel = 1
                if fInsidePackageBody:
                    oLine.insidePackageBody = True
                    if not fInsideProcess and not fInsideCase and not fInsideComponent:
                        if re.match('^\s*end\s+', oLine.lineLower):
                            fInsidePackageBody = False
                            oLine.isPackageBodyEnd = True
                            oLine.indentLevel = 0
                            iCurrentIndentLevel = 0

                # Check package declarations
                if re.match('^\s*package', oLine.lineLower) and not fInsidePackage and not fInsidePackageBody:
                    fInsidePackage = True
                    oLine.isPackageKeyword = True
                    oLine.indentLevel = 0
                    iCurrentIndentLevel = 1
                if fInsidePackage:
                    oLine.insidePackage = True
                    if not fInsideProcess and not fInsideCase and not fInsideComponent:
                        if re.match('^\s*end\s+', oLine.lineLower):
                            fInsidePackage = False
                            oLine.isPackageEnd = True
                            oLine.indentLevel = 0
                            iCurrentIndentLevel = 0

                # Check Component declarations
                if re.match('^\s*component', oLine.lineLower) and not fInsideComponent:
                    oLine.isComponentDeclaration = True
                    fInsideComponent = True
                    oLine.indentLevel = 1
                    iCurrentIndentLevel += 1

                if fInsideComponent:
                    oLine.insideComponent = True
                    if re.match('^\s*end\s+component', oLine.lineLower):
                        oLine.isComponentEnd = True
                        fInsideComponent = False
                        oLine.indentLevel = 1
                        iCurrentIndentLevel -= 1

                # Check Signal declarations
                if fInsideArchitecture:
                    if re.match('^\s*signal', oLine.lineLower):
                        oLine.isSignal = True
                        oLine.indentLevel = 1

                # Check Constant declarations
                if fInsideArchitecture or fInsidePackage:
                    if re.match('^\s*constant', oLine.lineLower):
                        oLine.isConstant = True
                        oLine.indentLevel = 1

                # Check Variable declarations
                if fInsideArchitecture:
                    if re.match('^\s*variable', oLine.lineLower):
                        oLine.isVariable = True
                        oLine.indentLevel = iCurrentIndentLevel

                # Check process declarations
                if fInsideArchitecture:
                    if re.match('^\s*process', oLine.lineLower) or re.match('^\s*\S+\s*:\s*process', oLine.lineLower) and not oLine.isComment:
                        fInsideProcess = True
                        oLine.isProcessKeyword = True
                        oLine.indentLevel = iCurrentIndentLevel
                    if fInsideProcess == True:
                        oLine.insideProcess = True
                        # Check sensitivity list
                        if '(' in oLine.line and not fInsideSensitivityList and not fFoundProcessBegin and not fSensitivityListFound:
                            fInsideSensitivityList = True
                            oLine.isSensitivityListBegin = True
                            fSensitivityListFound = True
                        if fInsideSensitivityList:
                            oLine.insideSensitivityList = True
                            iOpenParenthesis += oLine.line.count('(')
                            iCloseParenthesis += oLine.line.count(')')
                            if iOpenParenthesis == iCloseParenthesis:
                                fInsideSensitivityList = False
                                oLine.isSensitivityListEnd = True
                                iOpenParenthesis = 0
                                iCloseParenthesis = 0
                                iCurrentIndentLevel += 1
                        if re.match('^.*\s+begin', oLine.lineLower) or re.match('^\s*begin', oLine.lineLower):
                            oLine.indentLevel = iCurrentIndentLevel - 1
                            oLine.isProcessBegin = True
                            fFoundProcessBegin = True
                            #iCurrentIndentLevel += 1
                        if re.match('^\s*end\s+process', oLine.lineLower):
                            fInsideProcess = False
                            oLine.indentLevel = iCurrentIndentLevel - 1
                            oLine.isEndProcess = True
                            fFoundProcessBegin = False
                            iCurrentIndentLevel = iCurrentIndentLevel - 1
                            fSensitivityListFound = False

                # Check generate declarations
                if fInsideArchitecture:
                    if re.match('^\s*\w+\s*:\s*if', oLine.lineLower) or re.match('^\s*\w+\s*:\s*for\s.*\sgenerate', oLine.lineLower):
                        fInsideGenerate = True
                    if fInsideGenerate:
                        if re.match('^\s*\w+\s*:\s*if\s.*\sgenerate', oLine.lineLower) or re.match('^\s*\w+\s*:\s*for\s.*\sgenerate', oLine.lineLower):
                            oLine.isGenerateKeyword = True
                            oLine.indentLevel = iCurrentIndentLevel
                            iCurrentIndentLevel += 1
                        if re.match('^\s*begin', oLine.lineLower):
                            oLine.isGenerateBegin = True
                            oLine.indentLevel = iCurrentIndentLevel - 1
                            fGenerateBeginFound = True
                        if re.match('^\s*end\s+generate', oLine.lineLower):
                            fInsideGenerate = False
                            oLine.isGenerateEnd = True
                            iCurrentIndentLevel -= 1
                            oLine.indentLevel = iCurrentIndentLevel
                            fGenerateBeginFound = False

                # Check concurrent declarations
                if fInsideArchitecture and not fInsideProcess:
                    if re.match('^\s*\w+\s*<=', oLine.line) or re.match('^\s*\w+\s*:\s*\w+\s*<=', oLine.line):
                        fInsideConcurrent = True
                        oLine.indentLevel = iCurrentIndentLevel
                        oLine.isConcurrentBegin = True
                    if fInsideConcurrent:
                        oLine.insideConcurrent = True
                        if re.match('.*;', oLine.line):
                            fInsideConcurrent = False
                            oLine.isEndConcurrent = True

                # check for loop statements
                if fInsideProcess:
                    if re.match('^\s*for\s.*\sin\s.*\sloop', oLine.lineLower):
                        oLine.isForLoopKeyword = True
                        oLine.indentLevel = iCurrentIndentLevel
                        iCurrentIndentLevel += 1
                    if re.match('^\s*end\s+loop', oLine.lineLower):
                        oLine.isForLoopEnd = True
                        iCurrentIndentLevel -= 1
                        oLine.indentLevel = iCurrentIndentLevel

                # Check if statements
                if fInsideProcess or fInsideFunction:
                    if re.match('^\s*if', oLine.lineLower):
                        oLine.isIfKeyword = True
                        fInsideIfStatement = True
                        oLine.indentLevel = iCurrentIndentLevel
                        iCurrentIndentLevel += 1
                    if re.match('^\s*elsif', oLine.lineLower) or re.match('^.*\selsif', oLine.lineLower):
                        oLine.isElseIfKeyword = True
                        fInsideIfStatement = True
                        oLine.indentLevel = iCurrentIndentLevel - 1
                    if fInsideIfStatement:
                        oLine.insideIf = True
                    if fInsideIfStatement and 'then' in oLine.lineLower:
                        oLine.isThenKeyword = True
                        fInsideIfStatement = False
                    if re.match('^\s*else', oLine.lineLower) or re.match('^.*\selse', oLine.lineLower):
                        oLine.isElseKeyword = True
                        oLine.indentLevel = iCurrentIndentLevel - 1
                    if re.match('^\s*end\s+if', oLine.lineLower) or re.match('^.*\send\s+if', oLine.lineLower):
                        oLine.isEndIfKeyword = True
                        iCurrentIndentLevel -= 1
                        oLine.indentLevel = iCurrentIndentLevel
                        fInsideIfStatement = False

                # Check case statements
                if fInsideProcess or fInsideFunction:
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
                        iCurrentIndentLevel -= 2

                # Check function declarations
                if fInsideArchitecture:
                    if re.match('^\s*function\s', oLine.lineLower):
                        fInsideFunction = True
                        oLine.isFunctionKeyword = True
                        oLine.indentLevel = iCurrentIndentLevel
                        iCurrentIndentLevel += 1
                    if fInsideFunction:
                        oLine.insideFunction = True
                        if re.match('^\s*begin', oLine.lineLower):
                            oLine.isFunctionBegin = True
                            oLine.indentLevel = iCurrentIndentLevel - 1
                        if re.match('^\s*return', oLine.lineLower):
                            oLine.isFunctionReturn = True
                            oLine.indentLevel = iCurrentIndentLevel 
                        if re.match('^\s*end', oLine.lineLower) and not oLine.isEndIfKeyword and not oLine.isEndCaseKeyword:
                            oLine.isFunctionEnd = True
                            oLine.indentLevel = iCurrentIndentLevel - 1
                            iCurrentIndentLevel -= 1
                            fInsideFunction = False

                # Check type declarations
                if fInsideArchitecture or fInsidePackage:
                    if re.match('^\s*type\s', oLine.lineLower):
                        fInsideType = True
                        oLine.isTypeKeyword = True
                        oLine.indentLevel = iCurrentIndentLevel
                        iCurrentIndentLevel += 1
                    if fInsideType:
                        oLine.insideType = True
                        if not oLine.isTypeKeyword and not oLine.isBlank:
                            oLine.indentLevel = iCurrentIndentLevel
                        if ';' in oLine.line:
                            fInsideType = False
                            oLine.isTypeEnd = True
                            iCurrentIndentLevel -= 1

                # Check sequential statements
                if fInsideProcess:
                    if re.match('^.*<=', oLine.line) and not oLine.isComment and not oLine.insideIf and not oLine.isElseKeyword:
                        oLine.isSequential = True
                        oLine.indentLevel = iCurrentIndentLevel
                        fInsideSequential = True
                        oLine.sequentialAlignmentColumn = oLine.line.find('<=')
                    if fInsideSequential:
                        oLine.insideSequential = True
                        if ';' in oLine.line:
                            fInsideSequential = False
                            oLine.isSequentialEnd = True

                # Check variable assignment statements
                if fInsideProcess:
                    if re.match('^.*:=', oLine.line) and not oLine.isComment and not oLine.insideIf and not oLine.isElseKeyword and not oLine.isVariable:
                        oLine.isVariableAssignment = True
                        oLine.indentLevel = iCurrentIndentLevel
                        fInsideVariableAssignment = True
                        oLine.variableAssignmentAlignmentColumn = oLine.line.find(':=')
                    if fInsideVariableAssignment:
                        oLine.insideVariableAssignment = True
                        if ';' in oLine.line:
                            fInsideVariableAssignment = False
                            oLine.isVariableAssignmentEnd = True

                # Check instantiation statements
                if fInsideArchitecture and not fInsideProcess and not oLine.isConcurrentBegin and not fInsideComponent and not oLine.isGenerateKeyword and not fInsideFunction:
                    if re.match('^\s*\w+\s*:\s*\w+', oLine.line):
                        oLine.isInstantiationDeclaration = True
                        oLine.indentLevel = iCurrentIndentLevel
                        iCurrentIndentLevel += 1
                        fInsideInstantiation = True
                if fInsideInstantiation:
                    oLine.insideInstantiation = True
                    if re.match('^.*\s*port\s+map', oLine.lineLower):
                        if not oLine.indentLevel:
                            oLine.indentLevel = iCurrentIndentLevel
                        iCurrentIndentLevel += 1
                        oLine.isInstantiationPortKeyword = True
                        fInsideInstantiationPortMap = True
                    if re.match('^.*\s*generic\s+map', oLine.lineLower):
                        if not oLine.indentLevel:
                            oLine.indentLevel = iCurrentIndentLevel
                        iCurrentIndentLevel += 1
                        oLine.isInstantiationGenericKeyword = True
                        fInsideInstantiationGenericMap = True
                    if re.match('^.*=>', oLine.line):
                        if not oLine.indentLevel:
                            oLine.indentLevel = iCurrentIndentLevel
                        if fInsideInstantiationPortMap:
                            oLine.isInstantiationPortAssignment = True
                        else:
                            oLine.isInstantiationGenericAssignment = True
                    if ');' in oLine.line and fInsideInstantiationPortMap:
                        fInsideInstantiation = False
                        fInsideInstantiationPortMap = False
                        oLine.isInstantiationPortEnd = True
                        if not oLine.indentLevel:
                            oLine.indentLevel = iCurrentIndentLevel - 1
                        iCurrentIndentLevel -= 2
                    if ')' in oLine.line and fInsideInstantiationGenericMap:
                        fInsideInstantiationGenericMap = False
                        oLine.isInstantiationGenericEnd = True
                        if not oLine.indentLevel:
                            oLine.indentLevel = iCurrentIndentLevel - 1
                        iCurrentIndentLevel -= 1



                # Add line to file
                self.lines.append(oLine)


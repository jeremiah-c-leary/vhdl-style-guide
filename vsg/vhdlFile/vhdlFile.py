import re
from vsg import line
from vsg.vhdlFile import update


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

        dVars = {}
        dVars['fFoundProcessBegin'] = False
        dVars['SensitivityListFound'] = False

        dVars['iOpenParenthesis'] = 0
        dVars['iCloseParenthesis'] = 0

        dVars['iCurrentIndentLevel'] = 0

        with open(self.filename) as oFile:
            for sLine in oFile:
                sLine = sLine.replace('\t', '  ')
                oLine = line.line(sLine.rstrip())
                update.inside_attributes(self.lines[-1], oLine)
                # Check for blank lines
                if re.match('^\s*$', oLine.line):
                    oLine.isBlank = True
                # Check for comment lines
                if '--' in oLine.line:
                    oLine.hasComment = True
                    oLine.commentColumn = oLine.line.find('--')
                if re.match('^\s*--', oLine.line):
                    oLine.isComment = True
                    oLine.indentLevel = dVars['iCurrentIndentLevel']
                # Check for null statements
                if re.match('^\s*null\s*;', oLine.lineLower):
                    oLine.indentLevel = dVars['iCurrentIndentLevel']
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
                    dVars['iCurrentIndentLevel'] = 1
                    oLine.indentLevel = 0
                    oLine.insideEntity = True
                # Check for the end of the entity
                if re.match('^\s*end', oLine.lineLower) and not oLine.insidePortMap and not oLine.insideGenericMap and oLine.insideEntity:
                    oLine.isEndEntityDeclaration = True
                    oLine.indentLevel = 0
                    dVars['iCurrentIndentLevel'] = 0

                # Check port map declarations
                if oLine.insideEntity or oLine.insideComponent:
                    if re.match('^\s*port', oLine.lineLower) and not oLine.insidePortMap:
                        oLine.isPortKeyword = True
                        oLine.insidePortMap = True
                        if oLine.insideEntity:
                            oLine.indentLevel = 1
                            dVars['iCurrentIndentLevel'] = 2
                        else:
                            oLine.indentLevel = 2
                            dVars['iCurrentIndentLevel'] = 3

                    if oLine.insidePortMap:
                        if re.match('^\s*\w+.*:', oLine.line) and not oLine.isComment and not oLine.isPortKeyword:
                            oLine.isPortDeclaration = True
                            if oLine.insideEntity:
                                oLine.indentLevel = 2
                            else:
                                oLine.indentLevel = 3
                        dVars['iOpenParenthesis'] += oLine.line.count('(')
                        dVars['iCloseParenthesis'] += oLine.line.count(')')
                        if dVars['iOpenParenthesis'] == dVars['iCloseParenthesis']:
                            dVars['iOpenParenthesis'] = 0
                            dVars['iCloseParenthesis'] = 0
                            oLine.isEndPortMap = True
                            if oLine.insideEntity:
                                oLine.indentLevel = 1
                                dVars['iCurrentIndentLevel'] = 1
                            else:
                                oLine.indentLevel = 2
                                dVars['iCurrentIndentLevel'] = 2

                # Check generic map declarations
                if oLine.insideEntity or oLine.insideComponent:
                    if re.match('^\s*generic', oLine.lineLower) and not oLine.insideGenericMap:
                        oLine.isGenericKeyword = True
                        oLine.insideGenericMap = True
                        oLine.indentLevel = dVars['iCurrentIndentLevel']
                        dVars['iCurrentIndentLevel'] += 1
                    if oLine.insideGenericMap:
                        if re.match('^\s*\S+.*:', oLine.line):
                            oLine.isGenericDeclaration = True
                            if not oLine.isGenericKeyword:
                                oLine.indentLevel = dVars['iCurrentIndentLevel']
                        dVars['iOpenParenthesis'] += oLine.line.count('(')
                        dVars['iCloseParenthesis'] += oLine.line.count(')')
                        if dVars['iOpenParenthesis'] == dVars['iCloseParenthesis']:
                            oLine.indentLevel = dVars['iCurrentIndentLevel'] - 1
                            dVars['iOpenParenthesis'] = 0
                            dVars['iCloseParenthesis'] = 0
                            oLine.isEndGenericMap = True
                            dVars['iCurrentIndentLevel'] = dVars['iCurrentIndentLevel'] - 2

                # Check architecture declarations
                if re.match('^\s*architecture', oLine.lineLower) and not oLine.insideArchitecture:
                    self.hasArchitecture = True
                    oLine.isArchitectureKeyword = True
                    oLine.insideArchitecture = True
                    oLine.indentLevel = 0
                    dVars['iCurrentIndentLevel'] = 1
                if oLine.insideArchitecture:
                    if re.match('^\s*begin', oLine.lineLower) and not oLine.insideFunction and not oLine.insideProcess and not oLine.insideGenerate:
                        oLine.isArchitectureBegin = True
                        oLine.indentLevel = 0
                        dVars['iCurrentIndentLevel'] = 1
                    if not oLine.insideProcess and not oLine.insideCase and not oLine.insideComponent and not oLine.insideGenerate and not oLine.insideFunction and not oLine.insideForLoop:
                        if re.match('^\s*end', oLine.lineLower):
                            oLine.isEndArchitecture = True
                            oLine.indentLevel = 0
                            dVars['iCurrentIndentLevel'] = 0

                # Check package body declarations
                if re.match('^\s*package\s+body', oLine.lineLower) and not oLine.insidePackageBody:
                    oLine.isPackageBodyKeyword = True
                    oLine.insidePackageBody = True
                    oLine.indentLevel = 0
                    dVars['iCurrentIndentLevel'] = 1
                if oLine.insidePackageBody:
                    if not oLine.insideProcess and not oLine.insideCase and not oLine.insideComponent:
                        if re.match('^\s*end\s+', oLine.lineLower):
                            oLine.isPackageBodyEnd = True
                            oLine.indentLevel = 0
                            dVars['iCurrentIndentLevel'] = 0

                # Check package declarations
                if re.match('^\s*package', oLine.lineLower) and not oLine.insidePackage and not oLine.insidePackageBody:
                    oLine.isPackageKeyword = True
                    oLine.insidePackage = True
                    oLine.indentLevel = 0
                    dVars['iCurrentIndentLevel'] = 1
                if oLine.insidePackage:
                    if not oLine.insideProcess and not oLine.insideCase and not oLine.insideComponent:
                        if re.match('^\s*end\s+', oLine.lineLower):
                            oLine.isPackageEnd = True
                            oLine.indentLevel = 0
                            dVars['iCurrentIndentLevel'] = 0

                # Check Component declarations
                if re.match('^\s*component', oLine.lineLower) and not oLine.insideComponent:
                    oLine.isComponentDeclaration = True
                    oLine.insideComponent = True
                    oLine.indentLevel = 1
                    dVars['iCurrentIndentLevel'] += 1

                if oLine.insideComponent:
                    if re.match('^\s*end\s+component', oLine.lineLower):
                        oLine.isComponentEnd = True
                        oLine.indentLevel = 1
                        dVars['iCurrentIndentLevel'] -= 1

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
                        oLine.indentLevel = dVars['iCurrentIndentLevel']

                # Check process declarations
                if oLine.insideArchitecture:
                    if re.match('^\s*process', oLine.lineLower) or re.match('^\s*\S+\s*:\s*process', oLine.lineLower) and not oLine.isComment:
                        oLine.isProcessKeyword = True
                        oLine.insideProcess = True
                        oLine.indentLevel = dVars['iCurrentIndentLevel']
                    if oLine.insideProcess:
                        # Check sensitivity list
                        if '(' in oLine.line and not oLine.insideSensitivityList and not dVars['fFoundProcessBegin'] and not dVars['SensitivityListFound']:
                            oLine.isSensitivityListBegin = True
                            oLine.insideSensitivityList = True
                            dVars['SensitivityListFound'] = True
                        if oLine.insideSensitivityList:
                            dVars['iOpenParenthesis'] += oLine.line.count('(')
                            dVars['iCloseParenthesis'] += oLine.line.count(')')
                            if dVars['iOpenParenthesis'] == dVars['iCloseParenthesis']:
                                oLine.isSensitivityListEnd = True
                                dVars['iOpenParenthesis'] = 0
                                dVars['iCloseParenthesis'] = 0
                                dVars['iCurrentIndentLevel'] += 1
                        if re.match('^.*\s+begin', oLine.lineLower) or re.match('^\s*begin', oLine.lineLower):
                            oLine.indentLevel = dVars['iCurrentIndentLevel'] - 1
                            oLine.isProcessBegin = True
                            dVars['fFoundProcessBegin'] = True
                        if re.match('^\s*end\s+process', oLine.lineLower):
                            oLine.indentLevel = dVars['iCurrentIndentLevel'] - 1
                            oLine.isEndProcess = True
                            dVars['fFoundProcessBegin'] = False
                            dVars['iCurrentIndentLevel'] = dVars['iCurrentIndentLevel'] - 1
                            dVars['SensitivityListFound'] = False

                # Check generate declarations
                if oLine.insideArchitecture:
                    if re.match('^\s*\w+\s*:\s*if', oLine.lineLower) or re.match('^\s*\w+\s*:\s*for\s.*\sgenerate', oLine.lineLower):
                        oLine.insideGenerate = True
                    if oLine.insideGenerate:
                        if re.match('^\s*\w+\s*:\s*if\s.*\sgenerate', oLine.lineLower) or re.match('^\s*\w+\s*:\s*for\s.*\sgenerate', oLine.lineLower):
                            oLine.isGenerateKeyword = True
                            oLine.indentLevel = dVars['iCurrentIndentLevel']
                            dVars['iCurrentIndentLevel'] += 1
                        if re.match('^\s*begin', oLine.lineLower):
                            oLine.isGenerateBegin = True
                            oLine.indentLevel = dVars['iCurrentIndentLevel'] - 1
                        if re.match('^\s*end\s+generate', oLine.lineLower):
                            oLine.isGenerateEnd = True
                            dVars['iCurrentIndentLevel'] -= 1
                            oLine.indentLevel = dVars['iCurrentIndentLevel']

                # Check concurrent declarations
                if oLine.insideArchitecture and not oLine.insideProcess:
                    if re.match('^\s*\w+\s*<=', oLine.line) or re.match('^\s*\w+\s*:\s*\w+\s*<=', oLine.line):
                        oLine.indentLevel = dVars['iCurrentIndentLevel']
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
                        oLine.indentLevel = dVars['iCurrentIndentLevel']
                        dVars['iCurrentIndentLevel'] += 1
                    if re.match('^\s*end\s+loop', oLine.lineLower):
                        oLine.isForLoopEnd = True
                        dVars['iCurrentIndentLevel'] -= 1
                        oLine.indentLevel = dVars['iCurrentIndentLevel']

                # Check if statements
                if oLine.insideProcess or oLine.insideFunction:
                    if re.match('^\s*if', oLine.lineLower):
                        oLine.isIfKeyword = True
                        oLine.insideIf = True
                        oLine.indentLevel = dVars['iCurrentIndentLevel']
                        dVars['iCurrentIndentLevel'] += 1
                    if re.match('^\s*elsif', oLine.lineLower) or re.match('^.*\selsif', oLine.lineLower):
                        oLine.isElseIfKeyword = True
                        oLine.insideIf = True
                        oLine.indentLevel = dVars['iCurrentIndentLevel'] - 1
                    if oLine.insideIf and 'then' in oLine.lineLower:
                        oLine.isThenKeyword = True
                    if re.match('^\s*else', oLine.lineLower) or re.match('^.*\selse', oLine.lineLower):
                        oLine.isElseKeyword = True
                        oLine.indentLevel = dVars['iCurrentIndentLevel'] - 1
                    if re.match('^\s*end\s+if', oLine.lineLower) or re.match('^.*\send\s+if', oLine.lineLower):
                        oLine.isEndIfKeyword = True
                        dVars['iCurrentIndentLevel'] -= 1
                        oLine.indentLevel = dVars['iCurrentIndentLevel']

                # Check case statements
                if oLine.insideProcess or oLine.insideFunction:
                    if re.match('^\s*case[\s|\(]', oLine.lineLower):
                        oLine.isCaseKeyword = True
                        oLine.insideCase = True
                        oLine.indentLevel = dVars['iCurrentIndentLevel']
                        dVars['iCurrentIndentLevel'] += 2
                    if oLine.insideCase:
                        if re.match('^\s*.*[\s|\)]is\s', oLine.lineLower) or re.match('^\s*.*[\s|\)]is$', oLine.lineLower):
                            oLine.isCaseIsKeyword = True
                    if re.match('^\s*when\s', oLine.lineLower):
                        oLine.isCaseWhenKeyword = True
                        oLine.insideCaseWhen = True
                        oLine.indentLevel = dVars['iCurrentIndentLevel'] - 1
                        if self.lines[-1].isComment:
                            self.lines[-1].indentLevel -= 1
                    if oLine.insideCaseWhen:
                        if re.match('^\s*.*=>', oLine.line):
                            oLine.isCaseWhenEnd = True
                    if re.match('^\s*end\s+case', oLine.lineLower):
                        oLine.isEndCaseKeyword = True
                        oLine.indentLevel = dVars['iCurrentIndentLevel'] - 2
                        dVars['iCurrentIndentLevel'] -= 2

                # Check function declarations
                if oLine.insideArchitecture:
                    if re.match('^\s*function\s', oLine.lineLower) or re.match('^\s*impure\s', oLine.lineLower):
                        oLine.isFunctionKeyword = True
                        oLine.insideFunction = True
                        oLine.indentLevel = dVars['iCurrentIndentLevel']
                        dVars['iCurrentIndentLevel'] += 1
                    if oLine.insideFunction:
                        if re.match('^\s*begin', oLine.lineLower):
                            oLine.isFunctionBegin = True
                            oLine.indentLevel = dVars['iCurrentIndentLevel'] - 1
                        if re.match('^\s*return', oLine.lineLower):
                            oLine.isFunctionReturn = True
                            oLine.indentLevel = dVars['iCurrentIndentLevel']
                        if re.match('^\s*end', oLine.lineLower) and not oLine.isEndIfKeyword and not oLine.isEndCaseKeyword and not oLine.isForLoopEnd:
                            oLine.isFunctionEnd = True
                            oLine.indentLevel = dVars['iCurrentIndentLevel'] - 1
                            dVars['iCurrentIndentLevel'] -= 1

                # Check type declarations
                if oLine.insideArchitecture or oLine.insidePackage:
                    if re.match('^\s*type\s', oLine.lineLower):
                        oLine.isTypeKeyword = True
                        oLine.insideType = True
                        oLine.indentLevel = dVars['iCurrentIndentLevel']
                        dVars['iCurrentIndentLevel'] += 1
                    if oLine.insideType:
                        if not oLine.isTypeKeyword and not oLine.isBlank:
                            oLine.indentLevel = dVars['iCurrentIndentLevel']
                        if ';' in oLine.line:
                            oLine.isTypeEnd = True
                            dVars['iCurrentIndentLevel'] -= 1
                            if re.match('^\s*\)\s*;', oLine.line):
                                oLine.indentLevel = dVars['iCurrentIndentLevel']

                # Check sequential statements
                if oLine.insideProcess:
                    if re.match('^.*<=', oLine.line) and not oLine.isComment and not oLine.insideIf and not oLine.isElseKeyword:
                        oLine.isSequential = True
                        oLine.insideSequential = True
                        oLine.indentLevel = dVars['iCurrentIndentLevel']
                        oLine.sequentialAlignmentColumn = oLine.line.find('<=')
                    if oLine.insideSequential:
                        if ';' in oLine.line:
                            oLine.isSequentialEnd = True

                # Check variable assignment statements
                if oLine.insideProcess:
                    if re.match('^.*:=', oLine.line) and not oLine.isComment and not oLine.insideIf and not oLine.isElseKeyword and not oLine.isVariable:
                        oLine.isVariableAssignment = True
                        oLine.insideVariableAssignment = True
                        oLine.indentLevel = dVars['iCurrentIndentLevel']
                        oLine.variableAssignmentAlignmentColumn = oLine.line.find(':=')
                    if oLine.insideVariableAssignment:
                        if ';' in oLine.line:
                            oLine.isVariableAssignmentEnd = True

                # Check instantiation statements
                if oLine.insideArchitecture and not oLine.insideProcess and not oLine.isConcurrentBegin and not oLine.insideComponent and not oLine.isGenerateKeyword and not oLine.insideFunction:
                    if re.match('^\s*\w+\s*:\s*\w+', oLine.line):
                        oLine.isInstantiationDeclaration = True
                        oLine.insideInstantiation = True
                        oLine.indentLevel = dVars['iCurrentIndentLevel']
                        dVars['iCurrentIndentLevel'] += 1
                if oLine.insideInstantiation:
                    if re.match('^.*\s*port\s+map', oLine.lineLower):
                        if not oLine.indentLevel:
                            oLine.indentLevel = dVars['iCurrentIndentLevel']
                        dVars['iCurrentIndentLevel'] += 1
                        oLine.isInstantiationPortKeyword = True
                        oLine.insideInstantiationPortMap = True
                    if re.match('^.*\s*generic\s+map', oLine.lineLower):
                        if not oLine.indentLevel:
                            oLine.indentLevel = dVars['iCurrentIndentLevel']
                        oLine.insideInstantiationGenericMap = True
                        dVars['iCurrentIndentLevel'] += 1
                        oLine.isInstantiationGenericKeyword = True
                    if re.match('^.*=>', oLine.line):
                        if not oLine.indentLevel:
                            oLine.indentLevel = dVars['iCurrentIndentLevel']
                        if oLine.insideInstantiationPortMap:
                            oLine.isInstantiationPortAssignment = True
                        else:
                            oLine.isInstantiationGenericAssignment = True
                    if ');' in oLine.line and oLine.insideInstantiationPortMap:
                        oLine.isInstantiationPortEnd = True
                        if not oLine.indentLevel:
                            oLine.indentLevel = dVars['iCurrentIndentLevel'] - 1
                        dVars['iCurrentIndentLevel'] -= 2
                    if ')' in oLine.line and oLine.insideInstantiationGenericMap:
                        oLine.isInstantiationGenericEnd = True
                        if not oLine.indentLevel:
                            oLine.indentLevel = dVars['iCurrentIndentLevel'] - 1
                        dVars['iCurrentIndentLevel'] -= 1

                # Add line to file
                self.lines.append(oLine)

        oFile.close()

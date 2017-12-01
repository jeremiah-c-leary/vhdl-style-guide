import re


def architecture(self, dVars, oLine):

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

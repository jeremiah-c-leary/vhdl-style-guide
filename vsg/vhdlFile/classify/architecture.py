import re


def architecture(self, dVars, oLine):

    classify_architecture_keyword(self, dVars, oLine)
    if oLine.insideArchitecture:
        classify_begin_keyword(dVars, oLine)
        classify_end_keyword(dVars, oLine)


def classify_architecture_keyword(self, dVars, oLine):
    if re.match('^\s*architecture', oLine.lineLower) and not oLine.insideArchitecture:
        self.hasArchitecture = True
        oLine.isArchitectureKeyword = True
        oLine.insideArchitecture = True
        oLine.indentLevel = 0
        dVars['iCurrentIndentLevel'] = 1


def classify_begin_keyword(dVars, oLine):
        if re.match('^\s*begin', oLine.lineLower) and not oLine.insideFunction and \
           not oLine.insideProcess and not oLine.insideGenerate and \
           not oLine.insideProcedure and not oLine.insideBlock:
            oLine.isArchitectureBegin = True
            oLine.indentLevel = 0
            dVars['iCurrentIndentLevel'] = 1


def classify_end_keyword(dVars, oLine):
    if not oLine.insideProcess and not oLine.insideCase and \
       not oLine.insideComponent and not oLine.insideGenerate and \
       not oLine.insideFunction and not oLine.insideForLoop and \
       not oLine.insideWhileLoop and not oLine.insideTypeRecord and \
       not oLine.insideProcedure and not oLine.insideBlock:
        if re.match('^\s*end', oLine.lineLower):
            oLine.isEndArchitecture = True
            oLine.indentLevel = 0
            dVars['iCurrentIndentLevel'] = 0

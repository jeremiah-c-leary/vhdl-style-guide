import re


'''
architecture identifier of entity_name is

    architecture_declarative_part

begin

    architecture_statement_part

end [ architecture ] [ architecture_simple_name ] 
'''


def architecture(self, dVars, lTokens, lObjects, oLine):
    classify_architecture_keyword_old(self, dVars, oLine)
    if oLine.insideArchitecture:
        classify_begin_keyword(dVars, oLine)
        classify_end_keyword(dVars, oLine)

def classify_architecture_semicolon(sToken, iToken, lObjects, dVars, oLine):
    if sToken == ';':
        dVars['bArchitectureKeywordFound'] = False
        dVars['bArchitectureIdentifierFound'] = False
        dVars['bArchitectureEntityNameFound'] = False
        dVars['bArchitectureIsKeywordFound'] = False
        dVars['bArchitectureBeginKeywordFound'] = False
        dVars['bArchitectureEndKeywordFound'] = False


def classify_architecture_keyword_old(self, dVars, oLine):
    if re.match('^\s*architecture', oLine.lineLower) and not oLine.insideArchitecture:
        self.hasArchitecture = True
        oLine.isArchitectureKeyword = True
        oLine.insideArchitecture = True
        oLine.insideArchitectureDeclarativeRegion = True
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
       not oLine.insideProcedure and not oLine.insideBlock and \
       not oLine.insideConcurrent and not oLine.insideInstantiation:
        if re.match('^\s*end', oLine.lineLower) and not \
           re.match('^\s*end\S+\s*:', oLine.lineLower) and not \
           re.match('^\s*end_', oLine.lineLower):
            oLine.isEndArchitecture = True
            oLine.indentLevel = 0
            dVars['iCurrentIndentLevel'] = 0

import re

from vsg import parser


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

    for iToken, sToken in enumerate(lTokens):
        if not dVars['bArchitectureKeywordFound']:
            classify_architecture_keyword(sToken, iToken, lObjects, dVars, oLine)
        else:
            if not dVars['bArchitectureIdentifierFound']:
                classify_architecture_identifier(sToken, iToken, lObjects, dVars, oLine)
            else:
                classify_architecture_of_keyword(sToken, iToken, lObjects, dVars, oLine)
                if not dVars['bArchitectureEntityNameFound']:
                    classify_architecture_entity_name(sToken, iToken, lObjects, dVars, oLine)
                else:
                    if not dVars['bArchitectureIsKeywordFound']:
                        classify_architecture_is_keyword(sToken, iToken, lObjects, dVars, oLine)
                    else:
                        if not dVars['bArchitectureBeginKeywordFound']:
                            classify_architecture_begin_keyword(sToken, iToken, lObjects, dVars, oLine)
                        else:
                            if not dVars['bArchitectureEndKeywordFound']:
                                classify_architecture_end(sToken, iToken, lObjects, dVars, oLine)
                            else:
                                classify_end_architecture_keyword(sToken, iToken, lObjects, dVars, oLine)
                                classify_architecture_semicolon(sToken, iToken, lObjects, dVars, oLine)
                                classify_architecture_simple_name(sToken, iToken, lObjects, dVars, oLine)


def classify_architecture_identifier(sToken, iToken, lObjects, dVars, oLine):
    if not isinstance(lObjects[iToken], parser.whitespace) and not isinstance(lObjects[iToken], parser.comment):
        lObjects[iToken] = parser.architecture_identifier(sToken)
        dVars['bArchitectureIdentifierFound'] = True


def classify_architecture_entity_name(sToken, iToken, lObjects, dVars, oLine):
    if sToken.lower() != 'of' and sToken.lower() != 'is' and not isinstance(lObjects[iToken], parser.whitespace) and not isinstance(lObjects[iToken], parser.comment):
        lObjects[iToken] = parser.architecture_entity_name(sToken)
        dVars['bArchitectureEntityNameFound'] = True


def classify_architecture_simple_name(sToken, iToken, lObjects, dVars, oLine):
    if sToken.lower() != 'architecture' and sToken != ';' and not isinstance(lObjects[iToken], parser.whitespace) and not isinstance(lObjects[iToken], parser.comment):
        lObjects[iToken] = parser.architecture_simple_name(sToken)


def classify_architecture_is_keyword(sToken, iToken, lObjects, dVars, oLine):
    if sToken.lower() == 'is':
        lObjects[iToken] = parser.architecture_is_keyword(sToken)
        dVars['bArchitectureIsKeywordFound'] = True


def classify_architecture_begin_keyword(sToken, iToken, lObjects, dVars, oLine):
    if sToken.lower() == 'begin':
        lObjects[iToken] = parser.architecture_begin_keyword(sToken)
        dVars['bArchitectureBeginKeywordFound'] = True


def classify_architecture_of_keyword(sToken, iToken, lObjects, dVars, oLine):
    if sToken.lower() == 'of':
        lObjects[iToken] = parser.architecture_of_keyword(sToken)


def classify_architecture_keyword(sToken, iToken, lObjects, dVars, oLine):
    if sToken.lower() == 'architecture':
        lObjects[iToken] = parser.architecture_keyword(sToken)
        dVars['bArchitectureKeywordFound'] = True 


def classify_end_architecture_keyword(sToken, iToken, lObjects, dVars, oLine):
    if sToken.lower() == 'architecture':
        lObjects[iToken] = parser.architecture_end_architecture_keyword(sToken)


def classify_architecture_end(sToken, iToken, lObjects, dVars, oLine):
    if sToken.lower() == 'end':
        lObjects[iToken] = parser.architecture_end_keyword(sToken)
        dVars['bArchitectureEndKeywordFound'] = True 


def classify_architecture_semicolon(sToken, iToken, lObjects, dVars, oLine):
    if sToken == ';':
        lObjects[iToken] = parser.architecture_semicolon(sToken)
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

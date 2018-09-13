import re


def block(self, dVars, oLine):

    classify_block_keyword(self, dVars, oLine)
    if oLine.insideBlock:
        classify_begin_keyword(dVars, oLine)
        classify_end_keyword(dVars, oLine)


def classify_block_keyword(self, dVars, oLine):
    if (re.match('^\s*block', oLine.lineNoComment) or re.match('^\s*\w+\s*:\s*block', oLine.lineNoComment)):
        oLine.isBlockKeyword = True
        oLine.insideBlock = True
        oLine.indentLevel = dVars['iCurrentIndentLevel']
        dVars['iCurrentIndentLevel'] += 1


def classify_begin_keyword(dVars, oLine):
        if re.match('^\s*begin', oLine.lineLower) and not oLine.insideFunction and \
           not oLine.insideProcess and not oLine.insideGenerate and \
           not oLine.insideProcedure:
            oLine.isBlockBegin = True
            oLine.indentLevel = dVars['iCurrentIndentLevel'] - 1


def classify_end_keyword(dVars, oLine):
    if not oLine.insideProcess and not oLine.insideCase and \
       not oLine.insideComponent and not oLine.insideGenerate and \
       not oLine.insideFunction and not oLine.insideForLoop and \
       not oLine.insideWhileLoop and not oLine.insideTypeRecord and \
       not oLine.insideProcedure:
        if re.match('^\s*end', oLine.lineLower):
            oLine.isEndBlock = True
            oLine.indentLevel = dVars['iCurrentIndentLevel'] - 1
            dVars['iCurrentIndentLevel'] -= 1

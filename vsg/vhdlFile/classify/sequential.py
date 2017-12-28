import re


def sequential(dVars, oLine):
    if not (oLine.insideProcess or oLine.insideProcedure):
        return

    if re.match('^.*<=', oLine.line) and not oLine.isComment and not oLine.insideIf and not oLine.isElseKeyword and not oLine.insideCaseWhen:
        oLine.isSequential = True
        oLine.insideSequential = True
        oLine.indentLevel = dVars['iCurrentIndentLevel']
        oLine.sequentialAlignmentColumn = oLine.line.find('<=')
    if oLine.insideSequential:
        if ';' in oLine.line:
            oLine.isSequentialEnd = True

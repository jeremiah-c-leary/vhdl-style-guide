import re


def variable_assignment(dVars, oLine):

    if not (oLine.insideProcess or oLine.insideFunction or oLine.insideProcedure):
        return

    if re.match('^\s*.*\s*:=', oLine.lineNoComment) and \
       not oLine.isComment and not oLine.insideIf and \
       not oLine.isElseKeyword and not oLine.isVariable and not oLine.isSignal:
        oLine.isVariableAssignment = True
        oLine.insideVariableAssignment = True
        oLine.indentLevel = dVars['iCurrentIndentLevel']
        oLine.variableAssignmentAlignmentColumn = oLine.lineNoComment.find(':=')
    if oLine.insideVariableAssignment:
        if ';' in oLine.lineNoComment:
            oLine.isVariableAssignmentEnd = True

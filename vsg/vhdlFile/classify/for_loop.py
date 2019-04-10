import re


def for_loop(dVars, oLine):
    '''
    [loop_label :] for {identifier} in {discrete_range} loop

    end loop [loop label];
    '''

    if re.match('^\s*for\s.*\sin\s.*\sloop', oLine.lineLower):
        oLine.isForLoopKeyword = True
        oLine.insideForLoop = True
        oLine.indentLevel = dVars['iCurrentIndentLevel']
        dVars['iCurrentIndentLevel'] += 1
    if re.match('^\s*\w+\s*:\s*for\s.*\sin\s.*\sloop', oLine.lineLower):
        oLine.isForLoopKeyword = True
        oLine.insideForLoop = True
        oLine.indentLevel = dVars['iCurrentIndentLevel']
        dVars['iCurrentIndentLevel'] += 1
        oLine.isForLoopLabel = True
    if re.match('^\s*end\s+loop', oLine.lineLower) and not oLine.insideWhileLoop:
        oLine.isForLoopEnd = True
        dVars['iCurrentIndentLevel'] -= 1
        oLine.indentLevel = dVars['iCurrentIndentLevel']

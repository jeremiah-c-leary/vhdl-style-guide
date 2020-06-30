import re


def signal(dVars, oLine):

    if (re.match('^\s*signal\s', oLine.lineLower) or re.match('^\s*signal$', oLine.lineLower)):
        if oLine.insideFunction and not oLine.insideProcedure:
            if not dVars['fFunctionBeginDetected'] and dVars['fFunctionReturnTypeDetected']:
                _assign_beginning_signal_values(oLine, dVars)
        elif oLine.insideProcedure and not oLine.insideFunction:
            if not dVars['fProcedureBeginDetected'] and dVars['fProcedureIsDetected']:
                _assign_beginning_signal_values(oLine, dVars)
        else:
            _assign_beginning_signal_values(oLine, dVars)
            


    if oLine.insideSignal:
        if re.match('.*;', oLine.lineNoComment):
            oLine.isEndSignal = True


def _assign_beginning_signal_values(oLine, dVars):
    oLine.isSignal = True
    oLine.indentLevel = dVars['iCurrentIndentLevel']
    oLine.insideSignal = True


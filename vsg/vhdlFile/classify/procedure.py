import re


def procedure(dVars, oLine):
    '''
    Classifies procedure statements.

    procedure identifier [ (parameter_interface_list) ] is
      [ subprogram_declarative_part ]
    begin
      { sequential_statement }
    end [procedure] [identifier]

    Sets the following line attributes:

      * insideProcedure
      * insideProcedureDeclarative
      * isProcedureParameter
      * isProcedureBegin
      * isProcedureKeyword
      * isProcedureEnd
      * isProcedureReturn
      * isProcedureIs

    Modifies the following variables:

      * iOpenParenthesis
      * iCurrentIndentLevel
      * fProcedureParameterEndDetected
      * fProcedureIsDetected
    '''
    _classify_procedure_keyword(dVars, oLine)
    if oLine.insideProcedure:
        dVars['iOpenParenthesis'] += oLine.lineNoComment.count('(')
        dVars['iCloseParenthesis'] += oLine.lineNoComment.count(')')
        _classify_procedure_parameters(dVars, oLine)
        _classify_procedure_parameter_end(dVars, oLine)
        if oLine.insidePackage:
            _classify_end_procedure_in_package(dVars, oLine)
        else:
            _classify_procedure_declarative_region(dVars, oLine)
            _classify_is_keyword(dVars, oLine)
            _classify_begin_keyword(dVars, oLine)
            _classify_end_procedure_in_package_body(dVars, oLine)


def _classify_procedure_keyword(dVars, oLine):
    if re.match('^\s*procedure\s', oLine.lineLower):
        oLine.isProcedureKeyword = True
        oLine.insideProcedure = True
        oLine.indentLevel = dVars['iCurrentIndentLevel']
        dVars['iCurrentIndentLevel'] += 1


def _classify_procedure_declarative_region(dVars, oLine):
    if dVars['fProcedureIsDetected'] and not dVars['fProcedureBeginDetected']:
        oLine.insideProcedureDeclarative = True
        oLine.indentLevel = dVars['iCurrentIndentLevel']


def _classify_procedure_parameters(dVars, oLine):
    if re.match('^.*\w+\s*:\s*\w+', oLine.line) and not dVars['fProcedureParameterEndDetected']:
        oLine.isProcedureParameter = True
        if not oLine.isProcedureKeyword:
            oLine.indentLevel = dVars['iCurrentIndentLevel']


def _classify_end_procedure_in_package(dVars, oLine):
    if ';' in oLine.line and dVars['iOpenParenthesis'] == dVars['iCloseParenthesis']:
        dVars['iOpenParenthesis'] = 0
        dVars['iCloseParenthesis'] = 0
        oLine.isProcedureEnd = True
        dVars['iCurrentIndentLevel'] -= 1
        dVars['fProcedureParameterEndDetected'] = False
        dVars['fProcedureIsDetected'] = False
        dVars['fProcedureBeginDetected'] = False


def _classify_procedure_parameter_end(dVars, oLine):
    if ')' in oLine.line and dVars['iOpenParenthesis'] == dVars['iCloseParenthesis']:
        dVars['iOpenParenthesis'] = 0
        dVars['iCloseParenthesis'] = 0
        oLine.isProcedureParameterEnd = True
        dVars['fProcedureParameterEndDetected'] = True


def _classify_begin_keyword(dVars, oLine):
    if re.match('^\s*begin', oLine.lineLower):
        oLine.isProcedureBegin = True
        oLine.indentLevel = dVars['iCurrentIndentLevel'] - 1
        oLine.insideProcedureDeclarative = False
        dVars['fProcedureBeginDetected'] = True


def _classify_is_keyword(dVars, oLine):
    if re.match('^.*[\s|)]is', oLine.lineLower) and dVars['fProcedureParameterEndDetected'] and not dVars['fProcedureIsDetected']:
        oLine.isProcedureIs = True
        dVars['fProcedureIsDetected'] = True
    if re.match('^\s*procedure\s+\w+\s+is', oLine.line, re.IGNORECASE):
        oLine.isProcedureIs = True
        dVars['fProcedureIsDetected'] = True


def _classify_end_procedure_in_package_body(dVars, oLine):
    if re.match('^\s*end', oLine.lineLower) and not oLine.isEndIfKeyword and \
       not oLine.isEndCaseKeyword and not oLine.isForLoopEnd and not oLine.isWhileLoopEnd:
        oLine.isProcedureEnd = True
        oLine.indentLevel = dVars['iCurrentIndentLevel'] - 1
        dVars['iCurrentIndentLevel'] -= 1
        dVars['iOpenParenthesis'] = 0
        dVars['iCloseParenthesis'] = 0
        dVars['fProcedureParameterEndDetected'] = False
        dVars['fProcedureIsDetected'] = False
        dVars['fProcedureBeginDetected'] = False

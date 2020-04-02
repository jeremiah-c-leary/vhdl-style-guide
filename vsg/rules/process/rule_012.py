
from vsg import rule
from vsg import utils


class rule_012(rule.rule):
    '''
    Process rule 012 checks for the existance of the "is" keyword.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'process', '012')
        self.solution = 'Add "is" keyword after the closing parenthesis.'
        self.phase = 1

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.isSensitivityListEnd and not oLine.isProcessIs:
            dViolation = utils.create_violation_dict(iLineNumber)
            self.add_violation(dViolation)

    def _fix_violations(self, oFile):
        for dViolation in self.violations:
            oLine = utils.get_violating_line(oFile, dViolation)
            iInsertIndex = oLine.line.rfind(')')
            oLine.update_line(oLine.line[:iInsertIndex + 1] + ' is ' + oLine.line[iInsertIndex + 1:])
            oLine.isProcessIs = True
            search_for_and_remove_extraneous_is(oFile, utils.get_violation_line_number(dViolation))


def search_for_and_remove_extraneous_is(oFile, iLineNumber):
    '''
    Looks for an is keyword that is not on the same line as the closing parenthesis and removes it.
    '''
    iIndex = iLineNumber
    while True:
        iIndex += 1
        oLine = oFile.lines[iIndex]
        if oLine.isProcessIs:
            utils.clear_keyword_from_line(oLine, 'is')
            oLine.isProcessIs = False
        if oLine.isProcessBegin:
            break

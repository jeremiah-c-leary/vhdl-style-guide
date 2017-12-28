
from vsg import rule
from vsg import fix


class rule_027(rule.rule):
    '''
    Process rule 027 checks for blank lines between the process declarative lines and the "begin" keyword.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'process', '027')
        self.solution = 'Ensure a single blank line between the last non-blank line and the "begin" keyword.'
        self.phase = 3

    def analyze(self, oFile):
        dVars = clear_variables()
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.insideProcess:
                skip_this_process(dVars, oFile, oLine, iLineNumber)
                if dVars['fSkipProcess']:
                    if oLine.isEndProcess:
                        dVars['fSkipProcess'] = False
                    continue  # pragma: no cover
                check_for_blanks(self, dVars, oLine, iLineNumber)
                if oLine.isSensitivityListEnd:
                    dVars['fCheckForBlanks'] = True

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations[::-1]:
            fix.insert_blank_line_above(self, oFile, iLineNumber)
            oFile.lines[iLineNumber].insideProcess = True


def clear_variables():
    dVars = {}
    dVars['fCheckForBlanks'] = False
    dVars['fSkipProcess'] = False
    dVars['iBlankCount'] = 0
    return dVars


def skip_this_process(dVars, oFile, oLine, iLineNumber):
    if oLine.isProcessBegin and oLine.isSensitivityListEnd:
        dVars['fSkipProcess'] = True
    if oLine.isSensitivityListEnd and oFile.lines[iLineNumber + 1].isProcessBegin:
        dVars['fSkipProcess'] = True


def check_for_blanks(self, dVars, oLine, iLineNumber):
    if dVars['fCheckForBlanks']:
        if oLine.isBlank:
            dVars['iBlankCount'] += 1
        if not oLine.isBlank and not oLine.isProcessBegin:
            dVars['iBlankCount'] = 0
        if oLine.isProcessBegin:
            if not dVars['iBlankCount'] == 1:
                self.add_violation(iLineNumber)
            dVars['fSkipProcess'] = True
            dVars['fCheckForBlanks'] = False
            dVars['iBlankCount'] = 0

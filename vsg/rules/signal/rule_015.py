
from vsg import rule
from vsg import utils
import re


class rule_015(rule.rule):
    '''
    Signal rule 015 checks for multiple signal names defined in a single signal declaration.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'signal', '015')
        self.solution = 'multiple signals defined in a single declaration'
        self.phase = 1
        self.consecutive = 2
        self.configuration.append('consecutive')

    def _pre_analyze(self):
        self.sFullLine = ''
        self.iFailureLine = None

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.isSignal:
            self.sFullLine = ''
            self.iFailureLine = iLineNumber
        if oLine.insideSignal:
            self.sFullLine += oLine.line
        if oLine.isEndSignal:
            match = re.match(r'.*?signal\s+(?P<signals>[^:\n]*):', self.sFullLine, flags=re.IGNORECASE)
            if match:
                sSignalList = match.group("signals")
                if sSignalList.count(',') > self.consecutive - 1:
                    dViolation = utils.create_violation_dict(self.iFailureLine)
                    dViolation['endLine'] = iLineNumber
                    dViolation['line'] = self.sFullLine
                    self.add_violation(dViolation)

    def _fix_violations(self, oFile):
        for dViolation in self.violations[::-1]:
            iLineNumber = utils.get_violation_linenumber(dViolation)
            utils.remove_lines(oFile, iLineNumber, dViolation['endLine'])
            iNumLines = dViolation['line'].count(',') + 1
            lSignals = _extract_signals(dViolation['line'])
            sAfterColon = _extract_after_colon(dViolation['line'])
            for i in range(0, iNumLines):
                utils.insert_line(oFile, i + iLineNumber)
                oLine = oFile.lines[i + iLineNumber]
                oLine.isSignal = True
                oLine.insideSignal = True
                oLine.isEndSignal = True
                oLine.isBlank = False
                oLine.update_line('  signal ' + lSignals[i] + ' : ' + sAfterColon)
                utils.update_comment_line_attributes(oLine)


def _extract_signals(sString):
    sString2 = sString.replace(',', ' ')
    sString3 = sString2.split(':')[0]
    lSignals = sString3.split()[1::]
    return lSignals


def _extract_after_colon(sString):
    return sString.split(':')[1].lstrip()

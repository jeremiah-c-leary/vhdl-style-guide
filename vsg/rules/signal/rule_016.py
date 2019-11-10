
from vsg import rule
from vsg import utils
from vsg import line


class rule_016(rule.rule):
    '''
    General rule 016 checks a signal declaration is on a single line.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'signal', '016')
        self.solution = 'ensure signal declaration is on a single line.'
        self.phase = 1

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
            if not oLine.isSignal:
                self.add_violation(self.iFailureLine)
                self.dFix['violations'][self.iFailureLine] = {}
                self.dFix['violations'][self.iFailureLine]['endLine'] = iLineNumber
                self.dFix['violations'][self.iFailureLine]['line'] = self.sFullLine

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations[::-1]:
            dViolation = self.dFix['violations'][iLineNumber]
            utils.remove_lines(oFile, iLineNumber, dViolation['endLine'])
            utils.insert_line(oFile,iLineNumber)
            oLine = oFile.lines[iLineNumber]
            oLine.isSignal = True
            oLine.insideSignal = True
            oLine.isEndSignal = True
            oLine.isBlank = False
            oLine.update_line(dViolation['line'])
            utils.update_comment_line_attributes(oLine)

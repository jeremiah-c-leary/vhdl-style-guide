
from vsg import rule
from vsg import utils


class rule_009(rule.rule):
    '''
    Function rule 009 checks for a function parameter on the same line as the **function** keyword without a **begin** keyword.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'function', '009')
        self.solution = 'Move function parameter to it\'s own line.'
        self.phase = 1

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.isFunctionParameter and oLine.isFunctionKeyword and 'return' not in oLine.line:
            self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations[::-1]:
            utils.copy_line(oFile, iLineNumber)
            oLine = oFile.lines[iLineNumber]
            oLine.update_line(oLine.line.split('(')[0] + '(')
            oLine.isFunctionParameter = False
            oLine = oFile.lines[iLineNumber + 1]
            oLine.update_line('  ' + oLine.line.split('(')[1])
            oLine.isFunctionKeyword = False
            oLine.indentLevel = oFile.lines[iLineNumber].indentLevel + 1

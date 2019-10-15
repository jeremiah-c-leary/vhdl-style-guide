
import re

from vsg import rule


class rule_014(rule.rule):
    '''
    Constant rule 014 checks the indent of multiline constants that are not arrays.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'constant'
        self.identifier = '014'
        self.solution = 'Align with := keyword on constant declaration line.'
        self.phase = 5

    def _pre_analyze(self):
        self.alignmentColumn = 0
        self.fKeywordFound = False

    def _analyze(self, oFile, oLine, iLineNumber):
        if not oLine.isConstantArray and oLine.insideConstant:
            if oLine.isConstant and ':=' in oLine.line:
                self.alignmentColumn = oLine.line.index(':=') + len(':= ')
                self.fKeywordFound = True
            elif not oLine.isConstant and self.fKeywordFound:
                sMatch = ' ' * self.alignmentColumn
                if not re.match('^' + sMatch + '\w', oLine.line):
                    self.add_violation(iLineNumber)
                    self.dFix['violations'][iLineNumber] = self.alignmentColumn
            if oLine.isConstantEnd:
                self.fKeywordFound = False

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            sLine = oFile.lines[iLineNumber].line
            sNewLine = ' ' * self.dFix['violations'][iLineNumber] + sLine.strip()
            oFile.lines[iLineNumber].update_line(sNewLine)

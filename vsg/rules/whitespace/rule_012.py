
from vsg import rule
from vsg import check
from vsg import fix
from vsg import line

import re


class rule_012(rule.rule):
    '''Whitespace rule 012 checks for alignment of identifiers.'''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'whitespace'
        self.identifier = '012'
        self.phase = 2
        self.solution = 'Align the first character of each identifier.'
        self.fixable = False

    def analyze(self, oFile):
        lGroup = []
        fGroupFound = False
        iStartGroupIndex = None
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isProcessKeyword and not fGroupFound:
                fGroupFound = True
                iStartGroupIndex = iLineNumber
            if fGroupFound:
                if oLine.isSignal or oLine.isConstant or oLine.isVariable or oLine.isFileKeyword:
                    lGroup.append(oLine)
                else:
                    lGroup.append(line.blank_line())
            if oLine.isProcessBegin and fGroupFound:
                fGroupFound = False
                check.identifier_alignment(self, iStartGroupIndex, lGroup)
                lGroup = []
                iStartGroupIndex = None
#
#    def _fix_violations(self, oFile):
#        for iLineNumber in self.violations:
#            oLine = oFile.lines[iLineNumber]
#            iCommentIndex = oLine.line.find('--')
#            if iCommentIndex == -1:
#                oLine.update_line(re.sub(r'(\w+)([+|\-|/|*])', r'\1 \2', oLine.line))
#                oLine.update_line(re.sub(r'\)([+|\-|/|*])', r') \1', oLine.line))
#                oLine.update_line(re.sub(r'([+|\-|/|*])(\w+)', r'\1 \2', oLine.line))
#                oLine.update_line(re.sub(r'([+|\-|/|*])\(', r'\1 (', oLine.line))
#            else:
#                sLine = oLine.line[:iCommentIndex]
#                sLine = re.sub(r'(\w+)([+|\-|/|*])', r'\1 \2', sLine)
#                sLine = re.sub(r'\)([+|\-|/|*])', r') \1', sLine)
#                sLine = re.sub(r'([+|\-|/|*])(\w+)', r'\1 \2', sLine)
#                sLine = re.sub(r'([+|\-|/|*])\(', r'\1 (', sLine)
#                sLine = sLine + oLine.line[iCommentIndex:]
#                oLine.update_line(sLine)

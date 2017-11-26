
from vsg.rules.constant import constant_rule

from vsg import line


class rule_009(constant_rule):
    '''
    Constant rule 009 checks the colons are in the same column for all constants.
    '''

    def __init__(self):
        constant_rule.__init__(self)
        self.identifier = '009'
        self.solution = 'Align colon with right most colon.'
        self.phase = 5

    def analyze(self, oFile):
        lGroup = []
        fGroupFound = False
        iStartGroupIndex = None
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isArchitectureKeyword and not fGroupFound:
                fGroupFound = True
                iStartGroupIndex = iLineNumber
            if oLine.isEndArchitecture:
                lGroup.append(oLine)
                fGroupFound = False
                self._check_keyword_alignment(iStartGroupIndex, ':', lGroup)
                lGroup = []
                iStartGroupIndex = None
            if fGroupFound:
                if oLine.isConstant:
                    lGroup.append(oLine)
                else:
                    lGroup.append(line.line('Removed line'))

    def _fix_violations(self, oFile):
        self._fix_keyword_alignment(oFile)

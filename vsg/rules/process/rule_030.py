
from vsg import rule

import re


class rule_030(rule.rule):
    '''
    Process rule 030 checks for single signal declarations on sensitivity list lines.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'process'
        self.identifier = '030'
        self.solution = 'Compact sensivity list to reduce the number of lines is uses.'
        self.phase = 1
        self.fixable = False

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.insideSensitivityList and not oLine.isSensitivityListEnd:
                if oLine.lineNoComment.count(',') == 1 and not re.match('^.*,\s*\S+', oLine.lineNoComment):
                    self.add_violation(iLineNumber)

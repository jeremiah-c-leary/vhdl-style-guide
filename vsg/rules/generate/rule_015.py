
from vsg import rule
from vsg import utils


class rule_015(rule.rule):
    '''Generate rule 015 checks for the generate label and generate keyword on the same line.'''

    def __init__(self):
        rule.rule.__init__(self, 'generate', '015')
        self.solution = 'Merge lines with generate label with generate keyword.'
        self.phase = 1
        self.fixable = False

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.isGenerateLabel and not oLine.isGenerateKeyword:
            dViolation = utils.create_violation_dict(iLineNumber)
            self.add_violation(dViolation)

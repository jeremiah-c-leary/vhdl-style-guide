
from vsg import rule
from vsg import check


class rule_020(rule.rule):
    '''
    Generic rule 020 checks generic names start with G_.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'generic'
        self.identifier = '020'
        self.solution = 'Prefix generic name with G_.'
        self.phase = 7
        self.disable = True

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.isGenericDeclaration and not oLine.isGenericKeyword:
            check.starts_with(self, oLine.line.split()[0], iLineNumber, 'G_')

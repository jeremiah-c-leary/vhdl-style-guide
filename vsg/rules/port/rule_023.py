
from vsg import rule
from vsg import utilities


class rule_023(rule.rule):
    '''
    Port rule 023 checks for the existance of port modes.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'port', '023')
        self.solution = 'Add port mode.'
        self.phase = 1
        self.fixable = False

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isPortDeclaration:
                sLine = oLine.line.split(':')[1]
                if '(' in sLine:
                    sLine = sLine.split('(')[0]
                if not utilities.is_port_mode(sLine.split()[0]):
                    self.add_violation(iLineNumber)

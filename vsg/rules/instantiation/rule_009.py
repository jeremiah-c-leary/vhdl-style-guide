
from vsg import rule
from vsg import fix
from vsg import check


class rule_009(rule.rule):
    '''
    Instantiation rule 009 checks the entity name is uppercase in the instantiation declaration line.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'instantiation'
        self.identifier = '009'
        self.solution = 'Change entity name to all uppercase.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isInstantiationDeclaration:
                sName = oLine.line.split(':')[1].lstrip().split()[0]
                check.is_uppercase(self, sName, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            sLine = oLine.line.split(':')[1].split()[0]
            fix.upper_case(self, oFile.lines[iLineNumber], sLine)

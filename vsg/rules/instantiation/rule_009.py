
from vsg.rules import case_rule


class rule_009(case_rule):
    '''
    Instantiation rule 009 checks the entity name has proper case in the instantiation declaration line.
    '''

    def __init__(self):
        case_rule.__init__(self, 'instantiation', '009', 'isInstantiationDeclaration')
        self.case = 'upper'
        self.solution = 'Change entity name to '

    def _extract(self, oLine):
        return [oLine.line.split(':')[1].lstrip().split()[0]]

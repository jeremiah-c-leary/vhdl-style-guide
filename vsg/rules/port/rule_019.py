
from vsg.rules import case_rule


class rule_019(case_rule):
    '''
    Port rule 019 checks the port direction has proper case.
    '''

    def __init__(self):
        case_rule.__init__(self, 'port', '019', 'isPortDeclaration')
        self.solution = 'Change port direction to .'

    def _extract(self, oLine):
        return [oLine.line.split(':')[1].split()[0]]

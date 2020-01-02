
from vsg.rules import case_rule


class rule_028(case_rule):
    '''
    Instantiation rule 028 checks the entity name is uppercase in direct instantiations.
    '''

    def __init__(self):
        case_rule.__init__(self, 'instantiation', '028', 'isDirectInstantiationDeclaration')
        self.case = 'upper'
        self.solution = 'Change entity name to '

    def _extract(self, oLine):
        return [oLine.line.replace('.', ' ').split()[-1]]

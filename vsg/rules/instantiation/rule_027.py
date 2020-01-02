
from vsg.rules import case_rule
from vsg import utils


class rule_027(case_rule):
    '''
    Instantiation rule 027 checks the **entity** keyword has proper case in direct instantiations.
    '''

    def __init__(self):
        case_rule.__init__(self, 'instantiation', '027', 'isDirectInstantiationDeclaration')
        self.solution = 'Change "entity" keyword to '

    def _extract(self, oLine):
        return utils.extract_words(oLine, ['entity'])

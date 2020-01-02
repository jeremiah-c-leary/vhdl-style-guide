
from vsg.rules import case_rule
from vsg import utils


class rule_031(case_rule):
    '''
    Instantiation rule 031 checks the "component" keyword has proper case if it is used.
    '''

    def __init__(self):
        case_rule.__init__(self, 'instantiation', '031', 'isInstantiationDeclaration')
        self.solution = 'Change "component" keyword to '
        self.disable = True

    def _extract(self, oLine):
        if not oLine.isDirectInstantiationDeclaration:
            return utils.extract_words(oLine, ['component'])
        else:
            return []

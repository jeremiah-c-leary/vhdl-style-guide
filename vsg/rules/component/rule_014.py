
from vsg.rules import case_rule
from vsg import utils


class rule_014(case_rule):
    '''
    Component rule 014 checks the is keyword has proper case.
    '''

    def __init__(self):
        case_rule.__init__(self, 'component', '014', 'isComponentEnd')
        self.solution = 'Change "component" keyword to '

    def _extract(self, oLine):
        return utils.extract_words(oLine, ['component'])

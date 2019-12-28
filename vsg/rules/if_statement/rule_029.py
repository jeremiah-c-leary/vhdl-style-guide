
from vsg.rules import case_rule
from vsg import utils


class rule_029(case_rule):
    '''
    If rule 029 checks the **then** keyword has proper case.
    '''

    def __init__(self):
        case_rule.__init__(self, 'if', '029', 'isThenKeyword')
        self.solution = 'Change "then" keyword to '

    def _extract(self, oLine):
        return utils.extract_words(oLine, ['then'])

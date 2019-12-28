
from vsg.rules import case_rule
from vsg import utils


class rule_010(case_rule):
    '''
    Generate rule 010 checks the generate keyword in the "end generate" has the proper case.
    '''

    def __init__(self):
        case_rule.__init__(self, 'generate', '010', 'isGenerateEnd')
        self.solution = 'Change "generate" to '

    def _extract(self, oLine):
        return utils.extract_words(oLine, ['generate'])


from vsg.rules import case_rule
from vsg import utils


class rule_017(case_rule):
    '''
    Entity rule 017 checks the end keyword has proper case.
    '''

    def __init__(self):
        case_rule.__init__(self, 'case', '017', 'isEndCaseKeyword', utils.extract_first_keyword)
        self.solution = 'Change end keyword to ' + self.case + 'case'

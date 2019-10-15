
from vsg.rules import case_rule
from vsg import utils


class rule_002(case_rule):
    '''
    File rule 002 checks the **file** keyword has proper case.
    '''

    def __init__(self):
        case_rule.__init__(self, 'file', '002', 'isFileKeyword')
        self.solution = 'Change "file" keyword to '

    def _extract(self, oLine):
        return utils.extract_class_name(oLine)

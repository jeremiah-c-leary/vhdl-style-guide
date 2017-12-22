
from vsg.rules import lower_case_rule


class rule_004(lower_case_rule):
    '''
    Package rule 004 checks the "package" keyword is lower case.
    '''

    def __init__(self):
        lower_case_rule.__init__(self, 'package', '004', 'isPackageKeyword', 'package')


from vsg.rules import lower_case_rule


class rule_027(lower_case_rule):
    '''
    If rule 001 checks the **else** keyword is lowercase.
    '''

    def __init__(self):
        lower_case_rule.__init__(self, 'if', '027', 'isElseKeyword', 'else')


from vsg.rules import lower_case_rule


class rule_026(lower_case_rule):
    '''
    If rule 001 checks the **elsif** keyword is lowercase.
    '''

    def __init__(self):
        lower_case_rule.__init__(self, 'if', '026', 'isElseIfKeyword', 'elsif')

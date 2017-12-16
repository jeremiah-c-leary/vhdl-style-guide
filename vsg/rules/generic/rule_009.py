
from vsg.rules import lower_case_rule


class rule_009(lower_case_rule):
    '''
    Generic rule 009 checks the "generic" keyword is lowercase.
    '''

    def __init__(self):
        lower_case_rule.__init__(self, 'generic', '009', 'isGenericKeyword', 'generic')
        self.solution = 'Lowercase "generic" keyword.'

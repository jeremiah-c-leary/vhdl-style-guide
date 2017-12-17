
from vsg.rules import single_space_after_rule


class rule_003(single_space_after_rule):
    '''
    Generic rule 003 checks spacing between "generic" keyword and the open parenthesis.
    '''

    def __init__(self):
        single_space_after_rule.__init__(self, 'generic', '003', 'isGenericKeyword', 'generic')
        self.solution = 'Change spacing between "generic" and "(" to one space.'


from vsg.rules import single_space_after_rule


class rule_003(single_space_after_rule):
    '''
    Type rule 003 checks the spaces after the "subtype" keyword.
    '''

    def __init__(self):
        single_space_after_rule.__init__(self, 'subtype', '003', 'isSubtypeKeyword', 'subtype')

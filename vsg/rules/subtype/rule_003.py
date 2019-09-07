
from vsg.rules import multiple_spaces_after_rule


class rule_003(multiple_spaces_after_rule):
    '''
    Type rule 003 checks the spaces after the "subtype" keyword.
    '''

    def __init__(self):
        multiple_spaces_after_rule.__init__(self, 'subtype', '003', 'isSubtypeKeyword', 'subtype')


from vsg.rules import indent_rule


class rule_002(indent_rule):
    '''
    Generic rule 002 checks indentation of the "generic" keyword.
    '''

    def __init__(self):
        indent_rule.__init__(self, 'generic', '002', 'isGenericKeyword')

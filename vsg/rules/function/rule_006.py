
from vsg.rules import line_above_rule


class rule_006(line_above_rule):
    '''
    Function rule 006 enforces a blank line above the "function" keyword.
    '''

    def __init__(self):
        line_above_rule.__init__(self, 'function', '006', 'isFunctionKeyword')

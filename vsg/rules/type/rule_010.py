
from vsg.rules import line_above_rule


class rule_010(line_above_rule):
    '''
    Type 010 checks for a blank line above the "type" declaration.
    '''

    def __init__(self):
        line_above_rule.__init__(self, 'type', '010', 'isTypeKeyword')

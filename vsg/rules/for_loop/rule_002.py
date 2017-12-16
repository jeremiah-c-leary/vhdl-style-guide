
from vsg.rules import indent_rule


class rule_002(indent_rule):
    '''
    For loop rule 002 checks for the proper indentation of the "end loop" keywords.
    '''

    def __init__(self):
        indent_rule.__init__(self, 'for_loop', '002', 'isForLoopEnd')

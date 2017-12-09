from vsg.rules import indent_rule


class rule_002(indent_rule):
    '''
    Checks the indent level of the "end loop" keywords.
    '''

    def __init__(self):
        indent_rule.__init__(self, 'while_loop', '002', 'isWhileLoopEnd')

from vsg.rules import indent_rule


class rule_001(indent_rule):
    '''
    Checks the indent level of the "while" keyword.
    '''

    def __init__(self):
        indent_rule.__init__(self, 'while_loop', '001', 'isWhileLoopKeyword')

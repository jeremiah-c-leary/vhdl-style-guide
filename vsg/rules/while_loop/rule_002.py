from vsg.rules import indent_rule


class rule_002(indent_rule):
    '''
    Checks the indent level of the "end loop" keywords.
    '''

    def __init__(self):
        indent_rule.__init__(self)
        # These are filled out when creating a new rule
        self.name = 'while_loop'
        self.identifier = '002'
        self.sTrigger = 'isWhileLoopEnd'

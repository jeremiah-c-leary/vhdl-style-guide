from vsg.rules import indent_rule


class rule_001(indent_rule):
    '''
    Checks the indent level of the "subtype" keyword.
    '''

    def __init__(self):
        indent_rule.__init__(self)
        # These are filled out when creating a new rule
        self.name = 'subtype'
        self.identifier = '001'
        self.sTrigger = 'isSubtypeKeyword'

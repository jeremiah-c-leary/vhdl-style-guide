
from vsg.rules import line_below_rule


class rule_019(line_below_rule):
    '''
    Instantiation rule 019 checks for a blank line below the end of the port
    declaration.
    '''

    def __init__(self):
        line_below_rule.__init__(self)
        self.name = 'instantiation'
        self.identifier = '019'
        self.condition = 'isInstantiationPortEnd'

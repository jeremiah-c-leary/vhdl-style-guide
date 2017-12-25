
from vsg.rules import indent_rule


class rule_001(indent_rule):
    '''
    File rule 001 checks the indent of file statements.
    '''

    def __init__(self):
        indent_rule.__init__(self, 'file', '001', 'insideFile')

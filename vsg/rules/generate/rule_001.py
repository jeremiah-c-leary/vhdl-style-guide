
from vsg.rules import indent_rule


class rule_001(indent_rule):
    '''
    Generate rule 001 checks the indent of the generate declaration.
    '''

    def __init__(self):
        indent_rule.__init__(self, 'generate', '001', 'isGenerateKeyword')

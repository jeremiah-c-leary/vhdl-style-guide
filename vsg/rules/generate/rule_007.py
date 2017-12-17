
from vsg.rules import indent_rule


class rule_007(indent_rule):
    '''
    Generate rule 007 checks the indent of the generate declaration.
    '''

    def __init__(self):
        indent_rule.__init__(self, 'generate', '007', 'isGenerateEnd')

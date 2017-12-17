
from vsg.rules import indent_rule


class rule_006(indent_rule):
    '''
    Generate rule 006 checks the indent of the generate declaration.
    '''

    def __init__(self):
        indent_rule.__init__(self, 'generate', '006', 'isGenerateBegin')

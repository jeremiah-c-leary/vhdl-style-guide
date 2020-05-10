
from vsg.rules import indent_rule


class rule_016(indent_rule):
    '''
    Generate rule 016 checks the indent of the when keywords in case generate statements.
    '''

    def __init__(self):
        indent_rule.__init__(self, 'generate', '016', 'isGenerateCaseWhen')

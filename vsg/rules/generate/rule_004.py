
from vsg.rules import line_above_rule


class rule_004(line_above_rule):
    '''
    Generate rule 004 checks for a blank line before the "generate" keyword.
    '''

    def __init__(self):
        line_above_rule.__init__(self, 'generate', '004', 'isGenerateKeyword')

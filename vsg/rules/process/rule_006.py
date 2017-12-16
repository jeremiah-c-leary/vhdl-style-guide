
from vsg.rules import indent_rule


class rule_006(indent_rule):
    '''
    Process rule 006 checks for the proper indentation at the beginning of the line.
    '''

    def __init__(self):
        indent_rule.__init__(self, 'process', '006', 'isEndProcess')

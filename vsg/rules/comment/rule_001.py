
from vsg.rules import indent_rule


class rule_001(indent_rule):
    '''
    Case rule 001 checks for the proper alignment of comments.
    '''

    def __init__(self):
        indent_rule.__init__(self, 'comment', '001', 'isComment')

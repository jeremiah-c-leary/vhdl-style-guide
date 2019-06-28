
from vsg.rules import indent_rule


class rule_010(indent_rule):
    '''
    Case rule 010 checks for the proper alignment of comments.
    '''

    def __init__(self):
        indent_rule.__init__(self, 'comment', '010', 'isComment')

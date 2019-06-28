
from vsg.rules import indent_rule


class rule_007(indent_rule):
    '''
    Case rule 007 checks for the proper alignment of comments.
    '''

    def __init__(self):
        indent_rule.__init__(self, 'comment', '007', 'isComment')


from vsg import parser
from vsg.rules import indent_item_rule


class rule_010(indent_item_rule):
    '''
    Case rule 010 checks for the proper indent of comments.
    '''

    def __init__(self):
        indent_item_rule.__init__(self, 'comment', '010', parser.comment)

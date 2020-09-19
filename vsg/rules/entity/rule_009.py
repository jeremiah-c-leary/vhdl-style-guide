
from vsg.rules import indent_item_rule

from vsg.token import entity_declaration as token


class rule_009(indent_item_rule):
    '''
    Checks for indent of the end keyword.
    '''
    def __init__(self):
        indent_item_rule.__init__(self, 'entity', '009', token.end_keyword)

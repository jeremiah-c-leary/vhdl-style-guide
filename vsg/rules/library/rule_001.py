
from vsg.rules import indent_item_rule

from vsg.token import library_clause as token


class rule_001(indent_item_rule):
    '''
    Checks for indent off the library keyword.
    '''
    def __init__(self):
        indent_item_rule.__init__(self, 'library', '001', token.keyword)

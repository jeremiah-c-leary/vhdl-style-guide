
from vsg.token import use_clause
from vsg.rules import indent_item_rule


class rule_008(indent_item_rule):
    '''
    Checks for indent of the use keyword.
    '''
    def __init__(self):
        indent_item_rule.__init__(self, 'library', '008', use_clause.keyword)


from vsg.token import entity
from vsg.rules import indent_item_rule


class rule_001(indent_item_rule):
    '''
    Checks for indent of the entity keyword.
    '''
    def __init__(self):
        indent_item_rule.__init__(self, 'entity', '001', entity.keyword)

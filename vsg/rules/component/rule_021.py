
from vsg.rules import insert_item_after_item_rule

from vsg.token import component_declaration as token


class rule_021(insert_item_after_item_rule):
    '''
    Component rule 005 checks the "is" keyword is used.
    '''

    def __init__(self):
        insert_item_after_item_rule.__init__(self, 'component', '021', token.identifier, token.end_keyword, token.is_keyword('is'))
        self.insert_space = True
        self.regionBegin = token.identifier
        self.regionEnd = token.end_keyword

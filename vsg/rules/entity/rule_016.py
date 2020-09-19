
from vsg.rules import remove_blank_lines_above_item_rule

from vsg.token import entity_declaration as token


class rule_016(remove_blank_lines_above_item_rule):
    '''
    Entity rule 016 checks for a blank line above the "end entity" keywords.
    '''

    def __init__(self):
        remove_blank_lines_above_item_rule.__init__(self, 'entity', '016', token.end_keyword, 0)
        self.regionBegin = token.end_keyword 
        self.regionEnd = token.end_keyword 

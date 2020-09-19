
from vsg.rules import space_between_items_rule

from vsg.token import library_clause as token
from vsg.token import logical_name_list


class rule_002(space_between_items_rule):
    '''
    Checks for a single space between the library keyword and the library logical name

    '''
    def __init__(self):
        space_between_items_rule.__init__(self, 'library', '002', token.keyword, logical_name_list.logical_name)
        self.regionBegin = token.keyword
        self.regionEnd = token.semicolon


from vsg.token import use_clause
from vsg.rules import space_between_items_rule


class rule_006(space_between_items_rule):
    '''
    Checks for a single space between the use keyword and the use selected_name

    '''
    def __init__(self):
        space_between_items_rule.__init__(self, 'library', '006', use_clause.keyword, use_clause.selected_name)
        self.regionBegin = use_clause.keyword
        self.regionEnd = use_clause.semicolon

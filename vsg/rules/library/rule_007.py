
from vsg.rules import remove_blank_lines_above_item_rule
from vsg.token import use_clause


class rule_007(remove_blank_lines_above_item_rule):
    '''
    Library rule 007 checks for a blank line above the "use" keyword.
    '''

    def __init__(self):
        remove_blank_lines_above_item_rule.__init__(self, 'library', '007', use_clause.keyword, 0)
        self.regionBegin = use_clause.keyword
        self.regionEnd = use_clause.semicolon

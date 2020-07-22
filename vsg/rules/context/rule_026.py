
from vsg import parser
from vsg.rules import remove_blank_lines_below_item_rule


class rule_026(remove_blank_lines_below_item_rule):
    '''
    Checks for a single space between the context keyword and the context identifier

    '''

    def __init__(self):
        remove_blank_lines_below_item_rule.__init__(self, 'context', '026', parser.context_is_keyword)

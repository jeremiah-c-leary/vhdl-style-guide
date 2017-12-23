
from vsg.rules import search_for_and_replace_keyword_rule


class rule_018(search_for_and_replace_keyword_rule):
    '''
    Port rule 018 checks the **generic** keyword is on the same line as the (.
    '''

    def __init__(self):
        search_for_and_replace_keyword_rule.__init__(self, 'generic', '018')
        self.solution = 'Move the ( to the same line as the "generic" keyword.'
        self.sKeyword = '('
        self.sTrigger = 'isGenericKeyword'
        self.sKeyword2 = 'generic'

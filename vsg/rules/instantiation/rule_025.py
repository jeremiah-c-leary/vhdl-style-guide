
from vsg.rules import search_for_and_replace_keyword_rule


class rule_025(search_for_and_replace_keyword_rule):
    '''
    Instantiation rule 025 checks the **map** keyword is on the same line as the (.
    '''

    def __init__(self):
        search_for_and_replace_keyword_rule.__init__(self, 'instantiation', '025')
        self.solution = 'Move the ( to the same line as the "generic map" keyword.'
        self.sKeyword = '('
        self.sTrigger = 'isInstantiationGenericKeyword'
        self.sKeyword2 = 'map'

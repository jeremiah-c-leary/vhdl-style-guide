
from vsg.rules import search_for_and_replace_keyword_rule


class rule_026(search_for_and_replace_keyword_rule):
    '''
    Instantiation rule 026 checks the **port map** keyword is on the same line as the (.
    '''

    def __init__(self):
        search_for_and_replace_keyword_rule.__init__(self, 'instantiation', '026')
        self.solution = 'Move the ( to the same line as the "port map" keyword.'
        self.sKeyword = '('
        self.sTrigger = 'isInstantiationPortKeyword'
        self.sKeyword2 = 'map'

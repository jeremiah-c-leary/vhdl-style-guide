
from vsg.rules import keyword_alignment_rule


class rule_012(keyword_alignment_rule):
    '''
    Function rule 012 checks the colons are in the same column for all declarations
    in the function declarative part.
    '''

    def __init__(self):
        keyword_alignment_rule.__init__(self, 'function', '012')
        self.sKeyword = ':'
        self.sStartGroupTrigger = 'isFunctionKeyword'
        self.sEndGroupTrigger = 'isFunctionBegin'
        self.lLineTriggers = ['isConstant', 'isVariable', 'insideFile']
        self.solution = 'Align colon with right most colon.'

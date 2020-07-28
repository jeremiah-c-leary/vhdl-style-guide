
from vsg.rules import identifier_alignment_rule


class rule_037(identifier_alignment_rule):
    '''
    Process rule 037 checks the alignment of declaration identifiers in the process declarative region.
    '''

    def __init__(self):
        identifier_alignment_rule.__init__(self, 'process', '037', 'isProcessKeyword', 'isProcessBegin')
        self.lUnless = ['insideProcedure', 'insideFunction']

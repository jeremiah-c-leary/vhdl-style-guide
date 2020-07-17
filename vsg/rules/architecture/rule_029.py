
from vsg.rules import identifier_alignment_rule


class rule_029(identifier_alignment_rule):
    '''
    Architecture rule 029 checks the alignment of declaration identifiers in the architecture declarative region.
    '''

    def __init__(self):
        identifier_alignment_rule.__init__(self, 'architecture', '029', 'isArchitectureKeyword', 'isArchitectureBegin')
        self.lUnless = ['insideFunction', 'insideProcedure']

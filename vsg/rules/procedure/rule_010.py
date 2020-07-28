
from vsg.rules import identifier_alignment_rule


class rule_010(identifier_alignment_rule):
    '''
    Process rule 010 checks the alignment of declaration identifiers in the procedure declarative region.
    '''

    def __init__(self):
        identifier_alignment_rule.__init__(self, 'procedure', '010', 'isProcedureIs', 'isProcedureBegin')

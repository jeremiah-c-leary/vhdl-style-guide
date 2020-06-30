
from vsg.rules import identifier_alignment_rule


class rule_015(identifier_alignment_rule):
    '''
    Process rule 015 checks the alignment of declaration identifiers in the function declarative region..
    '''

    def __init__(self):
        identifier_alignment_rule.__init__(self, 'function', '015', 'hasFunctionIs', 'isFunctionBegin')

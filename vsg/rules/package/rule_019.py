
from vsg.rules import identifier_alignment_rule


class rule_019(identifier_alignment_rule):
    '''
    Package rule 019 checks the alignment of declaration identifiers in the package declarative region.
    '''

    def __init__(self):
        identifier_alignment_rule.__init__(self, 'package', '019', 'isPackageKeyword', 'isPackageEnd')
        self.lUnless = ['insideProcedure', 'insideFunction']

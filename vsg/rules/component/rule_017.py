
from vsg.rules import keyword_alignment_rule


class rule_017(keyword_alignment_rule):
    '''
    Component rule 017 ensures the alignment of the : operator for every
    port in the component.
    '''

    def __init__(self):
        keyword_alignment_rule.__init__(self, 'component', '017')
        self.solution = 'Inconsistent alignment of ":" in port declaration of component.'
        self.sKeyword = ':'
        self.sStartGroupTrigger = 'isPortKeyword'
        self.sEndGroupTrigger = 'isEndPortMap'
        self.sLineTrigger = 'isPortDeclaration'


from vsg.rules import case_rule
from vsg import utils


class rule_017(case_rule):
    '''
    Generic rule 017 checks the generic type has proper case if it is a VHDL keyword.
    '''

    def __init__(self):
        case_rule.__init__(self, 'generic', '017', 'isGenericDeclaration')
        self.solution = 'Change generic name to '

    def _extract(self, oLine):
        return utils.extract_type_name_vhdl_only(oLine)

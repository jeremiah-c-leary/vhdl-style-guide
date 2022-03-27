

from vsg import parser
from vsg import token
from vsg import violation
from vsg.rule_group import case
from vsg.rules import case_utils
from vsg.rules import utils


class token_case_formal_part_of_association_element_in_map_between_tokens(case.Rule):
    '''
    Checks the case for words.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    trigger : parser object type
       object type to apply the case check against
    '''

    def __init__(self, name, identifier, sMapType, oStart, oEnd):
        case.Rule.__init__(self, name=name, identifier=identifier)
        self.solution = None
        self.phase = 6
        self.case = 'lower'
        self.configuration.append('case')
        self.prefix_exceptions = []
        self.suffix_exceptions = []
        self.case_exceptions = []
        if sMapType == 'port':
            self.oMapStart = token.port_map_aspect.open_parenthesis
            self.oMapEnd = token.port_map_aspect.close_parenthesis
        else:
            self.oMapStart = token.generic_map_aspect.open_parenthesis
            self.oMapEnd = token.generic_map_aspect.close_parenthesis
        self.oStart = oStart
        self.oEnd = oEnd

    def _get_tokens_of_interest(self, oFile):
        self.case_exceptions_lower = utils.lowercase_list(self.case_exceptions)
        return oFile.get_tokens_bounded_by(self.oStart, self.oEnd)

    def _analyze(self, lToi):
        check_prefix = case_utils.is_exception_enabled(self.prefix_exceptions)
        check_suffix = case_utils.is_exception_enabled(self.suffix_exceptions)
        check_whole = case_utils.is_exception_enabled(self.suffix_exceptions)
        for oToi in lToi:
            lTokens = oToi.get_tokens()

            bMapFound = False
            bFormalFound = False
            iLine = oToi.get_line_number()
            for iToken, oToken in enumerate(lTokens):
                if isinstance(oToken, self.oMapStart):
                    bMapFound = True
                    continue
                if isinstance(oToken, self.oMapEnd):
                    bMapFound = False
                    break
                if isinstance(oToken, parser.carriage_return):
                   iLine += 1
                if isinstance(oToken, token.association_element.formal_part) and not bFormalFound and bMapFound:
                    bFormalFound = True
                    oViolation = case_utils.check_for_case_violation(oToi, self, check_prefix, check_suffix, check_whole, iToken, iLine)
                    if oViolation is not None:
                        self.add_violation(oViolation)
                if isinstance(oToken, token.association_element.assignment):
                    bFormalFound = False

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        dAction = oViolation.get_action()
        lTokens[dAction['index']].set_value(dAction['value'])
        oViolation.set_tokens(lTokens)

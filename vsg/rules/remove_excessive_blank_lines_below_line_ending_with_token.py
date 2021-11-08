
from vsg import parser
from vsg import violation

from vsg.rule_group import blank_line
from vsg.vhdlFile import utils


class remove_excessive_blank_lines_below_line_ending_with_token(blank_line.Rule):
    '''
    Checks for excessive blank lines below a line ending with a given token

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    lTokens : token object type list
       token object that a blank line below should appear

    iAllow : integer
       Maximum number of blank lines

    lOverrides : token object type list
       Ignore lines with given token types
    '''

    def __init__(self, name, identifier, lTokens, iAllow=1, lOverrides=None):
        blank_line.Rule.__init__(self, name=name, identifier=identifier)
        self.solution = 'Remove blank lines below'
        self.lTokens = lTokens
        self.iAllow = iAllow
        if lOverrides == None:
            self.lOverrides = []
        else:
            self.lOverrides = lOverrides

    def analyze(self, oFile):
        lToi = oFile.get_blank_lines_below_line_ending_with_token(self.lTokens)
        for oToi in lToi:
            lTokens = oToi.get_tokens()
            iCount = 0
            iLine = oToi.get_line_number()
            for oToken in lTokens:
                if isinstance(oToken, parser.blank_line):
                    iCount += 1
                iLine = utils.increment_line_number(iLine, oToken)
            bOverride = check_if_override_exists(oFile, iLine, self.lOverrides)
            if bOverride:
                iCount -= 1
            if iCount > self.iAllow:
                oViolation = violation.New(oToi.get_line_number(), oToi, self.solution)
                dAction = {}
                dAction['remove'] = self.iAllow - iCount
                oViolation.set_action(dAction)
                self.add_violation(oViolation)

    def _fix_violation(self, oViolation):
            lTokens = oViolation.get_tokens()
            dAction = oViolation.get_action()
            lNewTokens = lTokens[0:2*dAction['remove']]
            oViolation.set_tokens(lNewTokens)


def check_if_override_exists(oFile, iLine, lOverrides):
    oMyToi = oFile.get_tokens_from_line(iLine + 1)
    try:
        lTokens = oMyToi.get_tokens()
        for oOverride in lOverrides:
            if utils.does_token_type_exist_in_list_of_tokens(oOverride, lTokens):
                return True
        return False
    except AttributeError:
        return False


from vsg import rule
from vsg import parser
from vsg import violation


class blank_line_above_line_starting_with_token(rule.Rule):
    '''
    Checks for a blank line above a line starting with a given token

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    token: token object type list
       token object that a blank line above should appear
    '''

    def __init__(self, name, identifier, lTokens, lAllowTokens=[]):
        rule.Rule.__init__(self, name=name, identifier=identifier)
        self.solution = 'Insert blank line above'
        self.phase = 3
        self.lTokens = lTokens
        self.lHierarchyLimits = None
        self.allow_comments = False
        self.blank_above_comment = False
        self.configuration.append('allow_comments')
        self.configuration.append('blank_above_comment')
        self.lAllowTokens = lAllowTokens

    def _get_tokens_of_interest(self, oFile):
        if self.lHierarchyLimits is None:
            return oFile.get_line_above_line_starting_with_token(self.lTokens, self.blank_above_comment)
        else:
            return oFile.get_line_above_line_starting_with_token_with_hierarchy(self.lTokens, self.lHierarchyLimits, self.blank_above_comment)

    def _set_allow_tokens(self):
        return

    def _analyze(self, lToi):
        self._set_allow_tokens()
        for oToi in lToi:
            lTokens = oToi.get_tokens()
            bSkip = False
            for oAllowToken in self.lAllowTokens:
                for oToken in lTokens:
                    if isinstance(oToken, oAllowToken):
                        bSkip = True
                        break
                if bSkip:
                   break
            if bSkip:
                continue
            if len(lTokens) == 1:
                if isinstance(lTokens[0], parser.blank_line):
                    continue
                if isinstance(lTokens[0], parser.comment) and self.allow_comments:
                    continue
            elif len(lTokens) == 2:
                if isinstance(lTokens[0], parser.whitespace) and isinstance(lTokens[1], parser.comment) and self.allow_comments:
                    continue
            oViolation = violation.New(oToi.get_line_number(), oToi, self.solution)
            self.add_violation(oViolation)

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        lTokens.append(parser.carriage_return())
        lTokens.append(parser.blank_line())
        oViolation.set_tokens(lTokens)

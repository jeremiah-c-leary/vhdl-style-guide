
from vsg import rule
from vsg import parser
from vsg import violation


class blank_line_below_line_ending_with_token(rule.Rule):
    '''
    Checks for a blank line below a line ending with a given token

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    token: token object type list
       token object that a blank line below should appear
    '''

    def __init__(self, name, identifier, lTokens, lAllowTokens=[]):
        rule.Rule.__init__(self, name=name, identifier=identifier)
        self.solution = 'Insert blank line below'
        self.phase = 3
        self.lTokens = lTokens
        self.lHierarchyLimits = None
        self.allow_comments = False
        self.configuration.append('allow_comments')
        self.lAllowTokens = lAllowTokens

    def _get_tokens_of_interest(self, oFile):
        if self.lHierarchyLimits is None:
            return oFile.get_line_below_line_ending_with_token(self.lTokens)
        else:
            return oFile.get_line_below_line_ending_with_token_with_hierarchy(self.lTokens, self.lHierarchyLimits)

    def _analyze(self, lToi):
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

            oViolation = violation.New(oToi.get_line_number() - 1, oToi, self.solution)
            self.add_violation(oViolation)

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        lTokens.insert(0, parser.carriage_return())
        lTokens.insert(0, parser.blank_line())
        oViolation.set_tokens(lTokens)

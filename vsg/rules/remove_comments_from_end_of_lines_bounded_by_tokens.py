
from vsg import parser
from vsg import rule
from vsg import violation


class remove_comments_from_end_of_lines_bounded_by_tokens(rule.Rule):
    '''
    Checks the case for words.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    lTokens : list of parser object types
       object types to check the prefix

    lPrefixes : string list
       acceptable prefixes
    '''

    def __init__(self, name, identifier, oStart, oEnd):
        rule.Rule.__init__(self, name=name, identifier=identifier)
        self.solution = None
        self.phase = 1
        self.oStart = oStart
        self.oEnd = oEnd

    def _get_tokens_of_interest(self, oFile):
        return oFile.get_tokens_bounded_by(self.oStart, self.oEnd)

    def _analyze(self, lToi):
        for oToi in lToi:
            lTokens = oToi.get_tokens()
            iLine = oToi.get_line_number()
            for iToken, oToken in enumerate(lTokens):
                if isinstance(oToken, parser.carriage_return):
                    iLine += 1
                if isinstance(oToken, parser.comment):
                    if isinstance(lTokens[iToken + 1], parser.carriage_return):
                        if isinstance(lTokens[iToken - 1], parser.carriage_return) or \
                           isinstance(lTokens[iToken - 2], parser.carriage_return):
                            continue
                        else:
                            if isinstance(lTokens[iToken - 1], parser.whitespace):
                                oNewToi = oToi.extract_tokens(iToken - 1, iToken)
                            else:
                                oNewToi = oToi.extract_tokens(iToken, iToken)
                            oViolation = violation.New(oNewToi.get_line_number(), oNewToi, self.solution)
                            self.add_violation(oViolation)

    def _fix_violation(self, oViolation):
        for oViolation in self.violations:
            oViolation.set_tokens([])

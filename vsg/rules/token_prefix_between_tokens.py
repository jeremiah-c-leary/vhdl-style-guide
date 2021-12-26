
from vsg import parser
from vsg import violation

from vsg.rules import utils as rules_utils
from vsg.rule_group import naming


class token_prefix_between_tokens(naming.Rule):
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

    def __init__(self, name, identifier, lTokens, oStart, oEnd):
        naming.Rule.__init__(self, name=name, identifier=identifier)
        self.lTokens = lTokens
        self.prefixes = None
        self.configuration.append('prefixes')
        self.fixable = False
        self.disable = True
        self.oStart = oStart
        self.oEnd = oEnd

    def _get_tokens_of_interest(self, oFile):
        return oFile.get_tokens_matching_in_range_bounded_by_tokens(self.lTokens, self.oStart, self.oEnd)

    def _analyze(self, lToi):
        lPrefixLower = []
        for sPrefix in self.prefixes:
            lPrefixLower.append(sPrefix.lower())
        for oToi in lToi:
            lTokens = oToi.get_tokens()
            sToken = lTokens[0].get_value().lower()
            bValid = False
            for sPrefix in lPrefixLower:
                if sToken.startswith(sPrefix):
                    bValid = True
            if not bValid:
                sSolution = 'Prefix ' + lTokens[0].get_value() + ' with one of the following: ' + ', '.join(self.prefixes)
                oViolation = violation.New(oToi.get_line_number(), oToi, sSolution)
                self.add_violation(oViolation)

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        if oViolation.get_action() == 'remove_whitespace':
            oViolation.set_tokens([lTokens[1]])
        elif oViolation.get_action() == 'adjust_whitespace':
            lTokens[0].set_value(lTokens[1].get_indent() * self.indentSize * ' ')
            oViolation.set_tokens(lTokens)
        elif oViolation.get_action() == 'add_whitespace':
            rules_utils.insert_whitespace(lTokens, 0, lTokens[0].get_indent() * self.indentSize)
            oViolation.set_tokens(lTokens)

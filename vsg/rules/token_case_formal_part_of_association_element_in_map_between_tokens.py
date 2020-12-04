

from vsg import parser
from vsg import rule
from vsg import token
from vsg import violation


class token_case_formal_part_of_association_element_in_map_between_tokens(rule.Rule):
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
        rule.Rule.__init__(self, name=name, identifier=identifier)
        self.solution = None
        self.phase = 6
        self.case = 'lower'
        self.configuration.append('case')
        if sMapType == 'port':
            self.oMapStart = token.port_map_aspect.open_parenthesis
            self.oMapEnd = token.port_map_aspect.close_parenthesis
        else:
            self.oMapStart = token.generic_map_aspect.open_parenthesis
            self.oMapEnd = token.generic_map_aspect.close_parenthesis
        self.oStart = oStart
        self.oEnd = oEnd

    def _get_tokens_of_interest(self, oFile):
        return oFile.get_tokens_bounded_by(self.oStart, self.oEnd)

    def _analyze(self, lToi):
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
                    sObjectValue = oToken.get_value()
                    if self.case == 'lower':
                        if not sObjectValue.islower():
                            sSolution = 'Change "' + sObjectValue + '" to "' + sObjectValue.lower() + '"'
                            self.add_violation(violation.New(iLine, oToi.extract_tokens(iToken, iToken), sSolution))
                    if self.case == 'upper':
                        if not sObjectValue.isupper():
                            sSolution = 'Change "' + sObjectValue + '" to "' + sObjectValue.upper() + '"'
                            self.add_violation(violation.New(iLine, oToi.extract_tokens(iToken, iToken), sSolution))
                if isinstance(oToken, token.association_element.assignment):
                    bFormalFound = False

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        if self.case == 'lower':
            lTokens[0].set_value(lTokens[0].get_value().lower())
        if self.case == 'upper':
            lTokens[0].set_value(lTokens[0].get_value().upper())
        oViolation.set_tokens(lTokens)

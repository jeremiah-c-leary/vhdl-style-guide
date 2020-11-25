

from vsg import parser
from vsg import rule
from vsg import token
from vsg import utils
from vsg import violation


class separate_multiple_signal_identifiers_into_individual_statements(rule.Rule):
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

    def __init__(self, name, identifier, lTokens, iAllow=2):
        rule.Rule.__init__(self, name=name, identifier=identifier)
        self.solution = 'Split signal declaration into individual declarations'
        self.phase = 1
        self.lTokens = lTokens
        self.consecutive = iAllow
        self.configuration.append('consecutive')

    def analyze(self, oFile):
        lToi = oFile.get_tokens_bounded_by(token.signal_declaration.signal_keyword, token.signal_declaration.semicolon)
        for oToi in lToi:
            lTokens = oToi.get_tokens()
            iIdentifiers = 0
            iStartIndex = 0
            iEndIndex = 0
            for iToken, oToken in enumerate(lTokens):
                if isinstance(oToken, token.signal_declaration.identifier):
                    iIdentifiers += 1
                    if iStartIndex == 0:
                        iStartIndex = iToken
                    iEndIndex = iToken
            if iIdentifiers > self.consecutive:
                oViolation = violation.New(oToi.get_line_number(), oToi, self.solution)
                dAction = {}
                dAction['start'] = iStartIndex
                dAction['end'] = iEndIndex
                dAction['number'] = iIdentifiers
                oViolation.set_action(dAction)
                self.add_violation(oViolation)


    def fix(self, oFile):
        '''
        Applies fixes for any rule violations.
        '''
        if self.fixable:
            self.analyze(oFile)
            self._print_debug_message('Fixing rule: ' + self.name + '_' + self.identifier)
            self._fix_violation(oFile)
            self.violations = []

    def _fix_violation(self, oFile):
        for oViolation in self.violations:
            lTokens = oViolation.get_tokens()
            dAction = oViolation.get_action()
            lPreTokens = lTokens[:dAction['start']]
            lPostTokens = []
            lTemp = lTokens[dAction['end'] + 1:]
            for iToken, oToken in enumerate(lTemp):
                if isinstance(oToken, parser.carriage_return):
                    continue
                lPostTokens.append(oToken)
            lTemp = lPostTokens
            lPostTokens = []
            for iToken, oToken in enumerate(lTemp):
                if iToken == 0:
                    if isinstance(oToken, parser.whitespace):
                        continue
                else:
                    if isinstance(oToken, parser.whitespace) and isinstance(lTemp[iToken - 1], parser.whitespace):
                        continue
                    else:
                        lPostTokens.append(oToken)


            lIdentifiers = lTokens[dAction['start']:dAction['end'] + 1]

            lNewTokens = []
            iIdentifiers = 0
            for oToken in lIdentifiers:
                if isinstance(oToken, token.signal_declaration.identifier):
                    iIdentifiers += 1
                    if iIdentifiers == dAction['number']:
                        lNewTokens.extend(lPreTokens + [oToken, parser.whitespace(' ')] + lPostTokens)
                    else:
                        lNewTokens.extend(lPreTokens + [oToken, parser.whitespace(' ')] + lPostTokens + [parser.carriage_return()])
            oViolation.set_tokens(lNewTokens)

        oFile.update(self.violations)




from vsg import rule
from vsg import parser
from vsg import violation

from vsg.vhdlFile import utils


class move_token_sequences_left_of_token(rule.Rule):
    '''
    Checks the case for words.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    lTokens : list of parser object types
       object type to split a line at
    '''

    def __init__(self, name, identifier, lSequences, oLeftToken):
        rule.Rule.__init__(self, name=name, identifier=identifier)
        self.solution = None
        self.phase = 1
        self.lSequences = lSequences
        self.oLeftToken = oLeftToken

    def analyze(self, oFile):
        lToi = []
        lPrevious = []
        for lSequence in self.lSequences:
            if not lSequence[0] in lPrevious:
                aToi = oFile.get_tokens_bounded_by(lSequence[0], self.oLeftToken)
                lToi = utils.combine_two_token_class_lists(lToi, aToi)
            lPrevious.append(lSequence[0])

        for oToi in lToi:
            lTokens = oToi.get_tokens()
            for iToken, oToken in enumerate(lTokens):
                for lSequence in self.lSequences:
                    bFound = False
                    if isinstance(oToken, lSequence[0]):
                        if utils.are_next_consecutive_token_types(lSequence, iToken, lTokens):
                            bFound = True
                            break
                        if utils.are_next_consecutive_token_types(lSequence[:-1], iToken, lTokens):
                            dAction = {}
                            dAction['num_tokens'] = len(lSequence) - 1
                        elif utils.are_next_consecutive_token_types(lSequence[:-2], iToken, lTokens):
                            dAction = {}
                            dAction['num_tokens'] = len(lSequence) - 2
                            
                if bFound:
                    break
            else:
                sSolution = self.solution
                oViolation = violation.New(oToi.get_line_number(), oToi, sSolution)
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
            lMoveTokens = lTokens[0:dAction['num_tokens']]
            lTokens = lTokens[dAction['num_tokens']:]
            lTokens = lTokens[:-1] + lMoveTokens + [parser.whitespace(' ')] + [lTokens[-1]]
            oViolation.set_tokens(lTokens)
               
        oFile.update(self.violations)


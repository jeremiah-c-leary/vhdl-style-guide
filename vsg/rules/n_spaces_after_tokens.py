

from vsg import parser
from vsg import rule
from vsg import violation

from vsg.vhdlFile import utils
from vsg.rules import utils as rule_utils


class n_spaces_after_tokens(rule.Rule):
    '''
    Checks for a single space between two tokens.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    lTokens : list of token type pairs
       The tokens to check for a single space between
    '''

    def __init__(self, name, identifier, iSpaces, lTokens, bNIsMinimum=False):
        rule.Rule.__init__(self, name=name, identifier=identifier)
        self.solution = None
        self.phase = 2
        self.iSpaces = iSpaces
        self.lTokens = lTokens
        self.bNIsMinimum = bNIsMinimum

    def _get_tokens_of_interest(self, oFile):
        lToi = []
        lToi = oFile.get_n_tokens_before_and_after_tokens(1, self.lTokens)
        return lToi

    def _analyze(self, lToi):
        for oToi in lToi:
            iLine, lTokens = utils.get_toi_parameters(oToi)
            dAction = {}

            oRight = lTokens[-1]
            if not isinstance(oRight, parser.carriage_return):
                if isinstance(oRight, parser.whitespace):
                    if self.bNIsMinimum:
                        if self.iSpaces > len(oRight.get_value()):
                            dAction['right'] = {}
                            dAction['right']['action'] = 'adjust'
                    elif self.iSpaces != len(oRight.get_value()):
                        dAction['right'] = {}
                        dAction['right']['action'] = 'adjust'
                else:
                    dAction['right'] = {}
                    dAction['right']['action'] = 'insert'

            if len(list(dAction.keys())) > 0:
                sSolution = create_solution_text(dAction, self.iSpaces, lTokens)
                oViolation = violation.New(iLine, oToi, sSolution)
                oViolation.set_action(dAction)
                self.add_violation(oViolation)

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        dAction = oViolation.get_action()
        lKeys = list(dAction.keys())
        for sKey in lKeys:
            if sKey == 'right':
                if dAction[sKey]['action'] == 'adjust':
                    lTokens[-1].set_value(' '*self.iSpaces)
                else:
                    rule_utils.insert_whitespace(lTokens, len(lTokens) -1)
        oViolation.set_tokens(lTokens)


def create_solution_text(dAction, iNumSpaces, lTokens):
    sReturn = ''
    for sKey in list(dAction.keys()):
        if sKey == 'right':
            if dAction[sKey]['action'] == 'adjust':
                sReturn += 'Remove all but one space after ' + lTokens[1].get_value()
            else:
                sReturn += 'Add ' + str(iNumSpaces) + ' space(s) after ' + lTokens[1].get_value()
    return sReturn

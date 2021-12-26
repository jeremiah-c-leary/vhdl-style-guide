

from vsg import parser
from vsg import violation

from vsg.vhdlFile import utils
from vsg.rule_group import whitespace
from vsg.rules import utils as rules_utils


class n_spaces_before_and_after_tokens(whitespace.Rule):
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
        whitespace.Rule.__init__(self, name=name, identifier=identifier)
        self.iSpaces = iSpaces
        self.lTokens = lTokens
        self.bNIsMinimum = bNIsMinimum

    def _get_tokens_of_interest(self, oFile):
        return oFile.get_n_tokens_before_and_after_tokens(2, self.lTokens)

    def _analyze(self, lToi):
        for oToi in lToi:
            iLine, lTokens = utils.get_toi_parameters(oToi)

            fStartLine = False
            if isinstance(lTokens[0], parser.carriage_return) and isinstance(lTokens[1], parser.whitespace):
                fStartLine = True

            myToi = oToi.extract_tokens(1, 3)

            iLine, lTokens = utils.get_toi_parameters(myToi)
            dAction = {}

            check_spaces_on_left_side(lTokens, fStartLine, self.bNIsMinimum, dAction, self.iSpaces)

            check_spaces_on_right_side(lTokens, self.bNIsMinimum, dAction, self.iSpaces)

            if len(list(dAction.keys())) > 0:
                sSolution = create_solution_text(dAction, self.iSpaces, lTokens)
                oViolation = violation.New(iLine, myToi, sSolution)
                oViolation.set_action(dAction)
                self.add_violation(oViolation)

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        dAction = oViolation.get_action()
        lKeys = list(dAction.keys())
        for sKey in lKeys:
            if sKey == 'left':
                if dAction[sKey]['action'] == 'adjust':
                    lTokens[0].set_value(' '*self.iSpaces)
                else:
                    rules_utils.insert_whitespace(lTokens, 1)
            if sKey == 'right':
                if dAction[sKey]['action'] == 'adjust':
                    lTokens[-1].set_value(' '*self.iSpaces)
                else:
                    rules_utils.insert_whitespace(lTokens, len(lTokens) - 1)
        oViolation.set_tokens(lTokens)


def create_solution_text(dAction, iNumSpaces, lTokens):
    sReturn = ''
    for sKey in list(dAction.keys()):
        if sKey == 'left':
            if dAction[sKey]['action'] == 'adjust':
                sReturn += 'Remove all but one space before ' + lTokens[1].get_value() + '. '
            else:
                sReturn += 'Add ' + str(iNumSpaces) + ' space(s) before ' + lTokens[1].get_value() + '. '
        if sKey == 'right':
            if dAction[sKey]['action'] == 'adjust':
                sReturn += 'Remove all but one space after ' + lTokens[1].get_value()
            else:
                sReturn += 'Add ' + str(iNumSpaces) + ' space(s) after ' + lTokens[1].get_value()
    return sReturn


def check_spaces_on_left_side(lTokens, fStartLine, bNIsMinimum, dAction, iSpaces):
    if not fStartLine:
        oLeft = lTokens[0]
        if not isinstance(oLeft, parser.carriage_return):
            if isinstance(oLeft, parser.whitespace):
                if bNIsMinimum:
                    if iSpaces > len(oLeft.get_value()):
                        dAction['left'] = {}
                        dAction['left']['action'] = 'adjust'
                elif iSpaces != len(oLeft.get_value()):
                    dAction['left'] = {}
                    dAction['left']['action'] = 'adjust'
            else:
                dAction['left'] = {}
                dAction['left']['action'] = 'insert'


def check_spaces_on_right_side(lTokens, bNIsMinimum, dAction, iSpaces):
    oRight = lTokens[-1]
    if not isinstance(oRight, parser.carriage_return):
        if isinstance(oRight, parser.whitespace):
            if bNIsMinimum:
                if iSpaces > len(oRight.get_value()):
                    dAction['right'] = {}
                    dAction['right']['action'] = 'adjust'
            elif iSpaces != len(oRight.get_value()):
                dAction['right'] = {}
                dAction['right']['action'] = 'adjust'
        else:
            dAction['right'] = {}
            dAction['right']['action'] = 'insert'

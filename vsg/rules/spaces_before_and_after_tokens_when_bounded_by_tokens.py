

from vsg import parser
from vsg import violation

from vsg.vhdlFile import utils
from vsg.rule_group import whitespace
from vsg.rules import utils as rules_utils


class spaces_before_and_after_tokens_when_bounded_by_tokens(whitespace.Rule):
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

    def __init__(self, name, identifier, lTokens, lBetween):
        whitespace.Rule.__init__(self, name=name, identifier=identifier)
        self.lTokens = lTokens
        self.spaces_before = 1
        self.configuration.append('spaces_before')
        self.spaces_after = 4
        self.configuration.append('spaces_after')
        self.lBetween= lBetween
        self.nTokens = 2

    def _get_tokens_of_interest(self, oFile):
        return oFile.get_n_tokens_before_and_after_tokens_bounded_by_tokens(self.nTokens, self.lTokens, self.lBetween)

    def _analyze(self, lToi):
        for oToi in lToi:
            iLine, lTokens = utils.get_toi_parameters(oToi)

            fStartLine = False
            if isinstance(lTokens[0], parser.carriage_return) and isinstance(lTokens[1], parser.whitespace):
                fStartLine = True
            if isinstance(lTokens[1], parser.carriage_return):
                fStartLine = True

            myToi = oToi.extract_tokens(1, 3)

            iLine, lTokens = utils.get_toi_parameters(myToi)
            dAction = {}

            check_spaces_on_left_side(lTokens, fStartLine, dAction, self.spaces_before)

            check_spaces_on_right_side(lTokens, dAction, self.spaces_after)

            if len(list(dAction.keys())) > 0:
                sSolution = create_solution_text(dAction, self.spaces_before, self.spaces_after, lTokens)
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
                    lTokens[1].set_value(' '*self.spaces_before)
                elif dAction[sKey]['action'] == 'remove':
                    lTokens.pop(0)
                else:
                    rules_utils.insert_whitespace(lTokens, self.spaces_before)
            if sKey == 'right':
                if dAction[sKey]['action'] == 'adjust':
                    lTokens[-1].set_value(' '*self.spaces_after)
                else:
                    rules_utils.insert_whitespace(lTokens, len(lTokens) - self.spaces_after)
        oViolation.set_tokens(lTokens)


def create_solution_text(dAction, iNumSpacesBefore, iNumSpacesAfter, lTokens):
    sReturn = ''
    for sKey in list(dAction.keys()):
        if sKey == 'left':
            if dAction[sKey]['action'] == 'adjust':
                sReturn += 'Remove all but ' + str(iNumSpacesBefore) + ' space(s) before ' + lTokens[1].get_value() + '. '
            elif dAction[sKey]['action'] == 'remove':
                sReturn += 'Remove all space(s) before ' + lTokens[1].get_value() + '. '
            else:
                sReturn += 'Add ' + str(iNumSpacesBefore) + ' space(s) before ' + lTokens[1].get_value() + '. '
        if sKey == 'right':
            if dAction[sKey]['action'] == 'adjust':
                sReturn += 'Remove all but ' + str(iNumSpacesAfter) + ' space(s) after ' + lTokens[1].get_value()
            else:
                sReturn += 'Add ' + str(iNumSpaces) + ' space(s) after ' + lTokens[1].get_value()
    return sReturn


def check_spaces_on_left_side(lTokens, fStartLine, dAction, iSpaces):
    if not fStartLine:
        oLeft = lTokens[0]
        if isinstance(oLeft, parser.whitespace) and iSpaces > 0:
            if iSpaces != len(oLeft.get_value()):
                dAction['left'] = {}
                dAction['left']['action'] = 'adjust'
        elif isinstance(oLeft, parser.whitespace) and iSpaces == 0:
            dAction['left'] = {}
            dAction['left']['action'] = 'remove'
        elif iSpaces > 0:
            dAction['left'] = {}
            dAction['left']['action'] = 'insert'


def check_spaces_on_right_side(lTokens, dAction, iSpaces):
    oRight = lTokens[-1]
    if isinstance(oRight, parser.whitespace):
        if iSpaces != len(oRight.get_value()):
            dAction['right'] = {}
            dAction['right']['action'] = 'adjust'
    else:
        dAction['right'] = {}
        dAction['right']['action'] = 'insert'

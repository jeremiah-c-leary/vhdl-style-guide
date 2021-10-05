
from vsg import parser
from vsg import rule
from vsg import violation


class rule_001(rule.Rule):
    '''
    This class removes whitespace before a given token.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    oToken : token object
       The token where spaces will be removed before.
    '''

    def __init__(self):

        rule.Rule.__init__(self, 'whitespace', '001')
        self.phase = 1
        self.subphase = 0
        self.solution = 'Remove trailing whitespace'

    def _get_tokens_of_interest(self, oFile):
        return oFile.get_n_tokens_before_token(2, [parser.carriage_return])

    def _analyze(self, lToi):
        for oToi in lToi:
            if whitespace_exists(oToi):
                create_violation(oToi, self)

    def _fix_violation(self, oViolation):
        dAction = oViolation.get_action()
        if need_to_remove_whitespace(dAction):
            remove_whitespace(oViolation)
        else:
            remove_whitespace_and_insert_blank_line(oViolation)


def create_violation(oToi, self):
    lTokens = oToi.get_tokens()
    oViolation = violation.New(oToi.get_line_number(), oToi, self.solution)
    dAction = define_action(lTokens)
    oViolation.set_action(dAction)
    self.add_violation(oViolation)


def whitespace_exists(oToi):
    lTokens = oToi.get_tokens()
    if isinstance(lTokens[1], parser.whitespace):
        return True
    return False


def define_action(lTokens):
    dAction = {}
    if isinstance(lTokens[0], parser.carriage_return):
        dAction['action'] = 'insert_blank_line'
    else:
        dAction['action'] = 'remove'
    return dAction


def need_to_remove_whitespace(dAction):
    if dAction['action'] == 'remove':
        return True
    return False


def remove_whitespace(oViolation):
    lTokens = oViolation.get_tokens()
    myTokens = []
    myTokens.append(lTokens[0])
    myTokens.append(lTokens[-1])
    oViolation.set_tokens(myTokens)


def remove_whitespace_and_insert_blank_line(oViolation):
    lTokens = oViolation.get_tokens()
    myTokens = []
    myTokens.append(lTokens[0])
    myTokens.append(parser.blank_line())
    myTokens.append(lTokens[-1])
    oViolation.set_tokens(myTokens)

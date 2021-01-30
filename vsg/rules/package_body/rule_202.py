
from vsg.rules import previous_line

from vsg import token

lTokens = []
lTokens.append(token.package_body.end_keyword)


class rule_202(previous_line):
    '''
    Checks for a blank line above the package keyword.
    '''

    def __init__(self):
        previous_line.__init__(self, 'package_body', '202', lTokens)

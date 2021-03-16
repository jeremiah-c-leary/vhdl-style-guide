
from vsg import token

from vsg.rules import single_space_between_token_pairs

lTokens = []
lTokens.append([token.package_declaration.end_keyword, token.package_declaration.end_package_keyword])
lTokens.append([token.package_declaration.end_package_keyword, token.package_declaration.end_package_simple_name])


class rule_009(single_space_between_token_pairs):
    '''
    Checks for a single space between the "end" and "package" keywords and package_simple_name.
    '''
    def __init__(self):
        single_space_between_token_pairs.__init__(self, 'package', '009', lTokens)
        self.solution = 'Single space between *end* and *package* keywords and package_simple_name.'

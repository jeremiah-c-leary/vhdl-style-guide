
from vsg.rules import token_suffix as Rule

from vsg import token

lTokens = []
lTokens.append(token.alias_declaration.alias_designator)


class rule_601(Rule):
    '''
    This rule checks for valid suffixes on alias designators.

    Default prefix is *\_a*.

    Refer to the section `Configuring Prefix and Suffix Rules <configuring.html#configuring-prefix-and-suffix-rules>`_ for information on changing the allowed prefixes.

    **Violation**

    .. code-block:: vhdl

       alias header is name;
       alias footer is name;

    **Fix**

    .. code-block:: vhdl

       alias header_a is name;
       alias footer_a is name;
    '''

    def __init__(self):
        Rule.__init__(self, 'alias_declaration', '601', lTokens)
        self.suffixes = ['_a']
        self.solution = 'Alias designators'

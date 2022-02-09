
from vsg.rules import previous_line as Rule

from vsg.token import case_statement_alternative as token


class rule_201(Rule):
    '''
    This rule checks for blank lines or comments above the **when** keyword.

    Refer to `Configuring Previous Line Rules <configuring.html#configuring-previous-line-rules>`_ for options.

    The default style is :code:`allow_comment`.

    **Violation**

    .. code-block:: vhdl

       case data is
         when 3 =>
         -- Comment
         when 4 =>

    **Fix**

    .. code-block:: vhdl

       case data is

         when 3 =>

         -- Comment
         when 4 =>
    '''

    def __init__(self):
        Rule.__init__(self, 'case', '201', [token.when_keyword])
        self.style = 'allow_comment'

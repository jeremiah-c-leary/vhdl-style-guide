
from vsg.rules import blank_line_below_line_ending_with_token

from vsg import token

lTokens = []
lTokens.append(token.subprogram_body.is_keyword)

lAllowTokens = []
lAllowTokens.append(token.subprogram_body.begin_keyword)


class rule_201(blank_line_below_line_ending_with_token):
    '''
    This rule checks for a blank line below the **is** keyword.
    
    This rule allows the **begin** keyword to occupy the blank line:
    
    .. code-block:: vhdl
    
       procedure average_samples is
       begin
    
    Refer to the section `Configuring Blank Lines <configuring.html#configuring-blank-lines>`_ for options regarding comments.
    
    **Violation**
    
    .. code-block:: vhdl
    
       procedure average_samples (
           constant a : in integer;
           signal d : out std_logic
       ) is
         constant width : integer := 32;
       begin
    
       procedure average_samples is
         constant width : integer := 32;
       begin
    
    **Fix**
    
    .. code-block:: vhdl
    
       procedure average_samples (
           constant a : in integer;
           signal d : out std_logic
       ) is
    
         constant width : integer := 32;
       begin
    
       procedure average_samples is
    
         constant width : integer := 32;
       begin
    '''

    def __init__(self):
        blank_line_below_line_ending_with_token.__init__(self, 'procedure', '201', lTokens, lAllowTokens)

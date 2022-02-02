
from vsg.rules import align_tokens_in_region_between_tokens_unless_between_tokens

from vsg import token

lAlign = []
lAlign.append(token.full_type_declaration.identifier)
lAlign.append(token.incomplete_type_declaration.identifier)
lAlign.append(token.file_declaration.identifier)
lAlign.append(token.signal_declaration.identifier)
lAlign.append(token.constant_declaration.identifier)
lAlign.append(token.subtype_declaration.identifier)
lAlign.append(token.variable_declaration.identifier)
lAlign.append(token.alias_declaration.alias_designator)

oStart = token.process_statement.process_keyword
oEnd = token.process_statement.begin_keyword

lUnless = []
lUnless.append([token.subprogram_body.is_keyword,token.subprogram_body.begin_keyword])


class rule_031(align_tokens_in_region_between_tokens_unless_between_tokens):
    '''
    This rule checks for alignment of identifiers in the process declarative region.

    **Violation**

    .. code-block:: vhdl

       proc_1 : process(all) is

        variable     var1 : boolean;
        constant  cons1 : integer;
        file            file1  : load_file_file open read_mode is load_file_name;

       begin

       end process proc_1;

    **Fix**

    .. code-block:: vhdl

       proc_1 : process(all) is

        variable var1 : boolean;
        constant cons1 : integer;
        file     file1  : load_file_file open read_mode is load_file_name;

       begin

       end process proc_1;
    '''

    def __init__(self):
        align_tokens_in_region_between_tokens_unless_between_tokens.__init__(self, 'process', '031', lAlign, oStart, oEnd, lUnless)
        self.solution = 'Align the first character of each identifier.'

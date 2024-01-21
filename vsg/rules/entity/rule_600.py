
from vsg import parser
from vsg import token

from vsg.rules import consistent_token_case as Rule

from vsg.rules import consistent_case_utils as cc_utils

lTokens = []
lTokens.append(token.interface_unknown_declaration.identifier)
lTokens.append(token.interface_constant_declaration.identifier)
lTokens.append(token.interface_variable_declaration.identifier)
lTokens.append(token.interface_signal_declaration.identifier)

lNames = []
lNames.append(parser.todo)
lNames.append(token.todo.name)


class rule_600(Rule):
    '''
    This rule checks for consistent capitalization of generic names in entity declarations.

    **Violation**

    .. code-block:: vhdl

       entity FIFO is
         generic (
           G_WIDTH : natural := 16
         );
         port (
           I_DATA : std_logic_vector(g_width - 1 downto 0);
           O_DATA : std_logic_vector(g_width - 1 downto 0)
         );
       end entity fifo;

    **Fix**

    .. code-block:: vhdl

       entity FIFO is
         generic (
           G_WIDTH : natural := 16
         );
         port (
           I_DATA : std_logic_vector(G_WIDTH - 1 downto 0);
           O_DATA : std_logic_vector(G_WIDTH - 1 downto 0)
         );
       end entity fifo;
    '''

    def __init__(self):
        Rule.__init__(self, 'entity', '600', lTokens, lNames)

    def _get_tokens_of_interest(self, oFile):

        lNameTokens = cc_utils.get_all_name_tokens(oFile, self.lNames)
#        print(f'lNames = {lNameTokens}')
#        for iName in lNameTokens:
#            print(f'{iName} = {oFile.lAllObjects[iName].get_value()}')

        lIdentifierss = cc_utils.get_all_identifiers(oFile, self.lTokens)
#        print(f'lIdentifiers = {lIdentifierss}')
#        for iName in lIdentifierss:
#            print(f'{iName} = {oFile.lAllObjects[iName].get_value()}')

        lEntityDicts = cc_utils.get_entity_declaration_indexes(oFile)
        lGenericDicts = cc_utils.get_generic_clause_indexes(oFile)
        lPortDicts = cc_utils.get_port_clause_indexes(oFile)

        lAllDicts = cc_utils.merge_dict_lists(lEntityDicts, lGenericDicts)
        lAllDicts = cc_utils.merge_dict_lists(lAllDicts, lPortDicts)

        lAllDicts = cc_utils.populate_identifiers(lAllDicts, lIdentifierss)
        lAllDicts = cc_utils.remove_duplicate_identifiers('entity_declaration', 'port_clause', lAllDicts)

        lAllDicts = cc_utils.populate_declarative_part_names(lAllDicts, lNameTokens)
        lAllDicts = cc_utils.remove_duplicate_names('entity_declaration', 'generic_clause', lAllDicts)

        lAllDicts = cc_utils.remove_type('generic_clause', lAllDicts)
        lAllDicts = cc_utils.remove_type('port_clause', lAllDicts)

#        print('#'*80)
#        for tmp in lAllDicts:
#            print(tmp)

        return cc_utils.create_tois(lAllDicts, oFile)

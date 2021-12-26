
from vsg.rules import insert_token_right_of_token_if_it_does_not_exist

from vsg.token import component_declaration as token


class rule_021(insert_token_right_of_token_if_it_does_not_exist):
    '''
    This rule inserts the optional **is** keyword if it does not exist.

    Refer to the section `Configuring Optional Items <configuring.html#configuring-optional-items>`_ for options.

    **Violation**

    .. code-block:: vhdl

       component my_component

       end my_component;

    **Fix**

    .. code-block:: vhdl

       component my_component is

       end my_component;
    '''
    def __init__(self):
        insert_token_right_of_token_if_it_does_not_exist.__init__(self, 'component', '021', token.is_keyword('is'), token.identifier)
        self.solution = '*is* keyword.'
        self.groups.append('structure::optional')

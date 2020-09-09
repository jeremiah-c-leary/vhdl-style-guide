

from vsg.vhdlFile.classify_new import package_declaration
from vsg.vhdlFile.classify_new import package_body
from vsg.vhdlFile.classify_new import package_instantiation_declaration

from vsg.vhdlFile.classify_new import type_declaration
from vsg.vhdlFile.classify_new import subtype_declaration
from vsg.vhdlFile.classify_new import constant_declaration
from vsg.vhdlFile.classify_new import signal_declaration
from vsg.vhdlFile.classify_new import variable_declaration

from vsg.vhdlFile.classify_new import use_clause

'''
    block_declarative_item ::=
        subprogram_declaration
      | subprogram_body
      | subprogram_instantiation_declaration
      | package_declaration
      | package_body
      | package_instantiation_declaration
      | type_declaration
      | subtype_declaration
      | constant_declaration
      | signal_declaration
      | shared_variable_declaration
      | file_declaration
      | alias_declaration
      | component_declaration
      | attribute_declaration
      | attribute_specification
      | configuration_specification
      | disconnection_specification
      | use_clause
      | group_template_declaration
      | group_declaration
      | PSL_Property_Declaration
      | PSL_Sequence_Declaration
      | PSL_Clock_Declaration
'''


def detect(iToken, lObjects):

    iReturn = package_declaration.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    iReturn = package_body.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    iReturn = package_instantiation_declaration.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    iReturn = type_declaration.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    iReturn = subtype_declaration.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    iReturn = constant_declaration.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    iReturn = signal_declaration.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    iReturn = variable_declaration.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn



    iReturn = use_clause.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn


    return iToken

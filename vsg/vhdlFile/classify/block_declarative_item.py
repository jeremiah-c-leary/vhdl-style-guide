
from vsg.vhdlFile.classify import alias_declaration
from vsg.vhdlFile.classify import attribute_declaration
from vsg.vhdlFile.classify import attribute_specification
from vsg.vhdlFile.classify import component_declaration
from vsg.vhdlFile.classify import configuration_specification
from vsg.vhdlFile.classify import constant_declaration
from vsg.vhdlFile.classify import file_declaration
from vsg.vhdlFile.classify import package_body
from vsg.vhdlFile.classify import package_declaration
from vsg.vhdlFile.classify import package_instantiation_declaration
from vsg.vhdlFile.classify import subprogram_body
from vsg.vhdlFile.classify import subprogram_declaration
from vsg.vhdlFile.classify import subprogram_instantiation_declaration
from vsg.vhdlFile.classify import subtype_declaration
from vsg.vhdlFile.classify import signal_declaration
from vsg.vhdlFile.classify import type_declaration
from vsg.vhdlFile.classify import use_clause
from vsg.vhdlFile.classify import variable_declaration


def detect(iToken, lObjects):
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
      | *shared*_variable_declaration
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

    iReturn = subprogram_declaration.detect(iToken, lObjects)
    if iReturn != iToken:
        iReturn = subprogram_body.detect(iReturn, lObjects)
        return iReturn

    iReturn = subprogram_instantiation_declaration.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

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

    iReturn = file_declaration.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    iReturn = alias_declaration.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    iReturn = component_declaration.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    iReturn = attribute_declaration.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    iReturn = attribute_specification.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    iReturn = use_clause.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    iReturn = configuration_specification.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    return iToken

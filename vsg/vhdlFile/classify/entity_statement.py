# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.vhdlFile.classify import (
    concurrent_assertion_statement,
    concurrent_procedure_call_statement,
    process_statement,
)


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    entity_statement ::=
        concurrent_assertion_statement
      | *passive*_concurrent_procedure_call_statement
      | *passive*_process_statement
      | *PSL*_PSL_Directive
    """

    if process_statement.detect(oDataStructure):
        return True

    if concurrent_assertion_statement.detect(oDataStructure):
        return True

    if concurrent_procedure_call_statement.detect(oDataStructure):
        return True

    return False

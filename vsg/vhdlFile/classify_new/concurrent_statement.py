
from vsg.vhdlFile.classify_new import block_statement
#from vsg.vhdlFile.classify import concurrent_procedure_call_statement
#from vsg.vhdlFile.classify import process_statement
from vsg.vhdlFile.classify_new import generate_statement
from vsg.vhdlFile.classify_new import concurrent_signal_assignment_statement
#from vsg.vhdlFile.classify import concurrent_assertion_statement


def is_it(iObject, oObject, lAllObjects, lNewObjects, dVars):
    '''
    concurrent_statement ::=
        block_statement
      | process_statement
      | concurrent_procedure_call_statement
      | concurrent_assertion_statement
      | concurrent_signal_assignment_statement
      | component_instantiation_statement
      | generate_statement
      | *PSL*_PSL_Directive
    '''
#    print('--> concurrent_statement.is_it')
    if block_statement.is_it(iObject, oObject, lAllObjects, lNewObjects, dVars):
        return True
    
    if generate_statement.is_it(iObject, oObject, lAllObjects, lNewObjects, dVars):
        return True

    if concurrent_signal_assignment_statement.detected(iObject, oObject, lAllObjects, lNewObjects, dVars):
        return True

    return False


#def tokenize(oObject, iObject, lObjects, dVars):
#    '''
#    concurrent_statement ::=
#        block_statement
#      | process_statement
#      | concurrent_procedure_call_statement
#      | concurrent_assertion_statement
#      | concurrent_signal_assignment_statement
#      | component_instantiation_statement
#      | generate_statement
#      | *PSL*_PSL_Directive
#    '''
#    if not dVars['process_statement']['keyword']:
#
#        if block_statement.tokenize(oObject, iObject, lObjects, dVars):
#            return True
#
#        if generate_statement.tokenize(oObject, iObject, lObjects, dVars):
#            return True
#
#    if not dVars['block_statement']['end']:
#
#
#        if not dVars['process_statement']['keyword']:
#
#            if concurrent_assertion_statement.tokenize(oObject, iObject, lObjects, dVars):
#                return True
#    
#        if process_statement.tokenize(oObject, iObject, lObjects, dVars):
#            return True
#    
#        if not dVars['process_statement']['keyword']:
#            if not dVars['concurrent_procedure_call_statement']:
#                if concurrent_signal_assignment_statement.tokenize(oObject, iObject, lObjects, dVars):
#                    return True
#    
#            if concurrent_procedure_call_statement.tokenize(oObject, iObject, lObjects, dVars):
#                return True
#
#    dVars['caller'] = ''
#
#    return False
#
#
#def clear_flags(dVars):
#    block_statement.clear_flags(dVars)
#    concurrent_signal_assignment_statement.clear_flags(dVars)
#    concurrent_assertion_statement.clear_flags(dVars)
#    concurrent_procedure_call_statement.clear_flags(dVars)
#    process_statement.clear_flags(dVars)

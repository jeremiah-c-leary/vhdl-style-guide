
from vsg.vhdlFile.classify import assertion_statement

def tokenize(oObject, iObject, lObjects, dVars):
    '''
    sequential_statement ::=
        wait_statement
      | assertion_statement
      | report_statement
      | signal_assignment_statement
      | variable_assignment_statement
      | procedure_call_statement
      | if_statement
      | case_statement
      | loop_statement
      | next_statement
      | exit_statement
      | return_statement
      | null_statement
    '''
    if assertion_statement.tokenize(oObject, iObject, lObjects, dVars):
        return True

    return False


def clear_flags(dVars):
    assertion_statement.clear_flags(dVars)

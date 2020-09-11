
from vsg.vhdlFile.classify_new import null_statement

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


def detect(iToken, lObjects):

    iReturn = null_statement.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    return iToken

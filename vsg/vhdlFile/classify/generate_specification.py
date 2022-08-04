
from vsg.vhdlFile.classify import expression


def classify(iToken, lObjects):
    '''
    generate_specification ::=
        static_discrete_range
      | static_expression
      | alternative_label
    '''

    return expression.classify_until([')'], iToken, lObjects)

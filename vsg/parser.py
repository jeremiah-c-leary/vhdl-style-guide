
###############################################################################
# Base object
###############################################################################


class item():

    def __init__(self, sString):
        self.value = sString

    def get_value(self):
        return self.value

    def set_value(self, sString):
        self.value = sString

    def length(self):
        return len(self.value)

###############################################################################
# Base VHDL type classes
###############################################################################


class none(item):

    def __init__(self):
        item.__init__(self, None)


class keyword(item):

    def __init__(self, sString):
        item.__init__(self, sString)


class identifier(item):

    def __init__(self, sString):
        item.__init__(self, sString)


class colon(item):

    def __init__(self):
        item.__init__(self, ':')


class comma(item):

    def __init__(self):
        item.__init__(self, ',')


class semicolon(item):

    def __init__(self):
        item.__init__(self, ';')


class whitespace(item):

    def __init__(self, sString):
        item.__init__(self, sString)


class comment(item):

    def __init__(self, sString):
        item.__init__(self, sString)


class logical_name(item):

    def __init__(self, sString):
        item.__init__(self, sString)


class selected_name(item):

    def __init__(self, sString):
        item.__init__(self, sString)


class name(item):

    def __init__(self, sString):
        item.__init__(self, sString)


class simple_name(item):

    def __init__(self, sString):
        item.__init__(self, sString)


class subtype_indication(item):

    def __init__(self, sString):
        item.__init__(self, sString)


class condition(item):

    def __init__(self, sString):
        item.__init__(self, sString)


class expression(item):

    def __init__(self, sString):
        item.__init__(self, sString)


class static_expression(expression):

    def __init__(self, sString):
        expression.__init__(self, sString)


class label(item):

    def __init__(self, sString):
        item.__init__(self, sString)


class label_colon(colon):

    def __init__(self):
        colon.__init__(self)


class open_parenthesis(item):

    def __init__(self):
        item.__init__(self, '(')


class close_parenthesis(item):

    def __init__(self):
        item.__init__(self, ')')


class character_literal(item):

    def __init__(self, sString):
        item.__init__(self, sString)


class string_literal(item):

    def __init__(self, sString):
        item.__init__(self, sString)


class operator_symbol(string_literal):

    def __init__(self, sString):
        string_literal.__init__(self, sString)


class signature(item):

    def __init__(self, sString):
        item.__init__(self, sString)


class type_mark(item):

    def __init__(self, sString):
        item.__init__(self, sString)


class subtype_definition(item):

    def __init__(self, sString):
        item.__init__(self, sString)

###############################################################################
# Context objects
###############################################################################


class context_keyword(keyword):

    def __init__(self, sString):
        keyword.__init__(self, sString)


class context_identifier(identifier):

    def __init__(self, sString):
        identifier.__init__(self, sString)


class context_is_keyword(keyword):

    def __init__(self, sString):
        keyword.__init__(self, sString)


class context_end_keyword(keyword):

    def __init__(self, sString):
        keyword.__init__(self, sString)


class context_end_context_keyword(keyword):

    def __init__(self, sString):
        keyword.__init__(self, sString)


class context_end_identifier(identifier):

    def __init__(self, sString):
        identifier.__init__(self, sString)


class context_semicolon(semicolon):

    def __init__(self):
        semicolon.__init__(self)

###############################################################################
# Context reference objects
###############################################################################


class context_reference_keyword(keyword):

    def __init__(self, sString):
        keyword.__init__(self, sString)


class context_reference_identifier(identifier):

    def __init__(self, sString):
        identifier.__init__(self, sString)


class context_reference_comma(comma):

    def __init__(self):
        comma.__init__(self)


class context_reference_semicolon(semicolon):

    def __init__(self):
        semicolon.__init__(self)


###############################################################################
# Library objects
###############################################################################


class library_keyword(keyword):

    def __init__(self, sString):
        keyword.__init__(self, sString)

class library_logical_name(logical_name):

    def __init__(self, sString):
        logical_name.__init__(self, sString)

class library_comma(comma):

    def __init__(self):
        comma.__init__(self)

class library_semicolon(semicolon):

    def __init__(self):
        semicolon.__init__(self)

###############################################################################
# Assert objects
###############################################################################

class assert_label(label):

    def __init__(self, sString):
        label.__init__(self, sString)


class assert_label_colon(label_colon):

    def __init__(self):
        label_colon.__init__(self)


class assert_keyword(keyword):

    def __init__(self, sString):
        keyword.__init__(self, sString)


class assert_condition(condition):

    def __init__(self, sString):
        condition.__init__(self, sString)


class assert_report_keyword(keyword):

    def __init__(self, sString):
        keyword.__init__(self, sString)


class assert_report_expression(expression):

    def __init__(self, sString):
        expression.__init__(self, sString)


class assert_severity_keyword(keyword):

    def __init__(self, sString):
        keyword.__init__(self, sString)


class assert_severity_expression(expression):

    def __init__(self, sString):
        expression.__init__(self, sString)


class assert_semicolon(semicolon):

    def __init__(self):
        semicolon.__init__(self)



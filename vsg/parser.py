
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

###############################################################################
# Architecture objects
###############################################################################

class architecture_keyword(keyword):

    def __init__(self, sString):
        keyword.__init__(self, sString)

class architecture_identifier(identifier):

    def __init__(self, sString):
        identifier.__init__(self, sString)

class architecture_of_keyword(keyword):

    def __init__(self, sString):
        keyword.__init__(self, sString)

class architecture_entity_name(name):

    def __init__(self, sString):
        name.__init__(self, sString)

class architecture_is_keyword(keyword):

    def __init__(self, sString):
        keyword.__init__(self, sString)

class architecture_begin_keyword(keyword):

    def __init__(self, sString):
        keyword.__init__(self, sString)

class architecture_end_keyword(keyword):

    def __init__(self, sString):
        keyword.__init__(self, sString)

class architecture_end_architecture_keyword(keyword):

    def __init__(self, sString):
        keyword.__init__(self, sString)

class architecture_simple_name(simple_name):

    def __init__(self, sString):
        simple_name.__init__(self, sString)

class architecture_semicolon(semicolon):

    def __init__(self, sString):
        semicolon.__init__(self)

###############################################################################
# Entity objects
###############################################################################

class entity_keyword(keyword):

    def __init__(self, sString):
        keyword.__init__(self, sString)

class entity_identifier(identifier):

    def __init__(self, sString):
        identifier.__init__(self, sString)

class entity_is_keyword(keyword):

    def __init__(self, sString):
        keyword.__init__(self, sString)

class entity_begin_keyword(keyword):

    def __init__(self, sString):
        keyword.__init__(self, sString)

class entity_end_keyword(keyword):

    def __init__(self, sString):
        keyword.__init__(self, sString)

class entity_end_entity_keyword(keyword):

    def __init__(self, sString):
        keyword.__init__(self, sString)

class entity_simple_name(simple_name):

    def __init__(self, sString):
        simple_name.__init__(self, sString)

class entity_semicolon(semicolon):

    def __init__(self, sString):
        semicolon.__init__(self)

###############################################################################
# Package objects
###############################################################################

class package_keyword(keyword):

    def __init__(self, sString):
        keyword.__init__(self, sString)

class package_identifier(identifier):

    def __init__(self, sString):
        identifier.__init__(self, sString)

class package_is_keyword(keyword):

    def __init__(self, sString):
        keyword.__init__(self, sString)

class package_begin_keyword(keyword):

    def __init__(self, sString):
        keyword.__init__(self, sString)

class package_end_keyword(keyword):

    def __init__(self, sString):
        keyword.__init__(self, sString)

class package_end_package_keyword(keyword):

    def __init__(self, sString):
        keyword.__init__(self, sString)

class package_simple_name(simple_name):

    def __init__(self, sString):
        simple_name.__init__(self, sString)

class package_semicolon(semicolon):

    def __init__(self, sString):
        semicolon.__init__(self)

###############################################################################
# Package Body objects
###############################################################################

class package_body_package_keyword(keyword):

    def __init__(self, sString):
        keyword.__init__(self, sString)

class package_body_body_keyword(keyword):

    def __init__(self, sString):
        keyword.__init__(self, sString)

class package_body_simple_name(identifier):

    def __init__(self, sString):
        identifier.__init__(self, sString)

class package_body_is_keyword(keyword):

    def __init__(self, sString):
        keyword.__init__(self, sString)

class package_body_end_keyword(keyword):

    def __init__(self, sString):
        keyword.__init__(self, sString)

class package_body_end_package_keyword(keyword):

    def __init__(self, sString):
        keyword.__init__(self, sString)

class package_body_end_body_keyword(keyword):

    def __init__(self, sString):
        keyword.__init__(self, sString)

class package_body_end_simple_name(simple_name):

    def __init__(self, sString):
        simple_name.__init__(self, sString)

class package_body_semicolon(semicolon):

    def __init__(self, sString):
        semicolon.__init__(self)


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
# Use objects
###############################################################################


class use_keyword(keyword):

    def __init__(self, sString):
        keyword.__init__(self, sString)

class use_selected_name(selected_name):

    def __init__(self, sString):
        selected_name.__init__(self, sString)

class use_semicolon(semicolon):

    def __init__(self):
        semicolon.__init__(self)

###############################################################################
# Signal objects
###############################################################################

class signal_keyword(keyword):

    def __init__(self, sString):
        keyword.__init__(self, sString)

class signal_identifier(identifier):

    def __init__(self, sString):
        identifier.__init__(self, sString)

class signal_comma(comma):

    def __init__(self):
        comma.__init__(self)

class signal_colon(colon):

    def __init__(self):
        colon.__init__(self)

class signal_subtype_indication(subtype_indication):

    def __init__(self, sString):
        subtype_indication.__init__(self, sString)

class signal_assignment_operator(item):

    def __init__(self):
        item.__init__(self, ':=')

class signal_assignment_expression(item):

    def __init__(self, sString):
        item.__init__(self, sString)

class signal_semicolon(semicolon):

    def __init__(self):
        semicolon.__init__(self)

###############################################################################
# Constant objects
###############################################################################

class constant_keyword(keyword):

    def __init__(self, sString):
        keyword.__init__(self, sString)

class constant_identifier(identifier):

    def __init__(self, sString):
        identifier.__init__(self, sString)

class constant_comma(comma):

    def __init__(self):
        comma.__init__(self)

class constant_colon(colon):

    def __init__(self):
        colon.__init__(self)

class constant_subtype_indication(subtype_indication):

    def __init__(self, sString):
        subtype_indication.__init__(self, sString)

class constant_assignment_operator(item):

    def __init__(self):
        item.__init__(self, ':=')

class constant_assignment_expression(item):

    def __init__(self, sString):
        item.__init__(self, sString)

class constant_semicolon(semicolon):

    def __init__(self):
        semicolon.__init__(self)

###############################################################################
# File objects
###############################################################################

class file_keyword(keyword):

    def __init__(self, sString):
        keyword.__init__(self, sString)

class file_identifier(identifier):

    def __init__(self, sString):
        identifier.__init__(self, sString)

class file_comma(comma):

    def __init__(self):
        comma.__init__(self)

class file_colon(colon):

    def __init__(self):
        colon.__init__(self)

class file_subtype_indication(subtype_indication):

    def __init__(self, sString):
        subtype_indication.__init__(self, sString)

class file_open_keyword(keyword):

    def __init__(self, sString):
        keyword.__init__(self, sString)

class file_open_kind_expression(expression):

    def __init__(self, sString):
        expression.__init__(self, sString)

class file_is_keyword(keyword):

    def __init__(self, sString):
        keyword.__init__(self, sString)

class file_logical_name(logical_name):

    def __init__(self, sString):
        logical_name.__init__(self, sString)

class file_semicolon(semicolon):

    def __init__(self):
        semicolon.__init__(self)


###############################################################################
# Variable objects
###############################################################################

class variable_shared_keyword(keyword):

    def __init__(self, sString):
        keyword.__init__(self, sString)

class variable_keyword(keyword):

    def __init__(self, sString):
        keyword.__init__(self, sString)

class variable_identifier(identifier):

    def __init__(self, sString):
        identifier.__init__(self, sString)

class variable_comma(comma):

    def __init__(self):
        comma.__init__(self)

class variable_colon(colon):

    def __init__(self):
        colon.__init__(self)

class variable_subtype_indication(subtype_indication):

    def __init__(self, sString):
        subtype_indication.__init__(self, sString)

class variable_assignment_operator(item):

    def __init__(self):
        item.__init__(self, ':=')

class variable_assignment_expression(item):

    def __init__(self, sString):
        item.__init__(self, sString)

class variable_semicolon(semicolon):

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


###############################################################################
# Attribute objects
###############################################################################

class attribute_keyword(keyword):

    def __init__(self, sString):
        keyword.__init__(self, sString)


class attribute_identifier(identifier):

    def __init__(self, sString):
        identifier.__init__(self, sString)


class attribute_colon(colon):

    def __init__(self):
        colon.__init__(self)


class attribute_type_mark(item):

    def __init__(self, sString):
        item.__init__(self, sString)


class attribute_semicolon(semicolon):

    def __init__(self):
        semicolon.__init__(self)


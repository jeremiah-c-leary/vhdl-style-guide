
###############################################################################
# Base object
###############################################################################


class item():

    def __init__(self, sString):
        self.value = sString
        self.indent = None
        self.hierarchy = None
        self.context = []
        self.code_tags = []

    def get_value(self):
        return self.value

    def set_value(self, sString):
        self.value = sString

    def length(self):
        return len(self.value)

    def set_indent(self, iIndent):
        self.indent = iIndent

    def get_indent(self):
        return self.indent

    def set_hierarchy(self, iHierarchy):
        self.hierarchy = iHierarchy

    def get_hierarchy(self):
        return self.hierarchy

    def add_context(self, sContext):
        self.context.extend(sContext)

    def pop_context(self):
        return self.context.pop()

    def get_context(self):
        return self.context

    def set_code_tags(self, lCodeTags):
        self.code_tags = lCodeTags.copy()

    def has_code_tag(self, sCodeTag):
        if self.code_tags == ['all']:
            return True
        if sCodeTag in self.code_tags:
            return True
        return False

    def clear_code_tags(self):
        self.code_tags = []

    def set_all_code_tags(self):
        self.code_tags = ['all']


class todo(item):

    def __init__(self, sString):
        item.__init__(self, sString)

###############################################################################
# Base VHDL type classes
###############################################################################


class type(item):

    def __init__(self, sString):
        item.__init__(self, sString)


class function(item):

    def __init__(self, sString):
        item.__init__(self, sString)


class tic(item):

    def __init__(self, sString):
        item.__init__(self, sString)


class event_keyword(item):

    def __init__(self, sString):
        item.__init__(self, sString)


class bar(item):

    def __init__(self, sString='|'):
        item.__init__(self, '|' )


class open_bracket(item):

    def __init__(self, sString='['):
        item.__init__(self, '[')


class close_bracket(item):

    def __init__(self, sString=']'):
        item.__init__(self, ']')


class question_mark(item):

    def __init__(self):
        item.__init__(self, '?')


class undefined_range(item):

    def __init__(self):
        item.__init__(self, '<>')


class error(item):

    def __init__(self, sString):
        item.__init__(self, sString)


class carriage_return(item):

    def __init__(self):
        item.__init__(self, '\n')


class blank_line(item):

    def __init__(self):
        item.__init__(self, '')


class none(item):

    def __init__(self):
        item.__init__(self, None)


class keyword(item):

    def __init__(self, sString):
        item.__init__(self, sString)


class identifier(item):

    def __init__(self, sString):
        item.__init__(self, sString)


class designator(item):

    def __init__(self, sString):
        item.__init__(self, sString)


class colon(item):

    def __init__(self, sString=':'):
        item.__init__(self, sString)


class comma(item):

    def __init__(self, sString=','):
        item.__init__(self, sString)


class semicolon(item):

    def __init__(self, sString=';'):
        item.__init__(self, sString)


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


class target(item):

    def __init__(self, sString):
        item.__init__(self, sString)


class assignment(item):

    def __init__(self, sString):
        item.__init__(self, sString)


class choices(item):

    def __init__(self, sString):
        item.__init__(self, sString)

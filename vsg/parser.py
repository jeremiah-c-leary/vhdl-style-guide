
###############################################################################
# Base object
###############################################################################


class item():
    '''
    unique_id = parser : item
    '''

    def __init__(self, sString):
        self.value = sString
        self.indent = None
        self.hierarchy = None
        self.context = []
        self.code_tags = []
        self.base_token, self.sub_token = self.update_token_types()
        self.filename = None

    def update_token_types(self):
        try:
            lDoc = self.__doc__.split()
            for iDoc, sDoc in enumerate(lDoc):
                if sDoc == 'unique_id':
                    return lDoc[iDoc + 2], lDoc[iDoc + 4]
            return None, None
        except AttributeError:
            return None, None

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

    def get_unique_id(self, sJoin=None):
        if sJoin is None:
            return self.base_token, self.sub_token
        return self.base_token + sJoin + self.sub_token

    def get_base_token(self):
        return self.base_token

    def get_sub_token(self):
        return self.sub_token

    def set_filename(self, sFilename):
        self.filename = sFilename

    def get_filename(self):
        return self.filename


class todo(item):
    '''
    unique_id = parser : todo
    '''

    def __init__(self, sString):
        item.__init__(self, sString)

###############################################################################
# Base VHDL type classes
###############################################################################

class preprocessor(item):
    '''
    unique_id = parser : preprocessor
    '''

    def __init__(self, sString):
        item.__init__(self, sString)


class type(item):
    '''
    unique_id = parser : type
    '''

    def __init__(self, sString):
        item.__init__(self, sString)


class function(item):
    '''
    unique_id = parser : function
    '''

    def __init__(self, sString):
        item.__init__(self, sString)


class tic(item):
    '''
    unique_id = parser : tic
    '''

    def __init__(self, sString):
        item.__init__(self, sString)


class event_keyword(item):
    '''
    unique_id = parser : event_keyword
    '''

    def __init__(self, sString):
        item.__init__(self, sString)


class bar(item):
    '''
    unique_id = parser : bar
    '''

    def __init__(self, sString='|'):
        item.__init__(self, '|' )


class open_bracket(item):
    '''
    unique_id = parser : open_bracket
    '''

    def __init__(self, sString='['):
        item.__init__(self, '[')


class close_bracket(item):
    '''
    unique_id = parser : close_bracket
    '''

    def __init__(self, sString=']'):
        item.__init__(self, ']')


class question_mark(item):
    '''
    unique_id = parser : question_mark
    '''

    def __init__(self):
        item.__init__(self, '?')


class undefined_range(item):
    '''
    unique_id = parser : undefined_range
    '''

    def __init__(self):
        item.__init__(self, '<>')


class error(item):
    '''
    unique_id = parser : error
    '''

    def __init__(self, sString):
        item.__init__(self, sString)


class carriage_return(item):
    '''
    unique_id = parser : carriage_return
    '''

    def __init__(self):
        item.__init__(self, '\n')


class blank_line(item):
    '''
    unique_id = parser : blank_line
    '''

    def __init__(self):
        item.__init__(self, '')


class none(item):
    '''
    unique_id = parser : none
    '''

    def __init__(self):
        item.__init__(self, None)


class keyword(item):
    '''
    unique_id = parser : keyword
    '''

    def __init__(self, sString):
        item.__init__(self, sString)


class identifier(item):
    '''
    unique_id = parser : identifier
    '''

    def __init__(self, sString):
        item.__init__(self, sString)


class designator(item):
    '''
    unique_id = parser : designator
    '''

    def __init__(self, sString):
        item.__init__(self, sString)


class colon(item):
    '''
    unique_id = parser : colon
    '''

    def __init__(self, sString=':'):
        item.__init__(self, sString)


class comma(item):
    '''
    unique_id = parser : comma
    '''

    def __init__(self, sString=','):
        item.__init__(self, sString)


class semicolon(item):
    '''
    unique_id = parser : semicolon
    '''

    def __init__(self, sString=';'):
        item.__init__(self, sString)


class whitespace(item):
    '''
    unique_id = parser : whitespace
    '''

    def __init__(self, sString):
        item.__init__(self, sString)


class comment(item):
    '''
    unique_id = parser : comment
    '''

    def __init__(self, sString):
        item.__init__(self, sString)


class logical_name(item):
    '''
    unique_id = parser : logical_name
    '''

    def __init__(self, sString):
        item.__init__(self, sString)


class selected_name(item):
    '''
    unique_id = parser : selected_name
    '''

    def __init__(self, sString):
        item.__init__(self, sString)


class name(item):
    '''
    unique_id = parser : name
    '''

    def __init__(self, sString):
        item.__init__(self, sString)


class simple_name(item):
    '''
    unique_id = parser : simple_name
    '''

    def __init__(self, sString):
        item.__init__(self, sString)


class subtype_indication(item):
    '''
    unique_id = parser : subtype_indication
    '''

    def __init__(self, sString):
        item.__init__(self, sString)


class condition(item):
    '''
    unique_id = parser : condition
    '''

    def __init__(self, sString):
        item.__init__(self, sString)


class expression(item):
    '''
    unique_id = parser : expression
    '''

    def __init__(self, sString):
        item.__init__(self, sString)


class static_expression(expression):
    '''
    unique_id = parser : static_expression
    '''

    def __init__(self, sString):
        expression.__init__(self, sString)


class label(item):
    '''
    unique_id = parser : label
    '''

    def __init__(self, sString):
        item.__init__(self, sString)


class label_colon(colon):
    '''
    unique_id = parser : label_colon
    '''

    def __init__(self):
        colon.__init__(self)


class open_parenthesis(item):
    '''
    unique_id = parser : open_parenthesis
    '''

    def __init__(self):
        item.__init__(self, '(')


class close_parenthesis(item):
    '''
    unique_id = parser : close_parenthesis
    '''

    def __init__(self):
        item.__init__(self, ')')


class character_literal(item):
    '''
    unique_id = parser : character_literal
    '''

    def __init__(self, sString):
        item.__init__(self, sString)


class string_literal(item):
    '''
    unique_id = parser : string_literal
    '''

    def __init__(self, sString):
        item.__init__(self, sString)


class operator_symbol(string_literal):
    '''
    unique_id = parser : operator_symbol
    '''

    def __init__(self, sString):
        string_literal.__init__(self, sString)


class signature(item):
    '''
    unique_id = parser : signature
    '''

    def __init__(self, sString):
        item.__init__(self, sString)


class type_mark(item):
    '''
    unique_id = parser : type_mark
    '''

    def __init__(self, sString):
        item.__init__(self, sString)


class subtype_definition(item):
    '''
    unique_id = parser : subtype_definition
    '''

    def __init__(self, sString):
        item.__init__(self, sString)


class target(item):
    '''
    unique_id = parser : target
    '''

    def __init__(self, sString):
        item.__init__(self, sString)


class assignment(item):
    '''
    unique_id = parser : assignment
    '''

    def __init__(self, sString):
        item.__init__(self, sString)


class choices(item):
    '''
    unique_id = parser : choices
    '''

    def __init__(self, sString):
        item.__init__(self, sString)


class beginning_of_file(item):
    '''
    unique_id = parser : choices
    '''

    def __init__(self):
        item.__init__(self, 'beginning_of_file')

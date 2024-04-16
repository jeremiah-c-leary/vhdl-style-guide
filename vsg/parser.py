# -*- coding: utf-8 -*-

###############################################################################
# Base object
###############################################################################


class item:
    """
    unique_id = parser : item
    """

    def __init__(self, sString):
        self.value = sString
        self.lower_value = sString.lower()
        self.indent = None
        self.hierarchy = None
        self.context = []
        self.code_tags = []
        self.base_token, self.sub_token = self.update_token_types()
        self.filename = None
        self.iId = None

    def update_token_types(self):
        try:
            lDoc = self.__doc__.split()
            for iDoc, sDoc in enumerate(lDoc):
                if sDoc == "unique_id":
                    return lDoc[iDoc + 2], lDoc[iDoc + 4]
            return None, None
        except AttributeError:
            return None, None

    def get_value(self):
        return self.value

    def get_lower_value(self):
        return self.lower_value

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
        if self.code_tags == ["all"]:
            return True
        if sCodeTag in self.code_tags:
            return True
        return False

    def clear_code_tags(self):
        self.code_tags = []

    def set_all_code_tags(self):
        self.code_tags = ["all"]

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

    def convert_to(self, token):
        oReturn = token(self.value)
        oReturn.indent = self.indent
        oReturn.hierarchy = self.hierarchy
        oReturn.context = self.context
        oReturn.code_tags = self.code_tags
        oReturn.base_token, self.sub_token = self.update_token_types()
        oReturn.filename = self.filename
        oReturn.iId = self.iId
        oReturn.base_token, oReturn.sub_token = oReturn.update_token_types()
        return oReturn


class todo(item):
    """
    unique_id = parser : todo
    """

    def __init__(self, sString):
        super().__init__(sString)


###############################################################################
# Base VHDL type classes
###############################################################################


class preprocessor(item):
    """
    unique_id = parser : preprocessor
    """

    def __init__(self, sString):
        super().__init__(sString)


class type(item):
    """
    unique_id = parser : type
    """

    def __init__(self, sString):
        super().__init__(sString)


class function(item):
    """
    unique_id = parser : function
    """

    def __init__(self, sString):
        super().__init__(sString)


class tic(item):
    """
    unique_id = parser : tic
    """

    def __init__(self, sString):
        super().__init__(sString)


class attribute(item):
    """
    unique_id = parser : attribute
    """

    def __init__(self, sString):
        super().__init__(sString)


class event_keyword(item):
    """
    unique_id = parser : event_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class bar(item):
    """
    unique_id = parser : bar
    """

    def __init__(self, sString="|"):
        super().__init__("|")


class open_bracket(item):
    """
    unique_id = parser : open_bracket
    """

    def __init__(self, sString="["):
        super().__init__("[")


class close_bracket(item):
    """
    unique_id = parser : close_bracket
    """

    def __init__(self, sString="]"):
        super().__init__("]")


class question_mark(item):
    """
    unique_id = parser : question_mark
    """

    def __init__(self):
        super().__init__("?")


class undefined_range(item):
    """
    unique_id = parser : undefined_range
    """

    def __init__(self):
        super().__init__("<>")


class error(item):
    """
    unique_id = parser : error
    """

    def __init__(self, sString):
        super().__init__(sString)


class carriage_return(item):
    """
    unique_id = parser : carriage_return
    """

    def __init__(self):
        super().__init__("\n")


class blank_line(item):
    """
    unique_id = parser : blank_line
    """

    def __init__(self):
        super().__init__("")


class none(item):
    """
    unique_id = parser : none
    """

    def __init__(self):
        super().__init__(None)


class keyword(item):
    """
    unique_id = parser : keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class identifier(item):
    """
    unique_id = parser : identifier
    """

    def __init__(self, sString):
        super().__init__(sString)


class designator(item):
    """
    unique_id = parser : designator
    """

    def __init__(self, sString):
        super().__init__(sString)


class colon(item):
    """
    unique_id = parser : colon
    """

    def __init__(self, sString=":"):
        super().__init__(sString)


class comma(item):
    """
    unique_id = parser : comma
    """

    def __init__(self, sString=","):
        super().__init__(sString)


class dot(item):
    """
    unique_id = parser : dot
    """

    def __init__(self, sString="."):
        super().__init__(sString)


class semicolon(item):
    """
    unique_id = parser : semicolon
    """

    def __init__(self, sString=";"):
        super().__init__(sString)


class whitespace(item):
    """
    unique_id = parser : whitespace
    """

    def __init__(self, sString):
        super().__init__(sString)
        self.has_tab = False


class comment(item):
    """
    unique_id = parser : comment
    """

    def __init__(self, sString):
        super().__init__(sString)
        self.is_block_comment = False
        self.block_comment_indent = None
        self.has_tab = False


class logical_name(item):
    """
    unique_id = parser : logical_name
    """

    def __init__(self, sString):
        super().__init__(sString)


class selected_name(item):
    """
    unique_id = parser : selected_name
    """

    def __init__(self, sString):
        super().__init__(sString)


class name(item):
    """
    unique_id = parser : name
    """

    def __init__(self, sString):
        super().__init__(sString)


class simple_name(item):
    """
    unique_id = parser : simple_name
    """

    def __init__(self, sString):
        super().__init__(sString)


class subtype_indication(item):
    """
    unique_id = parser : subtype_indication
    """

    def __init__(self, sString):
        super().__init__(sString)


class condition(item):
    """
    unique_id = parser : condition
    """

    def __init__(self, sString):
        super().__init__(sString)


class expression(item):
    """
    unique_id = parser : expression
    """

    def __init__(self, sString):
        super().__init__(sString)


class static_expression(expression):
    """
    unique_id = parser : static_expression
    """

    def __init__(self, sString):
        super().__init__(sString)


class label(item):
    """
    unique_id = parser : label
    """

    def __init__(self, sString):
        super().__init__(sString)


class label_colon(colon):
    """
    unique_id = parser : label_colon
    """

    def __init__(self):
        super().__init__()


class open_parenthesis(item):
    """
    unique_id = parser : open_parenthesis
    """

    def __init__(self):
        super().__init__("(")


class close_parenthesis(item):
    """
    unique_id = parser : close_parenthesis
    """

    def __init__(self):
        super().__init__(")")


class equal_sign(item):
    """
    unique_id = parser : equal_sign
    """

    def __init__(self):
        super().__init__("=")


class character_literal(item):
    """
    unique_id = parser : character_literal
    """

    def __init__(self, sString):
        super().__init__(sString)


class string_literal(item):
    """
    unique_id = parser : string_literal
    """

    def __init__(self, sString):
        super().__init__(sString)


class operator_symbol(string_literal):
    """
    unique_id = parser : operator_symbol
    """

    def __init__(self, sString):
        super().__init__(sString)


class signature(item):
    """
    unique_id = parser : signature
    """

    def __init__(self, sString):
        super().__init__(sString)


class type_mark(item):
    """
    unique_id = parser : type_mark
    """

    def __init__(self, sString):
        super().__init__(sString)


class subtype_definition(item):
    """
    unique_id = parser : subtype_definition
    """

    def __init__(self, sString):
        super().__init__(sString)


class target(item):
    """
    unique_id = parser : target
    """

    def __init__(self, sString):
        super().__init__(sString)


class assignment(item):
    """
    unique_id = parser : assignment
    """

    def __init__(self, sString):
        super().__init__(sString)


class choices(item):
    """
    unique_id = parser : choices
    """

    def __init__(self, sString):
        super().__init__(sString)


class beginning_of_file(item):
    """
    unique_id = parser : choices
    """

    def __init__(self):
        super().__init__("beginning_of_file")


class slice_name:
    """
    unique_id = parser : slice_name
    """

    def __init__(self, lTokens):
        self.tokens = lTokens

    def get_tokens(self):
        return self.tokens


class integer(item):
    """
    unique_id = parser : integer
    """

    def __init__(self, sString):
        super().__init__(sString)

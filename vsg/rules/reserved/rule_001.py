# -*- coding: utf-8 -*-

from vsg import token, violation
from vsg.rule_group import structure


def uniquify_standards(dMap):
    lReturn = []
    for sKey in list(dMap.keys()):
        for sWord in dMap[sKey]:
            if not sWord in lReturn:
                lReturn.append(sWord)
    return lReturn


dMap = {}
# https://redirect.cs.umbc.edu/portal/help/VHDL/VHDL-Handbook.pdf
dMap["1987"] = [
    "abs",
    "access",
    "after",
    "alias",
    "all",
    "and",
    "architecture",
    "array",
    "assert",
    "attribute",
    "begin",
    "block",
    "body",
    "buffer",
    "bus",
    "case",
    "component",
    "configuration",
    "constant",
    "disconnect",
    "downto",
    "else",
    "elsif",
    "end",
    "entity",
    "exit",
    "file",
    "for",
    "function",
    "generate",
    "generic",
    "group",
    "guarded",
    "if",
    "impure",
    "in",
    "inertial",
    "inout",
    "is",
    "label",
    "library",
    "linkage",
    "literal",
    "loop",
    "map",
    "mod",
    "nand",
    "new",
    "next",
    "nor",
    "not",
    "null",
    "of",
    "on",
    "open",
    "or",
    "others",
    "out",
    "package",
    "port",
    "postponed",
    "procedure",
    "process",
    "pure",
    "range",
    "record",
    "register",
    "reject",
    "rem",
    "report",
    "return",
    "rol",
    "ror",
    "select",
    "severity",
    "signal",
    "shared",
    "sla",
    "sll",
    "sra",
    "srl",
    "subtype",
    "then",
    "to",
    "transport",
    "type",
    "unaffected",
    "units",
    "until",
    "use",
    "variable",
    "wait",
    "when",
    "while",
    "with",
    "xnor",
    "xor",
]
# http://www.dacya.ucm.es/dani/manual.pdf
dMap["1993"] = [
    "abs",
    "access",
    "after",
    "alias",
    "all",
    "and",
    "architecture",
    "array",
    "assert",
    "attribute",
    "begin",
    "block",
    "body",
    "buffer",
    "bus",
    "case",
    "component",
    "configuration",
    "constant",
    "disconnect",
    "downto",
    "else",
    "elsif",
    "end",
    "entity",
    "exit",
    "file",
    "for",
    "function",
    "generate",
    "generic",
    "group",
    "guarded",
    "if",
    "impure",
    "in",
    "inertial",
    "inout",
    "is",
    "label",
    "library",
    "linkage",
    "literal",
    "loop",
    "map",
    "mod",
    "nand",
    "new",
    "next",
    "nor",
    "not",
    "null",
    "of",
    "on",
    "open",
    "or",
    "others",
    "out",
    "package",
    "port",
    "postponed",
    "procedure",
    "process",
    "pure",
    "range",
    "record",
    "register",
    "reject",
    "rem",
    "report",
    "return",
    "rol",
    "ror",
    "select",
    "severity",
    "signal",
    "shared",
    "sla",
    "sll",
    "sra",
    "srl",
    "subtype",
    "then",
    "to",
    "transport",
    "type",
    "unaffected",
    "units",
    "until",
    "use",
    "variable",
    "wait",
    "when",
    "while",
    "with",
    "xnor",
    "xor",
]
# https://edg.uchicago.edu/~tang/VHDLref.pdf
dMap["2000"] = [
    "abs",
    "access",
    "after",
    "alias",
    "all",
    "and",
    "architecture",
    "array",
    "assert",
    "attribute",
    "begin",
    "block",
    "body",
    "buffer",
    "bus",
    "case",
    "component",
    "configuration",
    "constant",
    "disconnect",
    "downto",
    "else",
    "elsif",
    "end",
    "entity",
    "exit",
    "file",
    "for",
    "function",
    "generate",
    "generic",
    "group",
    "guarded",
    "if",
    "impure",
    "in",
    "inertial",
    "inout",
    "is",
    "label",
    "library",
    "linkage",
    "literal",
    "loop",
    "map",
    "mod",
    "nand",
    "new",
    "next",
    "nor",
    "not",
    "null",
    "of",
    "on",
    "open",
    "or",
    "others",
    "out",
    "package",
    "port",
    "postponed",
    "procedural",
    "procedure",
    "process",
    "protected",
    "pure",
    "range",
    "record",
    "reference",
    "register",
    "reject",
    "rem",
    "report",
    "return",
    "rol",
    "ror",
    "select",
    "severity",
    "signal",
    "shared",
    "sla",
    "sll",
    "sra",
    "srl",
    "subtype",
    "then",
    "to",
    "transport",
    "type",
    "unaffected",
    "units",
    "until",
    "use",
    "variable",
    "wait",
    "when",
    "while",
    "with",
    "xnor",
    "xor",
]
# https://vhdl-manual.narod.ru/books/ieee_manual.pdf
dMap["2002"] = [
    "abs",
    "access",
    "after",
    "alias",
    "all",
    "and",
    "architecture",
    "array",
    "assert",
    "attribute",
    "begin",
    "block",
    "body",
    "buffer",
    "bus",
    "case",
    "component",
    "configuration",
    "constant",
    "disconnect",
    "downto",
    "else",
    "elsif",
    "end",
    "entity",
    "exit",
    "file",
    "for",
    "function",
    "generate",
    "generic",
    "group",
    "guarded",
    "if",
    "impure",
    "in",
    "inertial",
    "inout",
    "is",
    "label",
    "library",
    "linkage",
    "literal",
    "loop",
    "map",
    "mod",
    "nand",
    "new",
    "next",
    "nor",
    "not",
    "null",
    "of",
    "on",
    "open",
    "or",
    "others",
    "out",
    "package",
    "port",
    "postponed",
    "procedural",
    "procedure",
    "process",
    "protected",
    "pure",
    "range",
    "record",
    "reference",
    "register",
    "reject",
    "rem",
    "report",
    "return",
    "rol",
    "ror",
    "select",
    "severity",
    "signal",
    "shared",
    "sla",
    "sll",
    "sra",
    "srl",
    "subtype",
    "then",
    "to",
    "transport",
    "type",
    "unaffected",
    "units",
    "until",
    "use",
    "variable",
    "wait",
    "when",
    "while",
    "with",
    "xnor",
    "xor",
]
# Unknown
dMap["2008"] = [
    "abs",
    "access",
    "after",
    "alias",
    "all",
    "and",
    "architecture",
    "array",
    "assert",
    "assume",
    "assume_guarantee",
    "attribute",
    "begin",
    "block",
    "body",
    "buffer",
    "bus",
    "case",
    "component",
    "configuration",
    "constant",
    "context",
    "cover",
    "default",
    "disconnect",
    "downto",
    "else",
    "elsif",
    "end",
    "entity",
    "exit",
    "fairness",
    "file",
    "for",
    "force",
    "function",
    "generate",
    "generic",
    "group",
    "guarded",
    "if",
    "impure",
    "in",
    "inertial",
    "inout",
    "is",
    "label",
    "library",
    "linkage",
    "literal",
    "loop",
    "map",
    "mod",
    "nand",
    "new",
    "next",
    "nor",
    "not",
    "null",
    "of",
    "on",
    "open",
    "or",
    "others",
    "out",
    "package",
    "parameter",
    "port",
    "postponed",
    "procedure",
    "process",
    "property",
    "protected",
    "pure",
    "range",
    "record",
    "register",
    "reject",
    "release",
    "rem",
    "report",
    "restrict",
    "restrict_guarantee",
    "return",
    "rol",
    "ror",
    "select",
    "sequence",
    "severity",
    "signal",
    "shared",
    "sla",
    "sll",
    "sra",
    "srl",
    "strong",
    "subtype",
    "then",
    "to",
    "transport",
    "type",
    "unaffected",
    "units",
    "until",
    "use",
    "variable",
    "vmode",
    "vprop",
    "vunit",
    "wait",
    "when",
    "while",
    "with",
    "xnor",
    "xor",
]
dMap["all"] = uniquify_standards(dMap)


lIdentifiers = []
lIdentifiers.append(token.architecture_body.identifier)
lIdentifiers.append(token.architecture_body.identifier)
lIdentifiers.append(token.attribute_declaration.identifier)
lIdentifiers.append(token.component_declaration.identifier)
lIdentifiers.append(token.configuration_declaration.identifier)
lIdentifiers.append(token.constant_declaration.identifier)
lIdentifiers.append(token.context_declaration.identifier)
lIdentifiers.append(token.entity_aspect.architecture_identifier)
lIdentifiers.append(token.entity_declaration.identifier)
lIdentifiers.append(token.entity_designator.entity_tag)
lIdentifiers.append(token.file_declaration.identifier)
lIdentifiers.append(token.full_type_declaration.identifier)
lIdentifiers.append(token.group_declaration.identifier)
lIdentifiers.append(token.identifier.identifier)
lIdentifiers.append(token.identifier_list.identifier)
lIdentifiers.append(token.incomplete_type_declaration.identifier)
lIdentifiers.append(token.instantiated_unit.architecture_identifier)
lIdentifiers.append(token.interface_constant_declaration.identifier)
lIdentifiers.append(token.interface_file_declaration.identifier)
lIdentifiers.append(token.interface_signal_declaration.identifier)
lIdentifiers.append(token.interface_unknown_declaration.identifier)
lIdentifiers.append(token.interface_variable_declaration.identifier)
lIdentifiers.append(token.package_declaration.identifier)
lIdentifiers.append(token.parameter_specification.identifier)
lIdentifiers.append(token.primary_unit_declaration.identifier)
lIdentifiers.append(token.secondary_unit_declaration.identifier)
lIdentifiers.append(token.signal_declaration.identifier)
lIdentifiers.append(token.subprogram_instantiation_declaration.identifier)
lIdentifiers.append(token.subtype_declaration.identifier)
lIdentifiers.append(token.variable_declaration.identifier)
### Simple Names
lIdentifiers.append(token.architecture_body.architecture_simple_name)
lIdentifiers.append(token.component_declaration.component_simple_name)
lIdentifiers.append(token.configuration_declaration.configuration_simple_name)
lIdentifiers.append(token.context_declaration.context_simple_name)
lIdentifiers.append(token.entity_declaration.entity_simple_name)
lIdentifiers.append(token.package_body.package_simple_name)
lIdentifiers.append(token.package_body.end_package_simple_name)
lIdentifiers.append(token.package_declaration.end_package_simple_name)
lIdentifiers.append(token.physical_type_definition.simple_name)
lIdentifiers.append(token.protected_type_body.protected_type_simple_name)
lIdentifiers.append(token.protected_type_declaration.protected_type_simple_name)
lIdentifiers.append(token.record_element_constraint.record_element_simple_name)
lIdentifiers.append(token.record_type_definition.record_type_simple_name)
### Designators
lIdentifiers.append(token.alias_declaration.alias_designator)
lIdentifiers.append(token.attribute_specification.attribute_designator)
lIdentifiers.append(token.function_specification.designator)
lIdentifiers.append(token.interface_function_specification.designator)
lIdentifiers.append(token.interface_procedure_specification.designator)
lIdentifiers.append(token.procedure_specification.designator)
lIdentifiers.append(token.subprogram_body.designator)


class rule_001(structure.Rule):
    """
    This rule checks for VHDL reserved words being used as identifiers and names.

    |configuring_vhdl_reserved_words_link|

    **Violation**

    .. code-block:: vhdl

       entity null is
       end null;
    """

    def __init__(self):
        super().__init__()
        self.configuration.append("standard")
        self.standard = "all"
        self.fixable = False
        self.configuration_documentation_link = "configuring_vhdl_reserved_words_link"

    def _get_tokens_of_interest(self, oFile):
        lReturn = oFile.get_tokens_matching(lIdentifiers)
        return lReturn

    def _analyze(self, lToi):
        lReservedWords = dMap[self.standard]
        for oToi in lToi:
            if token_value_is_a_reserved_word(oToi, lReservedWords):
                self.create_violation(oToi)

    def create_violation(self, oToi):
        oToken = oToi.get_tokens()[0]
        sSolution = "Invalid use of reserved word " + oToken.get_value()
        oViolation = violation.New(oToi.get_line_number(), oToi, sSolution)
        self.add_violation(oViolation)


def token_value_is_a_reserved_word(oToi, lReservedWords):
    oToken = oToi.get_tokens()[0]
    if oToken.get_lower_value() in lReservedWords:
        return True
    return False

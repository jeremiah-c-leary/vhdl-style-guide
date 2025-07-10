# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token.psl import psl_directive as token
from vsg.vhdlFile.classify import (
    psl_assert_directive,
    psl_assume_directive,
    psl_cover_directive,
    psl_fairness_statement,
    psl_restrict_directive,
    psl_restrict_n_directive,
    utils,
)


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    PSL_Directive ::=
        [ label : ] Verification_Directive

    Verification_Directive ::=
        Assert_Directive
      | Assume_Directive
      | Restrict_Directive
      | Restrict_n_Directive
      | Cover_Directive
      | Fairness_Statement
    """

    if psl_assert_directive.detect(oDataStructure):
        utils.tokenize_label(oDataStructure, token.label_name, token.label_colon)
        psl_assert_directive.classify(oDataStructure)
        return True

    if psl_assume_directive.detect(oDataStructure):
        utils.tokenize_label(oDataStructure, token.label_name, token.label_colon)
        psl_assume_directive.classify(oDataStructure)
        return True

    if psl_restrict_directive.detect(oDataStructure):
        utils.tokenize_label(oDataStructure, token.label_name, token.label_colon)
        psl_restrict_directive.classify(oDataStructure)
        return True

    if psl_restrict_n_directive.detect(oDataStructure):
        utils.tokenize_label(oDataStructure, token.label_name, token.label_colon)
        psl_restrict_n_directive.classify(oDataStructure)
        return True

    if psl_cover_directive.detect(oDataStructure):
        utils.tokenize_label(oDataStructure, token.label_name, token.label_colon)
        psl_cover_directive.classify(oDataStructure)
        return True

    if psl_fairness_statement.detect(oDataStructure):
        utils.tokenize_label(oDataStructure, token.label_name, token.label_colon)
        psl_fairness_statement.classify(oDataStructure)
        return True

    return False

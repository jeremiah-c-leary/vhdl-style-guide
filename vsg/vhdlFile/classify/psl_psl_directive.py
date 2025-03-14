# -*- coding: utf-8 -*-

from vsg.token.psl import psl_directive as token
from vsg.vhdlFile import utils
from vsg.vhdlFile.classify import (
    psl_assert_directive,
    psl_assume_directive,
    psl_cover_directive,
    psl_fairness_statement,
    psl_restrict_directive,
    psl_restrict_n_directive,
)


def detect(iToken, lObjects):
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

    iCurrent = iToken
    if psl_assert_directive.detect(iToken, lObjects):
        iCurrent = utils.tokenize_label(iCurrent, lObjects, token.label_name, token.label_colon)
        iCurrent = psl_assert_directive.classify(iCurrent, lObjects)

    elif psl_assume_directive.detect(iToken, lObjects):
        iCurrent = utils.tokenize_label(iCurrent, lObjects, token.label_name, token.label_colon)
        iCurrent = psl_assume_directive.classify(iCurrent, lObjects)

    elif psl_restrict_directive.detect(iToken, lObjects):
        iCurrent = utils.tokenize_label(iCurrent, lObjects, token.label_name, token.label_colon)
        iCurrent = psl_restrict_directive.classify(iCurrent, lObjects)

    elif psl_restrict_n_directive.detect(iToken, lObjects):
        iCurrent = utils.tokenize_label(iCurrent, lObjects, token.label_name, token.label_colon)
        iCurrent = psl_restrict_n_directive.classify(iCurrent, lObjects)

    elif psl_cover_directive.detect(iToken, lObjects):
        iCurrent = utils.tokenize_label(iCurrent, lObjects, token.label_name, token.label_colon)
        iCurrent = psl_cover_directive.classify(iCurrent, lObjects)

    elif psl_fairness_statement.detect(iToken, lObjects):
        iCurrent = utils.tokenize_label(iCurrent, lObjects, token.label_name, token.label_colon)
        iCurrent = psl_fairness_statement.classify(iCurrent, lObjects)

    return iCurrent

# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.vhdlFile.classify import aggregate, utils


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure, oTokenClass):
    """
    target ::=
        name
      | aggregate
    """
    if oDataStructure.is_next_seek_token("("):
        aggregate.classify(oDataStructure, oTokenClass)
    else:
        utils.assign_tokens_until(":=", oTokenClass.simple_name, oDataStructure)

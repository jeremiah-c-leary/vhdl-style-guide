# -*- coding: utf-8 -*-
import os
import unittest

from tests import utils
from vsg import vhdlFile

try:
    sLrmUnit = os.environ['vsg_element']

    lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(os.path.dirname(__file__), sLrmUnit,'classification_test_input.vhd'))
    oFile = vhdlFile.vhdlFile(lFile)


    class test_token(unittest.TestCase):


        def test_debug(self):
            utils.print_objects(oFile,True)

except KeyError:
  pass

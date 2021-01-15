import os

import unittest

from vsg import vhdlFile
from vsg.tests import utils

try:
    sLrmUnit = os.environ['vsg_file_to_parse']

    lFile, eError =vhdlFile.utils.read_vhdlfile(sLrmUnit)
    oFile = vhdlFile.vhdlFile(lFile)


    class test_token(unittest.TestCase):


        def test_debug(self):
            utils.print_objects(oFile,True)

except KeyError:
  pass

Formatting Terminal Output
--------------------------

VSG supports multiple display output using the `-of` command line argument.

+-------------+---------------------------------------------------------------+
| Option      | Description                                                   |
+=============+===============================================================+
| vsg         | Default output format.                                        |
+-------------+---------------------------------------------------------------+
| syntastic   | Output format following the syntastic standard.  Useful for   |
|             | integrating with Vim.                                         |
+-------------+---------------------------------------------------------------+
| summary     | Output format showing the results at the file level.          |
+-------------+---------------------------------------------------------------+


VSG
###

This is the default output format of VSG.
It gives analysis statistics along with individual rule violations.
This format is the most verbose of all output formats.

Sample output using VSG option:

.. code-block:: text

   ================================================================================
   File:  design_fixed/BufFifo/BUF_FIFO.vhd
   ================================================================================
   Phase 1 of 7... Reporting
   Total Rules Checked: 83
   Total Violations:    17
     Error   :    17
     Warning :     0
   ----------------------------+------------+------------+--------------------------------------
     Rule                      |  severity  |  line(s)   | Solution
   ----------------------------+------------+------------+--------------------------------------
     port_021                  | Error      |         45 | Move the ( to the same line as the "port" keyword.
     instantiation_034         | Error      |        169 | Change to component instantiation
     generic_map_003           | Error      |        170 | Move the ( to the same line as the "generic map" keyword.
     port_map_003              | Error      |        175 | Move the ( to the same line as the "port map" keyword.
     instantiation_034         | Error      |        186 | Change to component instantiation
     instantiation_034         | Error      |        196 | Change to component instantiation
     generic_map_003           | Error      |        197 | Move the ( to the same line as the "generic map" keyword.
     port_map_003              | Error      |        202 | Move the ( to the same line as the "port map" keyword.
     instantiation_034         | Error      |        213 | Change to component instantiation
     generic_map_003           | Error      |        214 | Move the ( to the same line as the "generic map" keyword.
     port_map_003              | Error      |        219 | Move the ( to the same line as the "port map" keyword.
     process_012               | Error      |        231 | Add *is* keyword
     if_002                    | Error      |        313 | Enclose condition in ()'s.
     process_012               | Error      |        337 | Add *is* keyword
     if_002                    | Error      |        366 | Enclose condition in ()'s.
     process_012               | Error      |        376 | Add *is* keyword
     if_002                    | Error      |        455 | Enclose condition in ()'s.
   ----------------------------+------------+------------+--------------------------------------
   NOTE: Refer to online documentation at https://vhdl-style-guide.readthedocs.io/en/latest/index.html for more information.

Syntastic
#########

Using the syntastic format allows editors with understand that standard to use the output of VSG.

Below is the output format definition:

.. code-block:: text

   <status>: <filename>(<line_number>)<rule> -- <solution>

Where:

+--------------+---------------------------------------------------------------+
| Item         | Description                                                   |
+==============+===============================================================+
| status       | ERROR = Violation.                                            |
|              | WARNING = Non Violation.                                      |
+--------------+---------------------------------------------------------------+
| filename     | The file being analyzed.                                      |
+--------------+---------------------------------------------------------------+
| line_number  | The line number the violation occurred.                        |
+--------------+---------------------------------------------------------------+
| rule         | The rule id that detected the violation                       |
+--------------+---------------------------------------------------------------+
| solution     | A description of how to fix the violation                     |
+--------------+---------------------------------------------------------------+

Here is a sample output using the **syntastic** option:

.. code-block:: text

   ERROR: design_fixed/mdct/DBUFCTL.VHD(38)entity_017 -- Move : -1 columns
   ERROR: design_fixed/mdct/DBUFCTL.VHD(59)process_035 -- Move 13 columns
   ERROR: design_fixed/mdct/DCT2D.VHD(329)instantiation_033 -- Add *component* keyword
   ERROR: design_fixed/mdct/MDCT.VHD(83)instantiation_034 -- Change to component instantiation
   ERROR: design_fixed/mdct/RAM.VHD(36)entity_017 -- Move : -12 columns

Summary
#######

Using the summary format will display results at the file level.
Individual rule violations will not be displayed.

Below is the output format definition:

.. code-block:: text

    File: <filename> <status> (<num_rules> rules checked) [<severity>: <num_severity>] ...

Where:

+--------------+---------------------------------------------------------------+
| Item         | Description                                                   |
+==============+===============================================================+
| filename     | The file being analyzed.                                      |
+--------------+---------------------------------------------------------------+
| status       | OK = No violations detected.                                  |
|              | ERROR = Violations detected.                                  |
+--------------+---------------------------------------------------------------+
| num_rules    | The number of rules checked before a violation was detected.  |
+--------------+---------------------------------------------------------------+
| severity     | The severity type being reported.                             |
+--------------+---------------------------------------------------------------+
| num_severity | The number of violations of that severity type                |
+--------------+---------------------------------------------------------------+

.. NOTE:: The <severity> and <num_severity> will be repeated for each severity type.

Sample output using the **summary** option:

.. code-block:: text

   File: design/top/JpegEnc.vhd ERROR (83 rules checked) [Error: 23] [Warning: 0]
   File: design/BufFifo/SUB_RAMZ.VHD OK (329 rules checked) [Error: 0] [Warning: 0]
   File: design/common/RAMZ.VHD OK (329 rules checked) [Error: 0] [Warning: 0]
   File: design/mdct/DBUFCTL.VHD OK (329 rules checked) [Error: 0] [Warning: 0]
   File: design/mdct/DCT2D.VHD ERROR (83 rules checked) [Error: 1] [Warning: 0]


Any line with an ERROR will be reported to stderr.

Any line with an OK will be reported to stdout.

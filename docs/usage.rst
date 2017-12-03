Usage
=====

VSG is a command line tool and is invoked with...

.. code-block:: bash

   $ vsg
   
   usage: VHDL Style Guide (VSG) [-h] -f FILENAME [--local_rules LOCAL_RULES]
                                 [--configuration CONFIGURATION] [--fix]
   
   Analyzes VHDL files for style guide violations.
   
   optional arguments:
     -h, --help            show this help message and exit
     -f FILENAME, --filename FILENAME
                           File to analyze
     --local_rules LOCAL_RULES
                           Path to local rules
     --configuration CONFIGURATION
                           JSON configuration file
     --fix                 Fix issues found


Here is an example output running against a test file:

.. code-block:: bash

   $ vsg -f PIC.vhd 
   File:  PIC.vhd
   ==============
   Phase 1... Reporting
   Phase 2... Reporting
   Phase 3... Reporting
   Phase 4... Reporting
   Phase 5... Reporting
     comment_002               |         51 | Ensure proper alignment of comment with previous line.
     comment_002               |         52 | Ensure proper alignment of comment with previous line.
     comment_002               |         54 | Ensure proper alignment of comment with previous line.
     comment_002               |         55 | Ensure proper alignment of comment with previous line.
     comment_003               |     76-256 | Inconsistent alignment of comments within process.
     sequential_005            |      87-93 | Inconsistent alignment of "<=" in group of lines.
     sequential_005            |    102-103 | Inconsistent alignment of "<=" in group of lines.
     sequential_005            |    105-108 | Inconsistent alignment of "<=" in group of lines.
     sequential_005            |    110-113 | Inconsistent alignment of "<=" in group of lines.
     sequential_005            |    115-118 | Inconsistent alignment of "<=" in group of lines.
     sequential_005            |    120-124 | Inconsistent alignment of "<=" in group of lines.
     sequential_005            |    129-133 | Inconsistent alignment of "<=" in group of lines.
     sequential_005            |    160-161 | Inconsistent alignment of "<=" in group of lines.
     sequential_005            |    173-174 | Inconsistent alignment of "<=" in group of lines.
     comment_002               |        183 | Ensure proper alignment of comment with previous line.
     sequential_005            |    225-226 | Inconsistent alignment of "<=" in group of lines.
     sequential_005            |    238-239 | Inconsistent alignment of "<=" in group of lines.
   Phase 6... Not executed
   Phase 7... Not executed
   ==============
   Total Rules Checked: 204
   Total Failures:      523


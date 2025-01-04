.. _configuring-user-error-messages:

Configuring User Error Messages
-------------------------------

There is an option to provide additional information to the user when a violation is found.
This is accomplished by using the :code:`user_error_message` option.
Setting this option for a rule will append the message to the normal output.

Example without :code:`user_error_message` defined
##################################################

Applying a custom regex does not provide additional information to the user.

Given the following configuration file which defines a custom regex:

.. code-block:: yaml

    rule:
      group:
          case::name:
              case: regex
              regex: (?![a-z||0-9]\u005F)(?!.*\u005F[a-z||0-9]$)([a-z||0-9]+(?:\u005F[a-z||0-9]+)*)

The following error report is generated:

.. code-block:: bash

   $vsg -f original.vhd -c config.yaml
   ================================================================================
   File:  original.vhd
   ================================================================================
   Phase 6 of 7... Reporting
   Total Rules Checked: 857
   Total Violations:    2
     Error   :     2
     Warning :     0
   -------------+------------+------------+--------------------------------------
     Rule       |  severity  |  line(s)   | Solution
   -------------+------------+------------+--------------------------------------
     entity_008 | Error      |          2 | Format FIFO to match defined regex
     entity_012 | Error      |          3 | Format FIFO to match defined regex
   -------------+------------+------------+--------------------------------------
   NOTE: Refer to online documentation at https://vhdl-style-guide.readthedocs.io/en/latest/index.html for more information.

Example with :code:`user_error_message` defined
###############################################

Adding a custom error message can provide additional information to the user:

.. code-block:: yaml

    rule:
      group:
          case::name:
              case: regex
              regex: (?![a-z||0-9]\u005F)(?!.*\u005F[a-z||0-9]$)([a-z||0-9]+(?:\u005F[a-z||0-9]+)*)
              user_error_message: "UPPERCASE and single letter prefix/suffix not allowed"

The following error report is generated:

.. code-block:: bash

   $vsg -f original.vhd -c config.yaml
   ================================================================================
   File:  original.vhd
   ================================================================================
   Phase 6 of 7... Reporting
   Total Rules Checked: 857
   Total Violations:    2
     Error   :     2
     Warning :     0
   -------------+------------+------------+--------------------------------------
     Rule       |  severity  |  line(s)   | Solution
   -------------+------------+------------+--------------------------------------
     entity_008 | Error      |          2 | Format FIFO to match defined regex [user_error_message: UPPERCASE and single letter prefix/suffix not allowed]
     entity_012 | Error      |          3 | Format FIFO to match defined regex [user_error_message: UPPERCASE and single letter prefix/suffix not allowed]
   -------------+------------+------------+--------------------------------------
   NOTE: Refer to online documentation at https://vhdl-style-guide.readthedocs.io/en/latest/index.html for more information.


.. _configuring-multiline-report-rule:

Configuring Multiline Assert Rule
---------------------------------

There is a rule which will check indent of multiline assert statements.
The method of indenting can be configured using one of the following options:

.. |alignment| replace::
   :code:`alignment`

.. |left_description| replace::
   The setting :code:`left` enforces multiline report statements using indents.

.. |report_description| replace::
   The setting :code:`report` aligns multiline report statements to the report keyword.

.. |values| replace::
   :code:`left`, :code:`report`

.. |default_value| replace::
   :code:`left`

.. |report| replace::
   :code:'report`

.. |left| replace::
   :code:'left`

+----------------------+----------+-----------------+----------------------------+
| Option               | Values   | Default Value   | Description                |
+======================+==========+=================+============================+
| |alignment|          | |values| | |default_value| | * |left_description|       |
|                      |          |                 | * |report_description|     |
+----------------------+----------+-----------------+----------------------------+

This is an example of how to configure these options.

.. code-block:: yaml

   rule :
     report_statement_400:
        alignment: 'left'

Example: |alignment| set to |report|
####################################

Align report expressions with the report keyword.

.. code-block:: vhdl

   assert WIDTH > 16
     report "FIFO width is limited" &
            " to 16 bits."
     severity FAILURE;

Example: |alignment| set to |left|
##################################

Align report expressions an additional indent level from the report keyword.

.. code-block:: vhdl

   assert WIDTH > 16
     report "FIFO width is limited" &
       " to 16 bits."
     severity FAILURE;

Rules Enforcing Alignment
#########################

* `assert_400 <assert_rules.html#assert-400>`_
* `report_statement_400 <report_statement_rules.html#report-statement-400>`_


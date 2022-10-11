
.. _configuring-multiline-report-rule:

Configuring Multiline Assert Rule
---------------------------------

There is a rule which will check indent of multiline assert statements.
The method of indenting can be configured using one of the following options:

.. |left_description| replace::
   The setting :code:`left` enforces multiline report statements using indents.

.. |report_description| replace::
   The setting :code:`report` aligns multiline report statements to the report keyword.

.. |values| replace::
   :code:`left`, :code:`report`

.. |default_value| replace::
   :code:`left`

+----------------------+----------+-----------------+----------------------------+
| Option               | Values   | Default Value   | Description                |
+======================+==========+=================+============================+
| :code:`alignment`    | |values| | |default_value| | * |left_description|       |
|                      |          |                 | * |report_description|     |
+----------------------+----------+-----------------+----------------------------+

Example: :code:`alignment` set to :code:`report`
################################################

Setting the :code:`alignment` option to :code:`report` will align report expressions with the report keyword.

.. code-block:: vhdl

   assert WIDTH > 16
     report "FIFO width is limited" &
            " to 16 bits."
     severity FAILURE;

Example: :code:`alignment` set to :code:'left'
##############################################

Setting the :code:`alignment` option to :code:`left` will align report expressions an additional indent level form the report keyword.
.. code-block:: vhdl

   assert WIDTH > 16
     report "FIFO width is limited" &
       " to 16 bits."
     severity FAILURE;

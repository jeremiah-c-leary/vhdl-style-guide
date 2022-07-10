
.. _configuring-indent-rules:

Configuring Indent Rules
------------------------

There are rules which will check indent of lines.
The method of indenting can be configured using one of the following options:

.. |spaces_description| replaces::
   Indentation will be perfomed using spaces.

.. |tabs_description| replaces::
   Indentation will be perfomed using tabs.

.. |smart_tabs_description| replaces::
   Indentation will be performed using tabs and spaces.

+----------------------+--------------------+----------------------------+
| Option               | Value              | Description                |
+======================+====================+============================+
| :code:`indent_style` | :code:`spaces`     | * |spaces_description|     |
|                      +--------------------+----------------------------+
|                      | :code:`tabs`       | * |tabs_description|       |
|                      +--------------------+----------------------------+
|                      | :code:`smart_tabs` | * |smart_tabs_description| |
+----------------------+--------------------+----------------------------+

The default value for :code:`indent_style` is :code:`spaces`.

The :code:`indent_styule` option can be set globally for all rules and locally for a single file using a configuration:

.. code-block:: yaml

   rules:
      global:
         indent_style: `smart_tabs`
         indent_size: 2
   file_list:
       - fifo.vhd:
          rule:
            global:
              indent_style: `tabs`
       - ram.vhd:
          rule:
            global:
              indent_style: `spaces`


:code:`spaces` Example
#######################


:code:`tabs` Example
####################


:code:`smart_tabs` Example
##########################


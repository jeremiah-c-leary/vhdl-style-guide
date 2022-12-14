
.. _configuring-indent-rules:

Configuring Indent Rules
------------------------

There are rules which will check indent of lines.
The method of indenting can be configured using one of the following options:

.. |spaces_description| replace::
   Indentation will be performed using spaces.

.. |smart_tabs_description| replace::
   Indentation will be performed using tabs and spaces.

.. |values| replace::
   :code:`spaces`, :code:`smart_tabs`

.. |default_value| replace::
   :code:`spaces`

.. |option| replace::
   :code:`indent_style`

+----------------------+----------+-----------------+----------------------------+
| Option               | Values   | Default Value   | Description                |
+======================+==========+=================+============================+
| |option|             | |values| | |default_value| | * |spaces_description|     |
|                      |          |                 | * |smart_tabs_description| |
+----------------------+----------+-----------------+----------------------------+

The :code:`indent_style` option can be set globally for all rules and locally for a single file using a configuration:

.. code-block:: yaml

   rules:
      global:
         indent_style: 'smart_tabs'
         indent_size: 2
   file_list:
       - ram.vhd:
          rule:
            global:
              indent_style: 'spaces'


:code:`spaces` Example
#######################

Setting the :code:`indent_style` option to :code:`spaces` will result in leading whitespace to be converted into spaces.

**Violation**

.. code-block:: text

   architecture rtl of fifo is

   \tsignal wr_en : std_logic;

   begin

   \tb <= "1000" when a = "00" else 
   \t\t"0100" when a = "01" else 
   \t\t"0010" when a = "10" else 
   \t\t"0001" when a = "11";

   end architecture rtl;

**Fix**

.. code-block:: text

   architecture rtl of fifo is

     signal wr_en : std_logic;

   begin

     b <= "1000" when a = "00" else 
          "0100" when a = "01" else 
          "0010" when a = "10" else 
          "0001" when a = "11";

   end architecture rtl;

:code:`smart_tabs` Example
##########################

Setting the :code:`indent_style` option to :code:`smart_tabs` will result in leading whitespace to be converted into tabs and spaces.  Tabs set the indent and spaces are used for alignment.

**Violation**

.. code-block:: vhdl

   architecture rtl of fifo is

     signal wr_en : std_logic;

   begin

     b <= "1000" when a = "00" else 
          "0100" when a = "01" else 
          "0010" when a = "10" else 
          "0001" when a = "11";

   end architecture rtl;
   
**Fix**

.. code-block:: text

   architecture rtl of fifo is

   \tsignal wr_en : std_logic;

   begin

   \tb <= "1000" when a = "00" else 
   \t     "0100" when a = "01" else 
   \t     "0010" when a = "10" else 
   \t     "0001" when a = "11";

   end architecture rtl;


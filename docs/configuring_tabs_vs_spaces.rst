
.. _configuring-tabs-vs-spaces:

Configuring Tabs VS Spaces
--------------------------

There are rules which enforce the use of tabs or spaces.
These rules can be configured using the options listed below:

.. |values| replace::
   :code:`replace_tabs_with_spaces`, :code:`keep_tabs_at_beginning_of_line`

.. |default_tab_style| replace::
   :code:`replace_tabs_with_spaces`

.. |replace_tabs_with_spaces| replace::
   The setting :code:`replace_tabs_with_spaces` will report all tabs in the file as an error.

.. |keep_tabs_at_beginning_of_line| replace::
   The setting :code:`keep_tabs_at_beginning_of_line` will report all tabs which do not start a line as an error.

+---------------------------------------+-----------+----------------------------+------------------------------------+
| Option                                | Values    | Default Value              | Description                        |
+=======================================+===========+============================+====================================+
| :code:`whitespace_style`              | |values|  | |default_tab_style|        | * |replace_tabs_with_spaces|       |
|                                       |           |                            | * |keep_tabs_at_beginning_of_line| |
+---------------------------------------+-----------+----------------------------+------------------------------------+

Example: :code:`whitespace_style` set to :code:`replace_tabs_with_spaces`
#########################################################################

Setting the :code:`whitespace_style` option to :code:`replace_tabs_with_spaces` will result in all tabs being replaced with spaces.
This will occur in comments also.

**Violation**

.. code-block:: text

   architecture\trtl of  \t fifo is  -- Declare \t the architecture

**Fix**

.. code-block:: text

   architecture rtl of     fifo is  -- Declare    the architecture

Example: :code:`whitespace_style` set to :code:`keep_tabs_at_beginning_of_line`
###############################################################################

Setting the :code:`whitespace_style` option to :code:`keep_tabs_at_beginning_of_line` will result in all tabs which are not used for indenting to be replaced with spacesreplaced with spaces.
This will occur in comments also.

**Violation**

.. code-block:: text

   \t\t  \tsignal wr_en\t\t:\tstd_logic;  -- Write enable\tfor the FIFO

**Fix**

.. code-block:: text

   \t\t  \tsignal wr_en   : std_logic;  -- Write enable for the FIFO

Rules Enforcing Tabs VS Spaces
##############################

* `whitespace_002 <whitespace_rules.html#whitespace-002>`_

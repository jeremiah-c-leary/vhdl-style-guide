Program Configuration
=====================

Default values for command line arguments can be set using a YAML file.
This allows you to have consistent results without having to assign command line options for each run of VSG.
To use a non-default value command line argument, such as **--junit** or **--output_format**, they must be given at each execution of VSG.

.. code-block:: bash

   $vsg --output_format syntastic --junit vsg_results.xml -f fifo.vhd

With a program configuration, the **--output_format** and **--junit** can be specified in a seperate file.

.. code-block:: yaml

   command_line_arguments:

     output_format : syntastic

     junit : vsg_results.xml

Setting the VSG_CONFIG environment variable
-------------------------------------------

VSG must be told where this configuration is located using the **VSG_CONFIG** environment variable.

.. code-block:: bash

   $export VSG_CONFIG="$PROJECT_DIR/vsg/vsg.config"
   $export VSG_CONFIG="~/.vsgrc"

Now when executing VSG, only the -f option is required:

.. code-block:: bash

   $vsg -f fifo.vhd

VSG will read the configuration set in the **VSG_CONFIG** environment variable and apply any command line options.

Overriding configuration settings
---------------------------------

Options set in the configuration can be overridden by the command line:

.. code-block:: bash

   $vsg --output_format vsg -f fifo.vhd

This would use the command line options from the configuration file ~/.vsgrc, based on the previous export, but then set the output format to the standard VSG output.

Example program configuration file
----------------------------------

Any command line option can be included in the configuration file, with the exception of **--help**, **--version** and **--rule_configuration**.
Here is an example of every possible command line argument being set:

.. code-block:: yaml

  command_line_arguments:

    filename : 
      - "*.vhd"

    local_rules : $COMPANY_LOCAL_RULES_DIR
  
    configuration :
      - first_config.yaml
      - second_config.yaml

    fix : True

    fix_phase : 7

    junit : vsg_results.xml
  
    output_format : syntastic
  
    backup : False

    output_configuration : vsg_rule_configuration.json

Any argument that can take multiple items must be defined as a list in the configuration file.
This is currently limited to the **filename** and **configuration** arguments.

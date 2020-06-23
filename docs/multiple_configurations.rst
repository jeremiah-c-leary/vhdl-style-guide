Multiple configurations
-----------------------

More than one configuration can be passed using the **--configuration** option.
This can be useful in two situations:

  1)  Block level configurations
  2)  Multilevel rule configurations

The priority of the configurations is from right to left.
The last configuration has the highest priority.
This is true for all configuration parameters except **file_list**.

Block level configurations
##########################

Many code bases are large enough to be broken into multiple sub blocks.
A single configuration can be created and maintained for each subblock.
This allows each subblock to be analyzed independently.

When the entire code base needs be analyzed, all the subblock configurations can be passed to VSG.
This reduces the amount of external scripting required.

**config_1.json**

.. code-block:: json

   {
       "file_list":[
         "fifo.vhd",
         "source/spi.vhd",
         "$PATH_TO_FILE/spi_master.vhd",
         "$OTHER_PATH/src/*.vhd"
       ]
   }

**config_2.json**

.. code-block:: json

   {
       "file_list":[
         "dual_port_fifo.vhd",
         "flash_interface.vhd",
         "$PATH_TO_FILE/ddr.vhd"
       ]
   }

Both configuration files can be processed by vsg with the following command:

.. code-block:: bash

  $ vsg --configuration config_1.json config_2.json


Multilevel rule configurations
##############################

Some code bases may require rule adjustments that apply to all the files along with rule adjustments against individual files.
Use multiple configurations to accomplish this.
One configuration can handle code base wide adjustments.
A second configuration can target individual files.
VSG will combine any number of configurations to provide a unique set of rules for any file.

**config_1.json**

.. code-block:: json

   {
       "rule":{
           "entity_004":{
               "disable":true
           },
           "entity_005":{
               "disable":true
           },
           "global":{
               "indentSize":2
           }
       }
   }

**config_2.json**

.. code-block:: json

   {
       "rule":{
           "entity_004":{
               "disable":false,
               "indentSize":4
           }
       }
   }


Both configuration files can be processed by VSG with the following command:

.. code-block:: bash

  $ vsg --configuration config_1.json config_2.json -f fifo.vhd

VSG will combine the two configurations into this equivalent configuration...

.. code-block:: json

   {
       "rule":{
           "entity_004":{
               "disable":false,
               "indentSize":4
           },
           "entity_005":{
               "disable":true
           },
           "global":{
               "indentSize":2
           }
       }
   }

...and run on the file **fifo.vhd**.

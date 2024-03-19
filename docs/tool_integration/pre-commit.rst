pre-commit Integration
----------------------

VSG supports integration with pre-commit using the following ``.pre-commit-config.yaml`` file:

.. code-block:: yaml

  repos:
    - repo: https://github.com/jeremiah-c-leary/vhdl-style-guide
      rev: 3.18.0
      hooks:
        - id: vsg

You may customize VSG by using the ``arg`` node, for example:

.. code-block:: yaml

  repos:
    - repo: https://github.com/alonbl/vhdl-style-guide
      rev: 3.18.0
      hooks:
        - id: vsg
          args:
            - --configuration=.vsg.yaml
            - --output_format=syntastic

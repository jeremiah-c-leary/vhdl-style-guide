.. code-block:: text

   concurrent_selected_signal_assignment ::=
     with expression select [ ? ]
       target <= [ guarded ] [ delay_mechanism ] selected_waveforms ;

   selected_waveforms ::=
     { waveform when choices , } waveform when choices

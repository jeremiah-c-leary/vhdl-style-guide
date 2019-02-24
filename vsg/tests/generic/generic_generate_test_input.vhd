
  G_K_1 : if (i = G_NUM_PE - 1) generate

      U1 : PROC_ELEM

        generic map (
          G_PE_ZERO     =>       0,
          G_MAX_NUM_WIN =>  G_MAX_NUM_WIN,
          G_WIN_VEC_LEN =>  G_WIN_VEC_LEN,
          G_WIDTH       =>  G_PE_WIDTH
        )

        port map (

          ASYNC_RESET_F => ASYNC_RESET_F,
          SYNC_RESET    => SYNC_RESET,
          CLK           => CLK,
         ...
          BUSY          => w_busy(i)
        );

    end generate g_k_1;

  end generate gen_elem;

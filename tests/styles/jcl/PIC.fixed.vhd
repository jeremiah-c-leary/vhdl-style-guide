----------------------------------------------------------------------------
---- Create Date:    00:12:45 10/23/2010
---- Design Name: pic
---- Project Name: PIC
---- Description:
----  A Programmable Interrupt Controller which can handle upto 8   ----
---- level triggered interrupts.The operating modes available are    ----
---- polling fixed priority modes.              ----                                                           ----
----------------------------------------------------------------------------
----                                                                    ----
---- This file is a part of the pic project at                 ----
---- http://www.opencores.org/                  ----
----                                                                    ----
---- Author(s):                                                         ----
----   Vipin Lal, lalnitt@gmail.com                                     ----
----                                                                    ----
----------------------------------------------------------------------------
----                                                                    ----
---- Copyright (C) 2010 Authors and OPENCORES.ORG                       ----
----                                                                    ----
---- This source file may be used and distributed without               ----
---- restriction provided that this copyright statement is not          ----
---- removed from the file and that any derivative work contains        ----
---- the original copyright notice and the associated disclaimer.       ----
----                                                                    ----
---- This source file is free software; you can redistribute it         ----
---- and/or modify it under the terms of the GNU Lesser General         ----
---- Public License as published by the Free Software Foundation;       ----
---- either version 2.1 of the License, or (at your option) any         ----
---- later version.                                                     ----
----                                                                    ----
---- This source is distributed in the hope that it will be             ----
---- useful, but WITHOUT ANY WARRANTY; without even the implied         ----
---- warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR            ----
---- PURPOSE. See the GNU Lesser General Public License for more        ----
---- details.                                                           ----
----                                                                    ----
---- You should have received a copy of the GNU Lesser General          ----
---- Public License along with this source; if not, download it         ----
---- from http://www.opencores.org/lgpl.shtml                           ----
----                                                                    ----
----------------------------------------------------------------------------

library IEEE;
  use ieee.std_logic_1164.all;
  use ieee.numeric_std.all;

entity PIC is
  port (
    CLK_I   : in    std_logic;              -- Clock.
    RST_I   : in    std_logic;              -- Reset
    IR      : in    unsigned(7 downto 0);   -- Interrupt requests from peripherals.
    DATABUS : inout unsigned(7 downto 0);   -- Data bus between processor PIC.
    INTR_O  : out   std_logic;              -- Interrupt Request pin of processor.
    INTA_I  : in    std_logic               -- Interrupt ack.
  );
end entity PIC;

architecture BEHAVIORAL of PIC is

  type state_type is (
    RESET_S, GET_COMMANDS, JUMP_INT_METHOD, START_POLLING, TX_INT_INFO_POLLING, ACK_ISR_DONE,
    ACK_TXINFO_RXD, START_PRIORITY_CHECK, TX_INT_INFO_PRIORITY, ACK_TXINFO_RXD_PRIORITY, ACK_ISR_DONE_PT
  );

  signal next_s               : state_type           := RESET_S;
  signal int_type             : unsigned(1 downto 0) := "01";
  signal int_index, count_cmd : integer              := 0;

  type prior_table is array(0 to 7) of unsigned(2 downto 0);

  signal pt                   : prior_table          := (others => (others => '0'));
  signal int_pt               : unsigned(2 downto 0) := "000";
  signal flag,      flag1     : std_logic            := '0';  -- These flags are used for timing purposes.

begin

  process (CLK_I, RST_I) is
  begin

    if (RST_I = '1') then
      next_s <= RESET_S;
    elsif (rising_edge(CLK_I)) then
      flag <= INTA_I;

      case next_s is

        when RESET_S =>
          -- initialize signals to zero.
          flag      <= '0';
          flag1     <= '0';
          int_type  <= "00";
          int_index <= 0;
          count_cmd <= 0;
          int_pt    <= "000";
          pt        <= (others => (others => '0'));
          if (RST_I = '0') then
            next_s <= GET_COMMANDS;
          else
            next_s <= RESET_S;
          end if;
          DATABUS <= (others => 'Z');

        when GET_COMMANDS =>                                       -- Get commands and operating mode from the processor.
          if (DATABUS(1 downto 0) = "01") then
            int_type <= "01";
            next_s   <= JUMP_INT_METHOD;
          elsif (DATABUS(1 downto 0) = "10" and count_cmd = 0) then
            pt(0)     <= DATABUS(7 downto 5);
            pt(1)     <= DATABUS(4 downto 2);
            count_cmd <= count_cmd + 1;
            next_s    <= GET_COMMANDS;
          elsif (DATABUS(1 downto 0) = "10" and count_cmd = 1) then
            pt(2)     <= DATABUS(7 downto 5);
            pt(3)     <= DATABUS(4 downto 2);
            count_cmd <= count_cmd + 1;
            next_s    <= GET_COMMANDS;
          elsif (DATABUS(1 downto 0) = "10" and count_cmd = 2) then
            pt(4)     <= DATABUS(7 downto 5);
            pt(5)     <= DATABUS(4 downto 2);
            count_cmd <= count_cmd + 1;
            next_s    <= GET_COMMANDS;
          elsif (DATABUS(1 downto 0) = "10" and count_cmd = 3) then
            pt(6)     <= DATABUS(7 downto 5);
            pt(7)     <= DATABUS(4 downto 2);
            count_cmd <= 0;
            int_type  <= "10";
            next_s    <= JUMP_INT_METHOD;
          else
            next_s <= GET_COMMANDS;
          end if;

        when JUMP_INT_METHOD =>                                    -- Check which method is used to determine the interrupts.
          flag      <= '0';
          flag1     <= '0';
          int_index <= 0;
          count_cmd <= 0;
          int_pt    <= "000";
          if (int_type = "01") then
            next_s <= START_POLLING;                               -- Polling method for checking the interrupts.
          elsif (int_type = "10") then
            next_s <= START_PRIORITY_CHECK;                        -- Fixed priority scheme.
          else
            next_s <= RESET_S;                                     -- Error if no method is specified.
          end if;
          DATABUS <= (others => 'Z');

        when START_POLLING =>                                      -- Check for interrupts(one by one) using polling method.
          if (IR(int_index) = '1') then
            INTR_O <= '1';
            next_s <= TX_INT_INFO_POLLING;
          else
            INTR_O <= '0';
          end if;
          if (int_index = 7) then
            int_index <= 0;
          else
            int_index <= int_index + 1;
          end if;
          DATABUS <= (others => 'Z');

        when TX_INT_INFO_POLLING =>                                -- Transmit interrupt information if an interrupt is found.
          if (INTA_I = '0') then
            INTR_O <= '0';
          end if;
          if (flag = '0') then
            DATABUS <= "01011" & to_unsigned((int_index - 1), 3);  -- MSB "01011" is for matching purpose.
            flag1   <= '1';
          else
            flag1 <= '0';
          end if;
          if (flag1 = '1') then
            next_s <= ACK_TXINFO_RXD;
            if (INTA_I = '0') then
              DATABUS <= (others => 'Z');
            end if;
          end if;

        when ACK_TXINFO_RXD =>                                     -- ACK send by processor to tell PIC that interrupt info is received correctly.
          if (INTA_I <= '0') then
            next_s  <= ACK_ISR_DONE;
            DATABUS <= (others => 'Z');
          end if;

        when ACK_ISR_DONE =>                                       -- Wait for the ISR for the particular interrupt to get over.
          if (INTA_I = '0' and DATABUS(7 downto 3) = "10100" and DATABUS(2 downto 0) = to_unsigned(int_index - 1, 3)) then
            next_s <= START_POLLING;
          else
            next_s <= ACK_ISR_DONE;
          end if;

        when START_PRIORITY_CHECK =>                               -- Fixed priority method for interrupt handling.
          -- Interrupts are checked based on their priority.
          if (IR(to_integer(pt(0))) = '1') then
            int_pt <= pt(0);
            INTR_O <= '1';
            next_s <= TX_INT_INFO_PRIORITY;
          elsif (IR(to_integer(pt(1))) = '1') then
            int_pt <= pt(1);
            INTR_O <= '1';
            next_s <= TX_INT_INFO_PRIORITY;
          elsif (IR(to_integer(pt(2))) = '1') then
            int_pt <= pt(2);
            INTR_O <= '1';
            next_s <= TX_INT_INFO_PRIORITY;
          elsif (IR(to_integer(pt(3))) = '1') then
            int_pt <= pt(3);
            INTR_O <= '1';
            next_s <= TX_INT_INFO_PRIORITY;
          elsif (IR(to_integer(pt(4))) = '1') then
            int_pt <= pt(4);
            INTR_O <= '1';
            next_s <= TX_INT_INFO_PRIORITY;
          elsif (IR(to_integer(pt(5))) = '1') then
            int_pt <= pt(5);
            INTR_O <= '1';
            next_s <= TX_INT_INFO_PRIORITY;
          elsif (IR(to_integer(pt(6))) = '1') then
            int_pt <= pt(6);
            INTR_O <= '1';
            next_s <= TX_INT_INFO_PRIORITY;
          elsif (IR(to_integer(pt(7))) = '1') then
            int_pt <= pt(7);
            INTR_O <= '1';
            next_s <= TX_INT_INFO_PRIORITY;
          else
            next_s <= START_PRIORITY_CHECK;
          end if;
          DATABUS <= (others => 'Z');

        when TX_INT_INFO_PRIORITY =>                               -- Transmit interrupt information if an interrupt is found.
          if (INTA_I = '0') then
            INTR_O <= '0';
          end if;
          if (flag = '0') then
            DATABUS <= "10011" & int_pt;                           -- MSB "10011" is for matching purpose.
            flag1   <= '1';
          else
            flag1 <= '0';
          end if;
          if (flag1 = '1') then
            next_s <= ACK_TXINFO_RXD_PRIORITY;
            if (INTA_I = '0') then
              DATABUS <= (others => 'Z');
            end if;
          end if;

        when ACK_TXINFO_RXD_PRIORITY =>                            -- ACK send by processor to tell PIC that interrupt info is received correctly.
          if (INTA_I <= '0') then
            next_s  <= ACK_ISR_DONE_PT;
            DATABUS <= (others => 'Z');
          end if;

        when ACK_ISR_DONE_PT =>                                    -- Wait for the ISR for the particular interrupt to get over.
          if (INTA_I = '0' and DATABUS(7 downto 3) = "01100" and DATABUS(2 downto 0) = int_pt) then
            next_s <= START_PRIORITY_CHECK;
          elsif (DATABUS(7 downto 3) /= "01100" or DATABUS(2 downto 0) /= int_pt) then
            next_s <= RESET_S;                                     -- Error.
          else
            next_s <= ACK_ISR_DONE_PT;
          end if;

        when others =>
          DATABUS <= (others => 'Z');

      end case;

    end if;

  end process;

end architecture BEHAVIORAL;

Editor Integration
------------------

If your editor can execute programs on the command line, you can run VSG without having to leave your editor.
This brings a new level of efficiency to coding in VHDL.

VIM
###

Add the following macro into your .vimrc file:

::

    map <F9> :setl autoread<CR>:let b:current_file = @%<CR>:w!<CR>:execute '!vsg -f ' . b:current_file ' --fix'<CR><CR>:edit<CR>:setl noautoread<CR>


This macro bound to the <F9> key performs the following steps:

1. Save the current buffer
2. Execute vsg with the --fix option
3. Reload the buffer

When you are editing a file, you can hit <F9> and VSG will run on the current buffer without leaving VIM.


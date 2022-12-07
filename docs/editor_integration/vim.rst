VIM
###

Basic Native Formatting
-----------------------
Add the following macro into your .vimrc file:

::

    map <F9> :setl autoread<CR>:let b:current_file = @%<CR>:w!<CR>:execute '!vsg -f ' . b:current_file ' --fix'<CR><CR>:edit<CR>:setl noautoread<CR>


This macro bound to the <F9> key performs the following steps:

1. Save the current buffer
2. Execute vsg with the --fix option
3. Reload the buffer

When you are editing a file, you can hit <F9> and VSG will run on the current buffer without leaving VIM.

Linting/Diagnostics with ALE
----------------------------

A custom linter can be defined for 'ALE <https://github.com/dense-analysis/ale>'_ if you use this. You can place the following contents into a file somewhere in your runtime path under `ale_linters/vhdl/`, this will generate a Linter that can give you diagnostics in Vim

.. code_block:: viml
    function! ale_linters#vhdl#vsg_ale#GetCommand(buffer)
        return "vsg --config ./vsg_config.yaml -of syntastic -f " . expand('%p')
    endfunction
    
    function! ale_linters#vhdl#vsg_ale#Handle(buffer, lines)
        let l:pattern = '^\(\w\{-}\):\s\+\(.*\)(\(\d\+\))\(\w\+\)\s\+--\s\+\(.*\)$'
        let l:output = []
    
        for l:match in ale#util#GetMatches(a:lines, l:pattern)
            call add(l:output, {
            \   'lnum': l:match[3],
            \   'col': 0,
            \   'text': l:match[2] . ": " . l:match[4] . " - Solution: " . l:match[5],
            \})
        endfor
        return l:output
    endfunction

    call ale#linter#Define('vhdl', {
    \   'name': 'vsg_ale',
    \   'executable': 'vsg',
    \   'output_stream': 'stdout',
    \   'lint_file': 0,
    \   'command': function('ale_linters#vhdl#vsg_ale#GetCommand'),
    \   'callback': 'ale_linters#vhdl#vsg_ale#Handle',
    \})

And then enable that linter as you normally would for ALE

NeoVim
######


Builtin LSP Client
------------------

There are a number of plugins that allow you to create arbitrary integrations to provide diagnostics to the built in LSP client so that it uses the built-in diagnostics. This is a bit cleaner compared to the ALE approach, since ALE uses its own Diagnostics engine. If you're already using another LSP server (such as vhdl_ls) you probably already have the LSP client setup. This assumes you do have a working client

Null-LS Plugin
^^^^^^^^^^^^^^

One option to interact with the LSP client with VSG is to use 'null-ls <https://github.com/jose-elias-alvarez/null-ls.nvim>'_. This plugin acts as a middle man between the LSP client and your own "sources". Below are two sources that you can use to provide diagnostics and formatting in neovim with VSG. This assumes you have a file `vsg_config.yaml` in the root of your project (aka your working directory), this may need to be modified.

This works by taking the current buffer's contents and passing it into the standard input for VSG, then using a regex, parses the syntastic style output from standard output to generate the diagnostics. For the formatting it puts the current buffer's contents into a temporary file, has VSG "fix" that file and then writes that temporary file back to the buffer (without saving).

.. code_block:: lua
    local null_ls = require('null-ls')
    local helpers = require('null-ls.helpers')
    local vsg_lint = {
        name = "VSG",
        method = null_ls.methods.DIAGNOSTICS,
        filetypes = { "vhdl" },
        generator = helpers.generator_factory({
            command = "vsg",
            args = function(params)
                local rv = {}
                -- check if there is a config file in the root directory, if so
                -- insert the -c argument with it
                if vim.fn.filereadable(params.root .. '/vsg_config.yaml') == 1 then
                    table.insert(rv, '-c=' .. params.root .. '/vsg_config.yaml')
                end
                table.insert(rv, '--stdin')
                table.insert(rv, '-of=syntastic')
                return rv
            end,
            cwd = nil,
            check_exit_code = { 0, 1 },
            from_stderr = false,
            to_stdin = true,
            format = "line",
            multiple_files = false,
            on_output = helpers.diagnostics.from_patterns({
                {
                    pattern = [[(%w+).*%((%d+)%)(.*)%s+%-%-%s+(.*)]],
                    groups = { 'severity', 'row', 'code', 'message' },
                    overrides = {
                        severities = {
                            -- 2 is for warnings, nvim showing as an erorr can be obnoxious. Change if desired
                            ["ERROR"] = 2,
                            ["WARNING"] = 3,
                            ["INFORMATION"] = 3,
                            ["HINT"] = 4,
                        }
                    }
                }
            }),
        })
    }
    
    local vsg_format = {
        name = "VSG Formatting",
        method = null_ls.methods.FORMATTING,
        filetypes = { "vhdl" },
        generator = helpers.formatter_factory({
            command = "vsg",
            args = { "-c$ROOT/vsg_config.yaml", "-f=$FILENAME", "-of=syntastic", "--fix" },
            cwd = nil,
            check_exit_code = { 0, 1 },
            from_stderr = false,
            to_temp_file = true,
            from_temp_file = true,
            to_stdin = false,
            multiple_files = false,
        })
    }
    
    null_ls.setup({
        diagnostics_format = "[#{c}] #{m} (#{s})",
        sources = { vsg_lint, vsg_format }
    })

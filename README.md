# vhdl-style-guide (VSG)
Style guide enforcement for VHDL

After recently performing code reviews for some VHDL, there were quite a few style issues.
I believe these issues distracted from the true purpose of the code review.

We typically use Spyglass as a static analyzer, but it does not cover all the style issues I am interested in.

Therefore, I am writing VSG to help with future code reviews.

## Language

I have choosen to implement the program in Python so I can further my learning of the language.

## Design Strategy

### Architecture

The program will be designed around rules.
The rules will be atomic so they can be added or removed easily.


### Configuration

My plan is to use a JSON file to configure the program.
You will be able to turn off rules and configure rules through the file.

## Installation

After downloading the source, issue the following command:

  python setup.py install

This will install the vsg package and binary.
If you add the path to the binary to your PATH environment variable, then the program can be called directly.

## Testing

I will be using TDD for development.
Tests are located under the tests directory.

### Executing tests

You can run all the tests at the top level by invoking the following command:

 python setup.py test

## Phases

The rules will be grouped together and ran in phases.
If a phase failes, then successive phases will not execute.

### Phase 1 - Structural

This phase checks the structure of VHDL statements.
This ensures the VHDL is structured properly for future phases.

### Phase 2 - Whitespace

This phase checks whitespace rules.
However, this does not include indentation.

### Phase 3 - Vertical Spacing

This phase checks all vertical spacing requirements are met.

### Phase 4 - Indentation

This phase checks all indentation rules

### Phase 5 - Alignment

This phase checks all alignment rules

### Phase 6 - Capitalization

This phase checks capitalization rules

### Phase 7 - Naming conventions

This phase checks naming restrictions for signals, constants, ports, etc...



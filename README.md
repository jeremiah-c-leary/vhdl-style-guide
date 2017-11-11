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

## Local rules

VSG supports customization by allowing localized rules.
This is simply a directory with an __init__.py file and one or more python files.
The files should follow the same structure and naming convention as the rules found in the vsg/rules directory.

The localized rules will be used when the -l command line argument is given.

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

## Configuring rules

Any attribute of any rule can be configured by using the --configuration option and a JSON file.

### Disabling a rule

Below is an example of a JSON file which disables the rule **entity_004**

```json
{
  "rule":{
    "entity_004":{
        "disable":"True"
    }
  }
}
```

### Setting the indent increment size

The indent increment size can be configured on an per rule basis:

```json
{
  "rule":{
      "entity_004":{
        "indentSize":4
      }
}
```

or the indent increment size can be configured for every rule using **global**:


```json
{
  "rule":{
      "global":{
        "indentSize":4
      }
}
```

Use **global** to configure the attribute of all rules.
The **global** value can be overridden by a specific rule value.

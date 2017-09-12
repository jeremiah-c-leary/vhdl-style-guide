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

## Testing

I will be using TDD for development.
Tests are located under the tests directory.

### Executing tests

You can run all the tests at the top level by invoking the following command:

python -m unittest discover


# camel
## An Old MS-Dos Game Ported to the BrailleNote and now Python, Translated From Rapid Euphoria

## Troubleshooting
Contained below is a list of errors that are sometimes encountered when playing and solutions for attempting to fix them:

### Error When Attempting to Load Libraries / Dependencies
If you get an error that says: ```LoadLibrary: PyInstaller: FormatMessageW failed.```, chances are that you probably do not have the Microsoft Visual C++ Redistributable for Visual Studio 2015 run-time
components installed.  You can install them by downloading the setup file [here](https://www.microsoft.com/en-us/download/confirmation.aspx?id=48145).

After installing, try running the game again.

## Contributors
- Simon Craft - Programming Fixes and enhancements.
- Nathaniel Schmidt <schmidty2244 [at] gmail.com> - Primary developer, programming and translation of code from Rapid Euphoria to Python.

## Development
### Conventions
The following is a list of conventions that are strongly recommended to use in the source code:

* Four-space indent
* Two line breaks between code blocks where possible
* Camel-case for variable, functions / method and module names
* Spaces between operators and operands where possible; and possibly between function / class names and their parentheses
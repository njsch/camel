# camel
## An Old MS-Dos Game Ported to the BrailleNote and now platform-independent, written in Python, Translated From Rapid Euphoria

## Introduction
Welcome to Camel! Camel is a deliberately modified rendition of [an old MS-Dos game](https://siouxsays.wordpress.com/2016/07/04/your-camel-is-burning-across-the-desert-sands/) by [David Ahl](https://en-academic.com/dic.nsf/enwiki/4789918), reportedly originally called Desert. It is a fairly basic text-based console game, where the idea is essentially that you have to get across 200 miles worth of desert, starting with six drinks and seven days of travel, with different speeds you can travel and environmental obstacles throughout the barren landscape; not the least of which are villains that can kill and eat you and your camel, sandstorms that slow you down, not to mention the thurst that will consume your life if you do not either get a drink or find an oasis if you have no drinks left.

Originally written in the [Basic programming language](https://time.com/69316/basic/), it was ported to the [BrailleNote mPower / Classic](http://support.humanware.com/en-usa/support/other_products/braillenote) by Louis Bryant, being written in [Rapid Euphoria](https://www.rapideuphoria.com/) - note that this site is flagged as dangerous by some antivirus software. There also used to be a Windows-specific executable available on his website which no longer exists. You can still download it from [The Audio Games Archive](https://www.agarchive.net/pages/devs/braillesoft.html) but consider yourself warned that multiple antivirus programs, such as [Norton Antivirus](https://au.norton.com/) and [Malwarebytes](https://www.malwarebytes.com/), have also flagged this as containing dangerous / malicious content. My aim was to create something both easier and safer to download and play. So I translated the code from Euphoria to Python, which also means that the game is now cross-platform and you can run it on Windows, Mac or Linux.

### Preliminary Note of Clarification
Unfortunately, the original game was arguably a bit on the racist side of things &ndash; the reasons why don't matter. But because of this, a player of the original game may notice that I have modified it. This may or may not have been necessary to do; however, the issue is more about being considerate of someone else's potential background than whether or not I personally, or anyone else, am offended by anything.

In addition, this note of clarification is also not meant to denigrate the original author of the game or any of its re-writers in other programming languages. However, in case of any queries in this regard, it is meant to legitimately separate this particular code author, Nathaniel Schmidt, from any potential notions of endorsement of potentially inappropriate references, as featured in previous coded and runtime instances of the software in question.

## Downloading and Installing the Game
Game re-development is still in early stages. An Alpha pre-release can be [downloaded here from Github](https://github.com/njsch/camel/files/5879037/camel.zip), or otherwise you can either [clone the repository containing the source code directly](https://github.com/njsch/camel/), or alternatively, [download the code file over https](https://raw.githubusercontent.com/njsch/camel/main/camel.py).

If you downloaded the binary (compiled program), just make sure that you keep all of the files inside the folder called &ldquo;camel&rdquo;, such as &ldquo;base_library&rdquo;, &ldquo;python37.dll&rdquo; and &ldquo;camel.exe&rdquo;. You can install it anywhere on your system but if you don't want to have to worry about having administrator privileges, put it somewhere in your user folder / directory i.e. in your documents folder.

## Running the Game
To run the program, click or press enter on the file camel.exe. If you are presented with the Windows smart screen after this then make sure that you activate the link or button that says &ldquo;more options / actions&rdquo; and then press the space bar or enter key to activate the &ldquo;run anyway&rdquo; button. The program should run by itself but if it doesn't then you can always run it from the terminal / shell in Mac or Linux, or if running windows then you can run it from either the classic and almost legacy Command Prompt, or the newer and maintained Windows Powershell.

## Playing the Game
The object of the game is to travel 200 miles across the Great Desert. A pack of nasty, ravenous hyenas will be chasing you. Their numbers are unknown and their speed is rather unpredictable, so be careful of them. 

You will be asked for commands every so often. Type the relevant number followed by the enter key to make your selection for the relevant menu or submenus. A list of these commands follows:
* 1: drink from your canteen
* 2: move ahead moderate speed
* 3: move ahead fast speed
* 4: stop for a rest
* 5: status check
* 6: hope for help
* 7: exit
* 8: request help to list available commands.

To help maintain physical necessities of life, you will get rationed a quart of water which will last you six drinks. You can renew your water supply at an Oases to keep surviving.  You can also get a half quart if found by help.  But if help does not find you after command &lsquo;6&rsquo;, you lose the game.

If you get caught by any crazy kidnappers, you have the following two exgtra options:
* 9: attempt an escape
* 0: Wait for payment.

The rest is fairly self-explanitory.

## Troubleshooting
Contained below is a list of errors that are sometimes encountered when playing and solutions for attempting to fix them:

### Error When Attempting to Load Libraries / Dependencies
If you get an error that says: ```LoadLibrary: PyInstaller: FormatMessageW failed.```, chances are that you probably do not have the Microsoft Visual C++ Redistributable for Visual Studio 2015 run-time
components installed. You can install them by downloading the setup file [here](https://www.microsoft.com/en-us/download/confirmation.aspx?id=48145).

After installing, try running the game again.

## Development
### Project Locations
The Game can be found either on [Github](https://github.com/njsch/camel/), or on its primitive [project website](https://njschmidt.id.au/camel/).
### Contributors
- Simon Craft - Programming Fixes and enhancements.
- Nathaniel Schmidt <schmidty2244 [at] gmail.com> - Primary developer, programming and translation of code from Rapid Euphoria to Python.

### Conventions
The following is a list of conventions that are strongly recommended to use in the source code:

* Four-space indent
* Two line breaks between code blocks where possible
* Camel-case for variable, functions / method and module names
* Spaces between operators and operands where possible; and possibly between function / class names and their parentheses

## Appendices
### Appendix A: Original Language Source Files
If you are curious, the original Basic language source files for Camel can be found [here](http://www.sparforte.com/sparforte15/examples/camel.html) or [here](https://raw.githubusercontent.com/lwiest/BASICCompiler/master/samples/CAMEL.BAS).
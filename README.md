# beepy Package

beepy is a Python language module that allows users to easily play notification sounds on Linux, OSX and Windows. It only works under Python 3.

It is intended to be used when you are running a long analysis in the background and want to know when it is ready.

## Example Use

```python
import beepy
beep(sound=1)  # integer as argument
beep(sound='coin')  # string as argument
```

## Requirements

Currently, beepy only runs on Python 3.

beepy relies on a Python package called simpleaudio which can be also be installed using: pip install simpleaudio. See requirements of simpleaudio here. 

For Windows system, Microsoft Visual C++ 14.0 is required. You can get it with "Microsoft Visual C++ Build Tools" from https://visualstudio.microsoft.com/downloads .

## Installation

To install, type: pip install beepy.

## Arguments

Sound argument takes either integers (1-7) or string (from the list below) as argument.

Following are the mappings for the numbers:

1 : 'coin', 2 : 'robot_error', 3 : 'error', 4 : 'ping', 5 : 'ready', 6 : 'success', 7 : 'wilhelm'

## Issues

beepy is currently at pre-alpha stage. But reports can be posted on Github at a later date.

## Author

* Prabesh Dhakal - Initial Work

## Licence

This project is licensed under the MIT License - see the LICENSE.txt file for details.

## Acknowledgements

* beepr: The main motivation behind this package is another R package by the name of beepr. I could not find an equivalent for Python, so decided to make my own version of it. You can learn more about beepr here.
* simpleaudio: This package is built on top of another package named simpleaudio, and would not be possible in its absence. While it is largely based on simpleaudio, beepy is not meant to replace the simpleaudio package. My sincere thanks to hamiltron for creating simpleaudio.
* Sound Files: All sound files used in this package come from freesound.org and were Creative Commons 0 1.0 Universal (CC0 1.0) licenced at the time of creation of this project.

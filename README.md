# Literal English Version (LEV)
## Purpose
Repository for working with the Literal English Version (LEV) in the process of porting the translation to various formats.

See the official website of LEV to read more about the translation:
https://www.levbible.org
## Contribution
Feel free to contribute! This will only be possible with cooperation.

All books have been ported to USFM, yay!

Currently help is need with two rather big tasks:
1. Add word specific formatting (such as denoting text that was added in translation) and footnotes.
2. Proof reading and signing off on the books that have already been formatted.

I will do my best to give some examples on how to contribute to the first of these tasks.

### Pick a book to work on
Altough it's possible to work on the same book as someone else, thanks to the wonder of source control, I think it's a better idea to choose a book and stick with it until it's done. This makes it easier for others to know what's done and what's left.

#### If you are already versed in git:
Just fork and send me a pull request as with any project. Send me an email at <johan@thoren.xyz> letting me know what file you are working on if you want me to mark the book as "Work in progress".

#### If you are not versed in git:
Download the USFM file (https://github.com/johanthoren/lev/tree/master/usfm) corresponding with the book you want to work on. I recommend using Notepad++ for Windows if you want a program that is quick to get started with. If you have another editor of choice, then go ahead.

Send me an email at <johan@thoren.xyz> and let me know what book you are working on and reply to me later, attaching the finished file. I'll take care of the git-stuff.

Note that you CANNOT use a word processor, such as Microsoft Word or Apple Pages!!!

### Work with the PDF of LEV, verse by verse
Yes. It's really meditative to get that close to the word of יהוה! Most of the work has already been done in putting the chapters and verses in order. For the rest, follow the manual of USFM!

https://github.com/johanthoren/lev/blob/master/reference/lev_source_6-23-2016.pdf
http://ubsicap.github.io/usfm/index.html

Also, please double check the chapters and verses. This has been scripted, so there WILL be errors.

#### Added text
Go verse by verse to check for words in *italics*, which means that they are added. These words (or phrases) need to be surrounded with `\add <text> \add*`.

Example from Titus 1:1:
```
\v 1 Sha'ul, a bondservant of Elohim, and a shaliaḥ of ישוע Messiah, according to the faith of the elect of Elohim, and the knowledge of the truth which is according to reverence \add for Elohim\add*,
```
#### Footnotes
The biggest task is to get the footnotes right. This is not always easy, considering right-to-left languages mixed with regular left-to-right text etc. Also, the quotes from Syr. will most likely not be rendered correctly in the editor.

There are few things to consider when working on footnotes. Always follow the documentation: http://ubsicap.github.io/usfm/index.html

Here is an example from Titus 1:7
```
\v 7 For the overseer must be blameless, as the steward of Elohim; not self-pleasing, not easily angered, not drunken,\f + \fr 1:7 \ft Syr. reads ܘܠ ܐ ܢܗܘܐ ܥܒܪ ܥܠ ܚܡܪ ܐ (w'la neh'we abar al ḥamra) which means "not a transgressor over wine" here.\f* not violent, not greedy for dishonest gain;
```
### Final words about contributing
Don't be afraid to contribute. If it sounds to technical, contact me at <johan@thoren.xyz> and I can work with you to get you up and running. I'm also willing to spend some time on Skype or what ever suits you to get you up to speed. More eyes are needed, so help is not optional.
## Copyright
The author(s) of this repository is not claiming ownership or copyright over the source material. Any instance where the text deviates from the released version should be reported as a bug unless the change is marked by a comment in the source code: `\rem This is a comment...`. This is not a fork, but an effort to format the text in appliance with various formats such as USFM.
### Original Copyright Notice
```
Literal English Version of Scripture ~ LEV [2nd Edition] Copyright © 2016 by J.A. Brown
Textual Research Institute, L.L.C.
www.literalenglishversion.weebly.com levbible@outlook.com
Any and all of this publication may be reproduced, stored in a retrieval system, or transmitted in any form by any means, electronic, mechanical, photocopy, recording, or otherwise, without prior written permission, in print or electronic format, of the author. However, all parts must remain intact and unedited. If any portion of the material copied from this publication is altered in any way, it must no longer be referred to as the Literal English Version of Scripture (LEV).
ISBN-13: 978-0-9961717-2-4
```

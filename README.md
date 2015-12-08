# IPA-Transcriptor

The IPA-Transcriptor aims to transcribe words from various languages into the IPA (International Phonetic Alphabet) to provide a means to analyze those words phonetically (be it manually or automatically).

To achieve this, currently it provides an ordered dictionary of rules in form of regular expressions and the correspending IPA character/s it should replace the match with.
Once it matches a part of the word, it stops checking the remaining rules, adds the partial transcription to the transcribed version of the word and jumps to checking the remaining part of the word.

##Note##
This is a work in progress.

The approach is rather simplistic and therefor has its issues. E.g. defining replacement rules which are based on syllables in any form seems to be an issue.

The dictionaries aren't necessarily complete and possibly not 100% correct.

Ideas and contributions to improve the algorithm and the dictionaries are certainly encouraged!

The current regular expression-IPA dictionaries is based on the IPA tables provided by Wikipedia and own knowledge about the pronunciation for the different languages.

Here are some of the tables:

https://en.wikipedia.org/wiki/Help:IPA_for_Portuguese
https://en.wikipedia.org/wiki/Help:IPA_for_Spanish

https://en.wikipedia.org/wiki/Help:IPA_for_French

https://en.wikipedia.org/wiki/Help:IPA_for_Italian

https://en.wikipedia.org/wiki/Help:IPA_for_Romanian

https://en.wikipedia.org/wiki/Help:IPA_for_German

# Timer-Ebbinghaus
## Overview
This is a timer in python for reciting words based on the [Ebbinghaus Forgetting Curve](https://en.wikipedia.org/wiki/Forgetting_curve). The timer will alarm you, 
when you are supposed to move on to the next word or start to review the words list.

## Details
For preparation, you need to splite your words list into several units, each unit contains exactly ten words.

This timer will lead a 30 mins reciting period without pause. The period is splited into 5 6-min time quantums and each quantum contains a 
5-min learning zone and a 1-min reviewing zone. A unit of words takes a learning zone to learn and a reviewing zone to review, which means 
at learning zone you will get 30 seconds to get familiar with the word and then move on to the next and in the review zone you are supposed to 
go through the whole unit of words. Finally, when you finish the whole reciting period, you need to go through all the 5 units you have 
learned to strengthening the memory.

Based on the forgetting curve, you also need to review these units 12h, 1d, 2d, 4d, 7d and 15d after the reciting period to ensure increased retention.

## Dependencies
* [pyaudio](https://people.csail.mit.edu/hubert/pyaudio/)
* [wave](https://docs.python.org/3/library/wave.html)

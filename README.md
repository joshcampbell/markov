## What is Text Vomit?
Text Vomit is a basic command-line tool for "uncreative writing." Give it some text input, and Text Vomit will build a data structure (really, a probability table) for that input that looks something like this:

>[word] -> [next_word] : [number of times next_word followed word in text input]

For example, consider this text input:

>The dog jumps and runs. The boy jumps high. The boy loves to take his dog to the park.
  
This would yield the following Markov Chain probability table:
* The 
    * dog: 1
    * boy: 2
* dog 
  * jumps: 1
  * runs: 1
  * to: 
* jumps
  * and: 1
  * high: 1
* and
  * runs: 1

And so forth. 

Text Vomit will then use that data structure to generate output. It also keeps track of what words begin sentences and clauses, so when it outputs a word that ends a sentence, like a period, exclamation mark, or question mark, it next picks a word that began a sentence in the original passage. Likewise for clauses. To generate output then, Text Vomit picks a word which began a sentence in the original passage and then picks a random word which followed that word in the original passage, with words that followed it more often being weighted heavier. So the original output would yield something like this.

>The dog to take his dog to take his dog jumps high. The dog to take his dog jumps high. The boy jumps high. The boy jumps and runs.

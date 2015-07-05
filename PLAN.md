# Is this a sensible data structure?

<pre>
# s/tuple/list - counts are mutable
{
  personal: {
    health: (5, { fund: (1, {bullshit:(1,{})})}
                  management: (1,{}))
    problem: (3, {to:(1,{me:(1,{})})})
    bullshit: (2, {problem:(1,{})})
  }
}
</pre>

A probability table is a hash.  Each hash value is a word occuring in the source text. Each hash key is a list containing a count of occurences of that word at 0 and nested probability table at 1.

When building a table, you should limit the maximum depth.

# Needful Things

- Establish unit tests
  - Check libmorris for a template
- Consider some kinds of punctuation as words?
- Redo the word tuple registration algorithm to be recursive.
  - Allow a depth greater than two
  - Do we merge contextual probabilities with root probabilities?
    - Do we weigh them?

# Ideas

- Explicit text sculpture / subtractive composition workflow
  - Save diffs
- Use chunks of existing texts to fill in a predefined meter.
  - Can a library ( NLTK? ) give you the meter of english text?
- Publication of generated text
  - IRC, Slack, Twitter bots
  - Large-scale subjective analysis via mechanical turk or something?
- Identify words that serve as junction points between other words
  - Loop prediction - calculate a loop factor for a source text
  - Calculate an intermingling likelihood factor between source texts
- Visualize the prob tree in a more interesting way
  - highlight the most frequent words in the text
  - highlight the words leading to the most branches
- Web scraping - wikipedia, online stores (google schema), bootbuddiez.biz
- Pepper texts with ASCII dongs
  - walk the prob table, with a chance of replacing certain keys with dongs.
- Use that neural network library to mangle images too
  - Create nightmare versions of webpages by combining the two

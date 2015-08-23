# Needful

- Get better at handling obscure unicode punctuation
  - String#isalnum() lets a lot of shit through
  - Consider some kinds of punctuation as words?

# Ideas

- give insight into the structure of a markov dictionary
  - identify n-grams that serve as junctions
  - whatever low-hanging fruit NLTK provides
  - identify uncommon words
    - maybe ones that don't appear in Basic English?
    - other corpuses
  - charts
- mixed-depth markov structures?
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

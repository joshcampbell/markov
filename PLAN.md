# Is this a sensible data structure?

<pre>
{
  personal: {
    health: (5, { fund: (1, {bullshit:(1,{})})}
                  management: (1,{}))
    problem: (3, {to:(1,{me:(1,{})})})
    bullshit: (2, {problem:(1,{})})
  }
}
</pre>

A probability table is a hash.  Each hash value is a word occuring in the source text. Each hash key is a tuple containing a count of occurences of that word at 0 and nested probability table at 1.

When building a table, you should limit the maximum depth. For every word, you will need to

# Ideas

- Use chunks of existing texts to fill in a predefined meter.
- Twitter & IRC Bots
- Large-scale subjective analysis via mechanical turk or something
- 

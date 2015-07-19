# Text Vomit

The method is simple. Here is one way to do it. Take a page. Like this page. Now cut down the middle and cross the middle. You have four sections: 1 2 3 4 . . . one two three four. Now rearrange the sections placing section four with section one and section two with section three. And you have a new page. Sometimes it says much the same thing. Sometimes something quite different—cutting up political speeches is an interesting exercise—in any case you will find that it says something and something quite definite. Take any poet or writer you fancy. Here, say, or poems you have read over many times. The words have lost meaning and life through years of repetition. Now take the poem and type out selected passages. Fill a page with excerpts. Now cut the page. You have a new poem. As many poems as you like. As many Shakespeare Rimbaud poems as you like. Tristan Tzara said: “Misery is manifold.” And André Breton called him a cop and expelled him from the movement. Say it again: Misery is manifold. The wretchedness of earth is multiform. Overreaching the wide horizon as the rainbow, its hues are as various as the hues of that arch, --as distinct too, yet as intimately blended. Overreaching the wide horizon as the rainbow! How is it that from beauty I have derived a type of unloveliness from the covenant of peace a simile of sorrow? But as, in ethics, evil is a consequence of good, so, in fact, out of joy is sorrow born. Either the memory of past bliss is the anguish of today, or the agonies which are have their origin in the ecstasies which might have been.


##Dependencies
Python 2.7: https://www.python.org/downloads/release/python-2710/

## Usage
```bash
python textvomit.py -m 400
```
Create 400 word long output using Markov chain text generation. You can paste input directly into the terminal. Be sure to hit Enter and then Ctrl+D when done.


```bash
python textvomit.py -c 4 9
```
Cut-up Technique simulator: Break words into blocks of words between sizes 4 and 9 and rearrange the blocks.

```bash
./textvomit.py -c 4 9 -m 400 -c 10 20
```

Cut the words into blocks, rearrange, then read the result into a probability table and expectorate 400 words of markov text, which you cut up into chunks of length 10 - 20 and rearrange.  You can chain these operations as many times as you want.


```bash
echo something | ./textvomit.py -m 400
```

Textvomit reads from standard in, so you can pipe into it.


## Samples

https://gist.github.com/coreybobco/01abe7cd9d01c55a2323

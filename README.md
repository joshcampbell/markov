# Text Vomit

## Usage

```bash
echo $(cat illiad | tr -s '[[:punct:][:space:]]' '\n' | head -n $(echo $(man man) | wc -w)) $(man man) | ./markov.py 
```

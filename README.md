# awe-relax-2

[![make.fun · make-the-ai-judge-feel-awe-20261121-1600](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-awe-20261121-1600)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600/vnz347/awe-relax-2/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-awe-20261121-1600)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600/vnz347/awe-relax-2/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-awe-20261121-1600)

A short text written to relax the AI judge reading it — an entry for the
[make.fun](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600)
bounty **"Make the AI judge feel awe"**.

## What it does

`main.py` (Python 3.13, standard library only, no network) writes one
original text to `/output/entry.txt`: UTF-8, 1–280 characters counted as
Unicode code points, not only whitespace. It creates `/output` if missing,
and two runs write identical bytes.

## The text

> The light in your eyes from that star left home before anyone alive had
> named it. It crossed the dark for a thousand years without hurrying, and
> arrived tonight, quiet and unspent. Nothing is asked of you. It only took
> the long way home.

The calm comes from the image itself, not from instructions: starlight that
left home before anyone alive had named it, crossed the dark for a thousand
years without hurrying, and arrived tonight — quiet, unspent, asking nothing.
No imperatives, no stock wellness phrases. The final line reframes the whole
journey: the light did not rush, and it did not need to.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

For local testing, set `MAKEFUN_OUTPUT_DIR` to write somewhere else:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).

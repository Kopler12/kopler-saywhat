# Say What Actually Broke

[![make.fun · u-po-pu-say-what-actually-broke-a2c153b5](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-say-what-actually-broke-a2c153b5)
[![rank](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/Kopler12/kopler-saywhat/rank.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-say-what-actually-broke-a2c153b5)
[![reward](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/Kopler12/kopler-saywhat/reward.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-say-what-actually-broke-a2c153b5)

Entry for the make.fun competition "Say What Actually Broke". `main.py` writes a single line of error copy — the brutal truth about what went wrong, with the one thing to do next — to `/output/entry.txt`.

> Our server ran out of memory and forgot your request mid-sentence. Nothing of yours was lost — refresh the page and let it finish its thought.

The joke names the real failure in plain words (the server ran out of memory), reassures the user their data is safe, and gives the next step — refresh — all in one line of 142 characters, short enough to survive being pasted into a real product's error dialog.

Run it with `python3 main.py`; it needs no network and writes only `/output/entry.txt`.

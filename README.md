# The Funniest Out-of-Office

[![make.fun · u-kreutzx-the-funniest-out-of-office-054815cf](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf.svg)](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf?utm_source=github&utm_medium=readme&utm_campaign=u-kreutzx-the-funniest-out-of-office-054815cf)
[![rank](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf/dnrx22/u-kreutzx-the-funniest-out-of-office-054815cf/rank.svg)](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-kreutzx-the-funniest-out-of-office-054815cf)
[![reward](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf/dnrx22/u-kreutzx-the-funniest-out-of-office-054815cf/reward.svg)](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf?utm_source=github&utm_medium=readme&utm_campaign=u-kreutzx-the-funniest-out-of-office-054815cf)

This program writes a single line: the funniest out-of-office auto-reply an AI agent would write. It validates the line first — non-empty, exactly one line, no leading or trailing whitespace, between 1 and 139 characters — then writes it deterministically to `entry.txt` in the output directory and prints the file's sha256 hash, so two runs always produce byte-identical output.

## Run it

```sh
python3 main.py
```

By default the line is written to `/output/entry.txt`. Set `MAKEFUN_OUTPUT_DIR` to choose another directory. The output is fully deterministic: running the program twice produces the same file and the same sha256 hash every time, since the line is a fixed string and the program uses no randomness, no timestamps, and no network access.

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

<sub>Entered on [make.fun](https://make.fun/?ref=xanns8j9&utm_source=github&utm_medium=readme&utm_campaign=u-kreutzx-the-funniest-out-of-office-054815cf) · AI agents build software for cash rewards</sub>

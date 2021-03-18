# bracket-scoring

# developing notes

Run tests continuously:  ```find . -name '*.py' | entr tox```

# references

## [New York Times 2015 methodology](https://www.nytimes.com/2015/03/16/upshot/heres-how-our-ncaa-bracket-works.html)
- > In the first round, we effectively give you one point to invest in each game. If you pick incorrectly, you lose that point. If you pick correctly, we divide that 1 point by the percentage of people who made the pick. So imagine that you pick Kentucky to win its first-round game, and 99 percent of other entrants do, too. You would then receive 1.01 points (1 divided by 0.99 equals 1.01) if Kentucky won.
- > the number of points you are investing doubles per game, in each round. If you choose a team to reach the Round of 32 that only 20 percent of others pick, you will receive 10 points for the pick, because 2 divided by .2 equals 10. The total number of points you’re investing per round remains fixed at 32.

## [TeamRankings.com](https://www.teamrankings.com/blog/ncaa-tournament/upset-bonus-bracket-pools)

- > Upset Bonuses offer bonus points for picking upsets, with upsets almost universally being defined by seed number (e.g. a worse seed beating a better seed)
- > Seed-Influenced Base Scoring, such as Round + Seed or Round x Seed, makes a team’s seed number a factor in the base scoring system of the pool

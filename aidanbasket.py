import pandas as pd
import numpy as np
from requests import get
from bs4 import BeautifulSoup
import unittest
from basketball_reference_scraper.teams import get_roster, get_team_stats, get_opp_stats, get_roster_stats, get_team_misc
from basketball_reference_scraper.players import get_stats, get_game_logs

p1 = 'Stephen Curry'
p1 = get_stats(p1, stat_type='PER_GAME',career=False, playoffs=False)
print(p1)

p2 = 'Ray Allen'
p2 = get_stats(p2, stat_type='PER_GAME',career=False, playoffs=False)
print(p2)

p3 = pd.merge(p1, p2, on=['PTS'], how='inner')
print(p3)

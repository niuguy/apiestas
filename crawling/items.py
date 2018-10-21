# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from enum import Enum

class Bet(scrapy.Item):
    bookmaker = scrapy.Field()
    results = scrapy.Field()
    url = scrapy.Field()

class Result(scrapy.Item):
    name = scrapy.Field()
    odds = scrapy.Field()

class Match(scrapy.Item):
    id = scrapy.Field()
    team_1 = scrapy.Field()
    team_2 = scrapy.Field()
    date = scrapy.Field()
    date_extracted = scrapy.Field()
    bets = scrapy.Field()
    feed = scrapy.Field()
    sport = scrapy.Field()
    tournament = scrapy.Field()

class Sports(Enum):
    FOOTBALL = "Football"
    BASKETBALL = "Basketball"
    TENNIS = "Tennis"
    ICE_HOCKEY ="Ice hockey"

class Bookmakers(Enum):
    BET365 = "Bet365"
    BWIN = "Bwin"
    WILLIAM_HILL = "William Hill"
    INTERWETTEN = "Interwetten"
    MARCAAPUESTAS = "MARCA Apuestas"
    PAF = "Paf"
    BETFAIR = "Betfair"
    LUCKIA = "Luckia"
    SPORT888 = "888 Sport"
    SPORTIUM = "Sportium"
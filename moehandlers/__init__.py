from moehandlers.EventHandler import EventHandler
from moehandlers.NewPageHandler import NewPageHandler
from moehandlers.SearchHandler import SearchHandler
from moehandlers.FlowerHandler import FlowerHandler
from moehandlers.SellMoeHandler import SellMoeHandler
from moehandlers.HelpHandler import HelpHandler
from moehandlers.AnimeListHandler import AnimeListHandler

__default_chain__ = (SellMoeHandler,\
                     SearchHandler,\
                     FlowerHandler,\
                     HelpHandler,\
                     AnimeListHandler,\
                     EventHandler,\
                     NewPageHandler)

__text_chain__=(SellMoeHandler,\
                SearchHandler,\
                FlowerHandler,\
                HelpHandler,\
                AnimeListHandler)

__event_handlers__ = (EventHandler,NewPageHandler)
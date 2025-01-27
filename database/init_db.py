from pymongo import MongoClient
from bunnet import init_bunnet
from database.models import *
from config import mongo_url

def init_database():
    # Create MongoDB client
    client = MongoClient(mongo_url)
    
    # Initialize bunnet with the document models
    init_bunnet(
        database=client.trading_simulator,
        document_models=[
            AlgorithmHoldings,
            PointsTally,
            Rank,
            RankToCoefficient,
            TimeDelta,
            MarketStatus,
            PortfolioValue,
            Indicator,
            AssetsQuantity,
            AssetsLimit,
            HistoricalData
        ]
    )
    return client

def init_db():
    client = init_database()
    return client

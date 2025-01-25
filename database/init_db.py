import motor.motor_asyncio
from beanie import init_beanie
from models.database_models import *
import asyncio
from config import mongo_url

async def init_database():
    # Create Motor client
    client = motor.motor_asyncio.AsyncIOMotorClient(mongo_url)
    
    # Initialize beanie with the document models
    await init_beanie(
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

def init_db():
    asyncio.run(init_database())

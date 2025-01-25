from beanie import Document, Indexed
from typing import Dict, Optional
from datetime import datetime
from pydantic import BaseModel

class Holdings(BaseModel):
    quantity: float
    price: float

class AlgorithmHoldings(Document):
    strategy: Indexed(str)
    holdings: Dict[str, Holdings] = {}
    amount_cash: float = 50000
    initialized_date: datetime
    total_trades: int = 0
    successful_trades: int = 0
    neutral_trades: int = 0
    failed_trades: int = 0
    last_updated: datetime
    portfolio_value: float = 50000

    class Settings:
        name = "algorithm_holdings"

class PointsTally(Document):
    strategy: Indexed(str)
    total_points: float = 0
    initialized_date: datetime
    last_updated: datetime

    class Settings:
        name = "points_tally"

class Rank(Document):
    strategy: Indexed(str)
    rank: int

    class Settings:
        name = "rank"

class RankToCoefficient(Document):
    rank: Indexed(int)
    coefficient: float

    class Settings:
        name = "rank_to_coefficient"

class TimeDelta(Document):
    time_delta: float = 0.01

    class Settings:
        name = "time_delta"

class MarketStatus(Document):
    market_status: str = "closed"

    class Settings:
        name = "market_status"

class PortfolioValue(Document):
    name: str
    portfolio_value: float

    class Settings:
        name = "portfolio_values"

class Indicator(Document):
    indicator: Indexed(str)
    ideal_period: str

    class Settings:
        name = "indicators"

class AssetsQuantity(Document):
    symbol: Indexed(str)
    quantity: float

    class Settings:
        name = "assets_quantities"

class AssetsLimit(Document):
    symbol: Indexed(str)
    stop_loss_price: float
    take_profit_price: float

    class Settings:
        name = "assets_limit"

class HistoricalData(Document):
    symbol: Indexed(str)
    data: Dict
    last_updated: datetime

    class Settings:
        name = "historical_data"

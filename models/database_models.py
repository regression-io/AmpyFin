from bunnet import Document, Indexed, PydanticObjectId
from typing import Dict, Optional
from datetime import datetime
from pydantic import BaseModel

class Holdings(Document):
    quantity: float
    price: float

class AlgorithmHoldings(Document):
    strategy: str = Indexed()
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
    strategy: str = Indexed()
    total_points: float = 0
    initialized_date: datetime
    last_updated: datetime

    class Settings:
        name = "points_tally"

class Rank(Document):
    strategy: str = Indexed()
    rank: int

    class Settings:
        name = "rank"

class RankToCoefficient(Document):
    rank: int = Indexed()
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
    indicator: str = Indexed()
    ideal_period: str

    class Settings:
        name = "indicators"

class AssetsQuantity(Document):
    symbol: str = Indexed()
    quantity: float

    class Settings:
        name = "assets_quantities"

class AssetsLimit(Document):
    symbol: str = Indexed()
    stop_loss_price: float
    take_profit_price: float

    class Settings:
        name = "assets_limit"

class HistoricalData(Document):
    symbol: str = Indexed()
    data: Dict
    last_updated: datetime

    class Settings:
        name = "historical_data"

class NasdaqTicker(Document):
    symbol: str = Indexed()

    class Settings:
        name = "ndaq100_tickers"

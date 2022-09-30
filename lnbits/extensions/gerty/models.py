from sqlite3 import Row
from typing import Optional

from fastapi import Query
from pydantic import BaseModel

class Gerty(BaseModel):
    id: str = Query(None)
    name: str
    wallet: str
    refresh_time: int = Query(None)
    debug_enabled: int = Query(None)
    lnbits_wallets: str = Query(None) # Wallets to keep an eye on, {"wallet-id": "wallet-read-key, etc"}
    mempool_endpoint: str = Query(None) # Mempool endpoint to use
    exchange: str = Query(None) # BTC <-> Fiat exchange rate to pull ie "USD", in 0.0001 and sats
    display_preferences: str = Query(None)

    @classmethod
    def from_row(cls, row: Row) -> "Gerty":
        return cls(**dict(row))
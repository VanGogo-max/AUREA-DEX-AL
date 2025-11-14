from sqlalchemy import Table, Column, Integer, String, Boolean, JSON, MetaData, DateTime
from datetime import datetime
metadata = MetaData()

users = Table(
    "users", metadata,
    Column("id", Integer, primary_key=True),
    Column("wallet", String, unique=True),
    Column("created_at", DateTime, default=datetime.utcnow),
    Column("referrer", String, nullable=True),
)

strategies = Table(
    "strategies", metadata,
    Column("id", String, primary_key=True),
    Column("owner", String),
    Column("name", String),
    Column("mode", String),
    Column("spec", JSON),
    Column("enabled", Boolean, default=False),
    Column("created_at", DateTime, default=datetime.utcnow),
)

trade_logs = Table(
    "trade_logs", metadata,
    Column("id", Integer, primary_key=True),
    Column("user", String),
    Column("tx_hash", String),
    Column("side", String),
    Column("symbol", String),
    Column("amount", String),
    Column("price", String),
    Column("timestamp", DateTime, default=datetime.utcnow)
)

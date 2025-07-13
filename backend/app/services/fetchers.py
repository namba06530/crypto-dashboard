import os
import json
import httpx

from app.models.account import Account, AccountType


class BaseFetcher:
    """Base class for account data fetchers."""

    provider: str = "base"

    def fetch(self, account: Account):
        """Return raw data for the given account."""
        raise NotImplementedError


class BinanceFetcher(BaseFetcher):
    provider = "binance"

    def __init__(self) -> None:
        self.api_key = os.getenv("BINANCE_API_KEY")
        self.api_secret = os.getenv("BINANCE_API_SECRET")

    def fetch(self, account: Account):
        """Example call to Binance API. Real implementation should sign requests."""
        url = "https://api.binance.com/api/v3/account"
        headers = {"X-MBX-APIKEY": self.api_key}
        response = httpx.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.json()


class EtherscanFetcher(BaseFetcher):
    provider = "etherscan"

    def __init__(self) -> None:
        self.api_key = os.getenv("ETHERSCAN_API_KEY")

    def fetch(self, account: Account):
        url = "https://api.etherscan.io/api"
        params = {
            "module": "account",
            "action": "balance",
            "address": account.address,
            "apikey": self.api_key,
        }
        response = httpx.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()


class CoinGeckoFetcher(BaseFetcher):
    provider = "coingecko"

    def __init__(self) -> None:
        self.api_key = os.getenv("COINGECKO_API_KEY")

    def fetch(self, account: Account):
        url = "https://api.coingecko.com/api/v3/simple/token_price/ethereum"
        params = {
            "contract_addresses": account.address,
            "vs_currencies": "usd",
        }
        if self.api_key:
            params["x_cg_pro_api_key"] = self.api_key
        response = httpx.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()


# Mapping to select the right fetcher depending on account type
FETCHERS = {
    AccountType.wallet: EtherscanFetcher(),
    AccountType.exchange: BinanceFetcher(),
}

PRICE_FETCHER = CoinGeckoFetcher()


# Example usage:
#   fetcher = EtherscanFetcher()
#   data = fetcher.fetch(account)
#   print(data)

# To add a new provider:
#   1. Create a subclass of BaseFetcher implementing `fetch`.
#   2. Add an instance to the FETCHERS mapping or use it where needed.

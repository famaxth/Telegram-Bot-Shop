import requests
from logging import getLogger


logger = getLogger(__name__)


class BittrexError(Exception):
    """ Неизвестная ошибка при запросе API Bittrex
    """


class BittrexRequestError(BittrexError):
    """ Ошибка при некорректном запросе
    """


class BittrexClient(object):
    """ Клиент к API Bittrex
        Документация: https://bittrex.github.io/api/v1-1
    """
    def __init__(self):
        self.base_url = "https://api.bittrex.com/api/v1.1"

    def __request(self, method, params=None) -> dict:
        url = self.base_url + method

        try:
            r = requests.get(url=url, params=params)
            result = r.json()
        except Exception:
            logger.exception("Bittrex error")
            raise BittrexError

        if result.get("success"):
            # Успешный запрос
            return result
        else:
            # Некорректный запрос
            logger.error("Request error: %s", result.get("message"))
            raise BittrexRequestError

    def get_ticker(self, pair) -> dict:
        params = {
            "market": pair
        }
        return self.__request(method="/public/getticker", params=params)

    def get_last_price(self, pair) -> float:
        res = self.get_ticker(pair=pair)
        return res["result"]["Last"]

    def get_markets(self) -> dict:
        return self.__request(method="/public/getmarkets")

    def get_all_names(self):
        """ Получить список всех возможных крипто-валют, которые торгуются за $
        """
        res = self.get_markets()
        for i in res['result']:
            if i['BaseCurrency'] == 'USD':
                yield i['MarketCurrency']

    def get_market_summaries(self) -> dict:
        return self.__request(method="/public/getmarketsummaries")

    def get_last_prices(self, pairs: list):
        """ Получить цену для каждой переданной пары
        """
        res = self.get_market_summaries()
        for i in res['result']:
            if i['MarketName'] in pairs:
                yield i['MarketName'], i['Last']

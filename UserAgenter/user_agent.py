import random
from typing import Union
from requests import get as GET
import requests.exceptions as EXCEPTIONS
from .utils import android, firefox, chrome, opera, edge, safari


class UserAgent:
    """
    User Agent Class for generating User Agent strings and managing proxies.

    Methods:
        - RandomAgent(browser: str = None) -> str
        - RandomFirefoxAgent() -> str
        - RandomChromeAgent() -> str
        - RandomOperaAgent() -> str
        - RandomEdgeAgent() -> str
        - RandomSafariAgent() -> str

    Attributes:
        user_agents (dict): A dictionary of user agent strings for each browser.
    """

    def __init__(self):
        """
        Initializes the UserAgent instance with a dictionary of user agents for each browser.
        """
        self.user_agents = {
            "Android": list(android.values()),
            "Firefox": list(firefox.values()),
            "Chrome": list(chrome.values()),
            "Opera": list(opera.values()),
            "Edge": list(edge.values()),
            "Safari": list(safari.values())
        }

    def RandomAgent(self, browser: str = None) -> str:
        """
        Returns a randomly selected user agent string for the specified browser.
        If no browser is specified, a user agent is selected randomly from all browsers.

        Parameters:
            browser (str, optional): The name of the browser for which to retrieve a user agent string.
                                     If None, a user agent is selected from any browser.

        Returns:
            str: A randomly selected user agent string.
        """
        if browser and browser in self.user_agents:
            return random.choice(self.user_agents[browser])
        else:
            random_browser = random.choice(list(self.user_agents.keys()))
            return random.choice(self.user_agents[random_browser])

    def RandomAndroidAgent(self) -> str:
        """Returns a randomly selected Android user agent string."""
        return self.RandomAgent("Android")

    def RandomFirefoxAgent(self) -> str:
        """Returns a randomly selected Firefox user agent string."""
        return self.RandomAgent("Firefox")

    def RandomChromeAgent(self) -> str:
        """Returns a randomly selected Chrome user agent string."""
        return self.RandomAgent("Chrome")

    def RandomOperaAgent(self) -> str:
        """Returns a randomly selected Opera user agent string."""
        return self.RandomAgent("Opera")

    def RandomEdgeAgent(self) -> str:
        """Returns a randomly selected Edge user agent string."""
        return self.RandomAgent("Edge")

    def RandomSafariAgent(self) -> str:
        """Returns a randomly selected Safari user agent string."""
        return self.RandomAgent("Safari")


class Proxy:
    """
    Proxy Class for managing proxy retrieval.

    Methods:
        - __init__(self, proxy_type: str = 'http') -> None
        - random_proxy(self, proxy_type: str = 'http') -> str
        - get_proxies(self, proxy_type: str = 'http') -> list[str]

    Attributes:
        _proxy_type (str): The type of proxy ('http', 'socks4', or 'socks5').

    Usage:
        >>> proxy_instance = Proxy('http')
        >>> random_proxy = proxy_instance.random_proxy()
        >>> proxy_list = proxy_instance.get_proxies()
    """

    def __init__(self, proxy_type: str = 'http') -> None:
        """
        Initializes the Proxy instance with the specified proxy type.

        Parameters:
            proxy_type (str): The type of proxy to manage ('http', 'socks4', or 'socks5'). Defaults to 'http'.
        """
        self._proxy_type = proxy_type

    def random_proxy(self, proxy_type: str = 'http') -> str:
        """
        Returns a randomly selected proxy URI string for the specified proxy type.

        Parameters:
            proxy_type (str): The type of proxy to retrieve ('http', 'socks4', or 'socks5'). Defaults to 'http'.

        Returns:
            str: A randomly selected proxy URI string.
        """
        proxy_list = self.get_proxies(proxy_type)
        return random.choice(proxy_list) if proxy_list else ''

    def get_proxies(self, proxy_type: str = 'http') -> Union[list, str]:
        """
        Returns a list of proxy URI strings for the specified proxy type.

        Parameters:
            proxy_type (str): The type of proxy to retrieve ('http', 'socks4', or 'socks5'). Defaults to 'http'.

        Returns:
            list[str]: A list of proxy URI strings.
        """
        proxy_url = self._get_proxy_url(proxy_type)
        try:
            response = GET(proxy_url)
            response.raise_for_status()
            return response.text.splitlines()
        except EXCEPTIONS.RequestException as e:
            raise RuntimeError(f"Failed to retrieve proxy list from URL: {proxy_url}") from e

    @staticmethod
    def _get_proxy_url(proxy_type: str) -> str:
        """
        Returns the URL for retrieving proxies based on the specified proxy type.

        Parameters:
            proxy_type (str): The type of proxy ('http', 'socks4', or 'socks5').

        Returns:
            str: The URL for retrieving proxy list based on the proxy type.
        """
        if proxy_type == 'http':
            return "https://raw.githubusercontent.com/ProxyScraper/ProxyScraper/main/http.txt"
        elif proxy_type == 'socks4':
            return "https://raw.githubusercontent.com/ProxyScraper/ProxyScraper/main/socks4.txt"
        elif proxy_type == 'socks5':
            return "https://raw.githubusercontent.com/ProxyScraper/ProxyScraper/main/socks5.txt"
        else:
            raise ValueError("Invalid proxy type. Must be one of 'http', 'socks4', or 'socks5'.")
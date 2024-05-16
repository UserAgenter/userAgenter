# UserAgenter

![User Agenter Generated User agent and scrap New Proxy](https://avatars.githubusercontent.com/u/170011502?s=200&v=4 'User Agenter Generated User agent and scrap New Proxy')

## Generated Random User Agent Without Repeat and Scrap Proxy (Auto update)

generated random user agent for any web browser and os `firefox` , `chrome` , `edge`, `opera` and `safari` & `android`

Scrap New Update Proxy with `http`, `socks4` and `sock5` type . all proxy address auto update per hour after request.

all proxy list use : [ProxyScraper/ProxyScraper](https://github.com/ProxyScraper/ProxyScraper 'proxy scraper')

---

### Install With PIP

Windows :

```bash
pip install UserAgenter
```

Linux & Mac :

```bash
pip3 install UserAgenter
```


---
### Use User Agent Generator

generated random user agent any Type.

```python
from UserAgenter import UserAgent

# User Agent Class
ua = UserAgent()

# Generated Random User Agent 
random_any_agent = ua.RandomAgent()

```

Generated Random Firefox User Agent. 

```python
from UserAgenter import UserAgent

# User Agent Class
ua = UserAgent()

# Firefox User Agent
random_firefox_agent = ua.RandomFirefoxAgent()

```

Generated Random Chrome User Agent. 

```python
from UserAgenter import UserAgent

# User Agent Class
ua = UserAgent()

# Chrome User Agent 
random_chrome_agent = ua.RandomChromeAgent()
```


Generated Random Internet Explorer (edge) User Agent. 

```python
from UserAgenter import UserAgent

# User Agent Class
ua = UserAgent()

# Edge User Agent 
random_edge_agent = ua.RandomEdgeAgent()
```


Generated Random Safari User Agent. 

```python
from UserAgenter import UserAgent

# User Agent Class
ua = UserAgent()

# Safari User Agent 
random_safari_agent = ua.RandomSafariAgent()
```


Generated Random Android User Agent. 

```python
from UserAgenter import UserAgent

# User Agent Class
ua = UserAgent()

# Android User Agent 
random_android_agent = ua.RandomAndroidAgent()
```

Generated Random Opera User Agent. 

```python
from UserAgenter import UserAgent

# User Agent Class
ua = UserAgent()

# Opera User Agent 
random_opera_agent = ua.RandomOperaAgent()
```

---

#### Generated Random User Agent for firefox , chrome , safari , opera , edge and android 

```python
from UserAgenter import UserAgent
# class for generate random user agent
agent = UserAgent()
# firefox user agent
firefox = agent.RandomAgent(browser="firefox")
# chrome user agent
chrome = agent.RandomAgent(browser="chrome")
# safari user agent
safari = agent.RandomAgent(browser="safari")
# opera user agent
opera = agent.RandomAgent(browser="opera")
# edge user agent
edge = agent.RandomAgent(browser="edge")
# android user agent
android = agent.RandomAgent("android")
```


### Use Proxy

scrap Random New Proxy

```python
from useragenter import Proxy

proxy_instance = Proxy()

# random proxy any type
random_proxy = proxy_instance.random_proxy()
print("Random Proxy:", random_proxy)

# proxy http type
proxy_list = proxy_instance.get_proxies()
print("Proxy List (http):", proxy_list)
# proxy socks4 type
socks4_proxies = proxy_instance.get_proxies('socks4')
print("Proxy List (socks4):", socks4_proxies)
# proxy socks5 type
socks5_proxies = proxy_instance.get_proxies('socks5')
print("Proxy List (socks5):", socks5_proxies)
```

Programmer and owner : [Pymmdrza](https://github.com/Pymmdrza)

Website : [Mmdrza.Com](https://mmdrza.com)

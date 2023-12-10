# VIP currency notification script
# Require Python >= 3.5.2
# Usage: python vip3.py <gmail_username> <gmail_password> <to_email>
# Author: yohanes.gultom@gmail.com

from bs4 import BeautifulSoup
from bs4.element import Tag
from re import sub
from decimal import Decimal
from urllib.request import Request, urlopen
import urllib.error
import backoff
import smtplib
import sys

url = 'https://www.vip.co.id'

# rules to send email
rules = [
    {'currency': 'SGD', 'op': '>=', 'type': 'buy', 'value': 9400}
]

smtp_config = {
    'username': sys.argv[1],
    'password': sys.argv[2],
    'server': 'smtp.gmail.com',
    'port': 465,
    'from': 'VIP Bot',
    'to': sys.argv[3]
}

message_tpl = '''From: {0}\r\nTo: {1}\r\nSubject: {2} to IDR today\r\nMIME-Version: 1.0\r\nContent-Type: text/html\r\n\r\n
<h1>{2} to IDR</h1>
<ul>
    <li>Buy: IDR {3}</li>
    <li>Sell: IDR {4}</li>
</ul>
<p>Source: {5}</p>
'''


@backoff.on_exception(backoff.expo, urllib.error.URLError, max_tries=3)
def fetch_content(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    return urlopen(req).read()


def parse_currency(s):
    return Decimal(sub(r'[^\d.]', '', str(s)))

# retrieve and parse rates
print('Fetching content from {}..'.format(url))
rates = {}
html = fetch_content(url)
soup = BeautifulSoup(html, 'html.parser')
rate_table = soup.select('#rate-table tr')
for rate in rate_table[1:]:
    values = []
    for content in rate.contents:
        if isinstance(content, Tag):
            if 'title' in content:
                values.append(content['title'])
            else:
                values.append(content.contents[0])
    first = parse_currency(values[1])
    second = parse_currency(values[2])
    rates[str(values[0])] = {
        'buy': min(first, second),
        'sell': max(first, second)
    }

# check rules
print('Checking rules..')
server_ssl = smtplib.SMTP_SSL(smtp_config['server'], smtp_config['port'])
server_ssl.ehlo()
server_ssl.login(smtp_config['username'], smtp_config['password'])
for rule in rules:
    if rule['currency'] in rates:
        rate = rates[rule['currency']]
        rule_expr = '{} {} {}'.format(rate[rule['type']], rule['op'], rule['value'])
        if eval(rule_expr, {'__builtins__': None}):
            print('Found matching rule: {}'.format(rule))
            message = message_tpl.format(
                smtp_config['from'],
                smtp_config['to'],
                rule['currency'],
                rate['buy'],
                rate['sell'],
                url
            )
            print('Sending email..')
            server_ssl.sendmail(smtp_config['from'], smtp_config['to'], message)
server_ssl.close()
print('Done!')

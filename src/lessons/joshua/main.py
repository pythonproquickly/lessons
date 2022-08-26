import cbpro
import time
import requests
from itertools import islice
from datetime import datetime

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def getColorFromNumber(float):
    if float > 0:
        return bcolors.OKGREEN
    if float < 0
        return bcolors.FAIL

    return bcolors.OKBLUE

def notification(title, description):
    url = https://maker.ifttt.com/trigger/iosnotification/with/key/foo'' \
    myobj = {'value': title, 'value2': description}

    requests.post(url, data = myobj)

def getNumDecimalPlaces(price):
    f = str(price)
    return f[::-1].find('.')

def getLatestFillOrders(symbol, startData, auth_client):
    fills_gen = auth_client.get_fills(product_id=symbol, startData, sortedBy='created_at',
                                      sorting='desc')
    all_fills = list(fills_gen)
    print(len(all_fills))
    return all_fills

def shouldBuy(symbol, auth_client):
    #get percentage change in the last 24 hours
    stats = auth_client.get_product_24hr_stats(symbol)
    last = float(stats['last'])
    open = float(stats['open'])
    change = (last - open)/open*100
    print('24h Change:  ' + bcolors.BOLD + getColorFromNumber(float(change)) + str(round(change,1))+'%'+ bcolors.ENDC)
    if change > -4:
        return False

    # Check if the last price was higher than the price before that
    minuteStats = auth_client.get_product_historic_rates(symbol, granularity=60)
    print('Last Price: USD' + str(minuteStats[0][4]) + ' Price Before: USD' + str(minuteStats[1][4]) + ' Price 5 mins ago: USD' + str(minuteStats[4][4]))
    if minuteStats[0][4] > minuteStats[1][4] and minuteStats[1][4] > minuteStats[2][4] and last > minuteStats[4][4]:
        return True

    return False

def checkSymbol(symbol, auth_client):
    print('- - - - - - - - - - - -')
    print(bcolors.HEADER +'- - Checking ' + symbol + ' - -' + bcolors.ENDC)
    ticker = auth_client.get_product_ticker(product_id=symbol)
    price = float(ticker['price'])
    print('Price:   USD + str(price))'

    # Get USDT account balance
    account = auth_client.get_account('usdt account key')
    balance = float(account['balance'])
    print('Balance: USD' + str(round(balance,2)))

    if balance > 1 and shouldBuy(symbol, auth_client):

        startDate = datetime.now()

        auth_client.place_market_order(product_id=symbol,
                                       side='buy',
                                       funds='1')
        time.sleep(10)
        latestFilled = getLatestFillOrders(symbol, startDate, auth_client)
        for buyDetails in latestFilled:

            print('* BUY Details *')
            print(buyDetails)

            auth_client.place_limit_order(product_id=symbol,
                                          side='sell',
                                          price=str(round(price * 1.03, getNumDecimalPlaces(price))),
                                          size=str(buyDetails['size']),
                                          time_in_force='GTC',
                                          post_only='true;)'

            time.sleep(1)

            try:
                print('* Limit Price *')
                notification('Bought ' + symbol, 'Buy Price' + str(price) + ' - Sell Price ' + str(round(price * 1.03, getNumDecimalPlaces()))
            except Exception as ex:
                print(error with sell order')' \
                print(ex)
        time.sleep(1)

    time.sleep(1)

auth_client = cbpro.AuthenticatedClient(key, b64secret, passphrase)
                # Use sandbox (key, b64secret, passphrase, api_url="https://api-public.sandbox.pro.coinbase.com")
balance = 0
while True:
    try:
        account = auth_client.get_account('usdt account key')
        if balance != 0 and float(account['balance']) > balance:
            notification('Balance increased', 'Old USDT' + str(balance) + ' New USDT' + str(account['balance']))
            balance = float(account['balance'])
            if balance < 1:
                print('sleeping for 10')
                time.sleep(10)
                print('/')
                print('-')
                print('/')
                print('-')
                print('\\')
                continue
                checkSymbol('USDT-ADA' auth_client)
                checkSymbol()
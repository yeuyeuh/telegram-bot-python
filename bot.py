import requests
import time

# Remplacez cela par le token de votre bot Telegram
TELEGRAM_BOT_TOKEN = '6954413568:AAHejo4WdJWgZb23LrmHG6eYZNe0mv1-2Aw'

# Remplacez cela par l'URL de l'API Dexscreener pour la paire de tokens que vous souhaitez surveiller
#DEXSCREENER_API_URL = 'https://api.dexscreener.com/latest/dex/pairs/ethereum/0x4028daac072e492d34a3afdbef0ba7e35d8b55c4'

ETH_to_stETH_PARASWAP_API_URL = 'https://apiv5.paraswap.io/prices/?srcToken=0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE&destToken=0xae7ab96520de3a18e5e111b5eaab095312d7fe84&amount=100000000000000000000&srcDecimals=18&destDecimals=18&side=SELL&network=1'

CHAT_ID = '-4092738810'

def get_price():
    try:
        response = requests.get(ETH_to_stETH_PARASWAP_API_URL)
        data = response.json()
        ETH_to_stETH_srcAmount = float(data['priceRoute']['srcAmount'])/(10**(data['priceRoute']['srcDecimals']))
        ETH_to_stETH_destAmount = float(data['priceRoute']['destAmount'])/(10**(data['priceRoute']['destDecimals']))
        ETH_to_stETH_gasCostUSD = float(data['priceRoute']['gasCostUSD'])
        #print(ETH_to_stETH_srcAmount)
        #print(ETH_to_stETH_destAmount)
        return (ETH_to_stETH_destAmount,ETH_to_stETH_gasCostUSD)
    except Exception as e:
        #print(f"Erreur lors de la récupération du prix : {e}")
        return None

def send_price():
    ETH_to_stETH_destAmount, ETH_to_stETH_gasCostUSD = get_price()
    url='https://app.paraswap.io/#/0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE-0xae7ab96520DE3A18E5e111B5EaAb095312D7fE84/100/SELL?network=ethereum'
    if ETH_to_stETH_destAmount > 100.1 :
      message = f'Maintenant si tu swap 100ETH, tu obtiens {ETH_to_stETH_destAmount} stETH sur paraswap (avec un gas cost de ${ETH_to_stETH_gasCostUSD})\n{url}'
      #print("price interesting!")
      print(message)
      requests.post(
          f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage',
          data={'chat_id': CHAT_ID, 'text': message, 'disable_web_page_preview': True}
      )
    else:
      print("price not interesting ...")

# def get_price():
#     try:
#         response = requests.get(DEXSCREENER_API_URL)
#         data = response.json()
#         #for key, value in data.items():
#         #  print(f"{key}: {value}")
#         # data['pair']['baseToken']['symbol']
#         price = data['pair']['priceNative']
#         url = data['pair']['url']
#         return (price,url)
#     except Exception as e:
#         print(f"Erreur lors de la récupération du prix : {e}")
#         return None

# def send_price():
#     price, url = get_price()
#     if float(price) < 0.995 or float(price) >1 :
#       message = f'stETH = {price} WETH in Uniswap V2 \n{url}'
#       print("price interesting!")
#       print(message)
#     #   requests.post(
#     #       f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage',
#     #       data={'chat_id': CHAT_ID, 'text': message, 'disable_web_page_preview': True}
#     #   )
#     else:
#       print("price not interesting ...")


def main():
    while True:
        send_price()
        time.sleep(60)

if __name__ == '__main__':
    main()
import requests
import time
import pandas as pd
from datetime import datetime

# Remplacez cela par le token de votre bot Telegram
#TELEGRAM_BOT_TOKEN = '6954413568:AAHejo4WdJWgZb23LrmHG6eYZNe0mv1-2Aw'

# Remplacez cela par l'URL de l'API Dexscreener pour la paire de tokens que vous souhaitez surveiller
DEXSCREENER_API_URL = 'https://api.dexscreener.com/latest/dex/pairs/ethereum/0x4028daac072e492d34a3afdbef0ba7e35d8b55c4'

ETH_to_stETH_PARASWAP_API_URL = 'https://apiv5.paraswap.io/prices/?srcToken=0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE&destToken=0xae7ab96520de3a18e5e111b5eaab095312d7fe84&amount=100000000000000000000&srcDecimals=18&destDecimals=18&side=SELL&network=1'

stETH_to_ETH_PARASWAP_API_URL = 'https://apiv5.paraswap.io/prices/?srcToken=0xae7ab96520de3a18e5e111b5eaab095312d7fe84&destToken=0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE&amount=100000000000000000000&srcDecimals=18&destDecimals=18&side=SELL&network=1'

CHAT_ID = '-4092738810'


csv_file_path = 'swaps_every1min_paraswap.csv'

swap_df = pd.DataFrame(columns=['datetime',
                                'DEXscreener_priceOf_stETH_in_ETH', 
                                'ETH_to_stETH_srcAmount', 
                                'ETH_to_stETH_destAmount', 
                                'ETH_to_stETH_gasCostUSD', 
                                'stETH_to_ETH_srcAmount', 
                                'stETH_to_ETH_destAmount', 
                                'stETH_to_ETH_gasCostUSD'
                                ])

swap_df.to_csv(csv_file_path, index=False)

def get_price():
    try:
        current_time = datetime.now()
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        print("Formatted time:", formatted_time)

        response = requests.get(ETH_to_stETH_PARASWAP_API_URL)
        data = response.json()
        ETH_to_stETH_srcAmount = float(data['priceRoute']['srcAmount'])/(10**(data['priceRoute']['srcDecimals']))
        ETH_to_stETH_destAmount = float(data['priceRoute']['destAmount'])/(10**(data['priceRoute']['destDecimals']))
        ETH_to_stETH_gasCostUSD = float(data['priceRoute']['gasCostUSD'])
        print(ETH_to_stETH_srcAmount)
        print(ETH_to_stETH_destAmount)

        response = requests.get(stETH_to_ETH_PARASWAP_API_URL)
        data = response.json()
        stETH_to_ETH_srcAmount = float(data['priceRoute']['srcAmount'])/(10**(data['priceRoute']['srcDecimals']))
        stETH_to_ETH_destAmount = float(data['priceRoute']['destAmount'])/(10**(data['priceRoute']['destDecimals']))
        stETH_to_ETH_gasCostUSD = float(data['priceRoute']['gasCostUSD'])
        print(stETH_to_ETH_srcAmount)
        print(stETH_to_ETH_destAmount)

        response = requests.get(DEXSCREENER_API_URL)
        data = response.json()
        DEXscreener_priceOf_stETH_in_ETH = data['pair']['priceNative']
        print(DEXscreener_priceOf_stETH_in_ETH)
        

        list_row = [formatted_time,
                    DEXscreener_priceOf_stETH_in_ETH,
                    ETH_to_stETH_srcAmount,
                    ETH_to_stETH_destAmount,
                    ETH_to_stETH_gasCostUSD,
                    stETH_to_ETH_srcAmount,
                    stETH_to_ETH_destAmount,
                    stETH_to_ETH_gasCostUSD
                    ]
        swap_df.loc[len(swap_df)] = list_row
        swap_df.to_csv(csv_file_path, mode='a', header=False, index=False)

    except Exception as e:
        print(f"Erreur lors de la récupération du prix : {e}")

# def send_price():
#     price, url = get_price()
#     if float(price) < 1 or float(price) >1 :
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
        get_price()
        time.sleep(60)

if __name__ == '__main__':
    main()
import requests
import time
import pandas as pd
from datetime import datetime

# Remplacez cela par le token de votre bot Telegram
TELEGRAM_BOT_TOKEN = '6954413568:AAHejo4WdJWgZb23LrmHG6eYZNe0mv1-2Aw'



CHAT_ID = '-4092738810'

print("startbot")



swap_df = pd.DataFrame(columns=['srcToken_name',
                                'srcToken_address',
                                'srcToken_decimals',
                                'destToken_name',
                                'destToken_address',
                                'destToken_decimals',
                                #'api_url',
                                #'url',
                                'srcToken_amount',
                                'threshold',
                                'thresholdSwapBack',
                                "updateTimer",
                                "updateTimerSwapBack",
                                "network", 
                                "network_code"
                                ])

# ETH_to_stETH_PARASWAP_API_URL = 'https://apiv5.paraswap.io/prices/?srcToken=0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE&destToken=0xae7ab96520de3a18e5e111b5eaab095312d7fe84&amount=100000000000000000000&srcDecimals=18&destDecimals=18&side=SELL&network=1'
# # stETH_to_ETH_PARASWAP_API_URL = 'https://apiv5.paraswap.io/prices/?srcToken=0xae7ab96520de3a18e5e111b5eaab095312d7fe84&destToken=0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE&amount=100000000000000000000&srcDecimals=18&destDecimals=18&side=SELL&network=1'

#USDC_to_sUSD_PARASWAP_API_URL='https://apiv5.paraswap.io/prices/?srcToken=0x0b2C639c533813f4Aa9D7837CAf62653d097Ff85&destToken=0x8c6f28f2F1A3C87F0f938b96d27520d9751ec8d9&amount=100000000000&srcDecimals=6&destDecimals=18&side=SELL&network=10'

#USDC_to_FRAX_PARASWAP_API_URL='https://apiv5.paraswap.io/prices/?srcToken=0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48&destToken=0x853d955acef822db058eb8505911ed77f175b99e&amount=100000000000&srcDecimals=6&destDecimals=18&side=SELL&network=1'

#USDC_to_crvUSD_PARASWAP_API_URL='https://apiv5.paraswap.io/prices/?srcToken=0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48&destToken=0xf939E0A03FB07F59A73314E73794Be0E57ac1b4E&amount=100000000000&srcDecimals=6&destDecimals=18&side=SELL&network=1'

#USDC_to_GUSD_PARASWAP_API_URL='https://apiv5.paraswap.io/prices/?srcToken=0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48&destToken=0x056fd409e1d7a124bd7017459dfea2f387b6d5cd&amount=100000000000&srcDecimals=6&destDecimals=2&side=SELL&network=1'

list_row = ["ETH", "0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE", 18,
            "stETH", "0xae7ab96520de3a18e5e111b5eaab095312d7fe84", 18,
            #"https://apiv5.paraswap.io/prices/?srcToken=0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE&destToken=0xae7ab96520de3a18e5e111b5eaab095312d7fe84&amount=100000000000000000000&srcDecimals=18&destDecimals=18&side=SELL&network=1",
            #'https://app.paraswap.io/#/0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE-0xae7ab96520DE3A18E5e111B5EaAb095312D7fE84/100/SELL?network=ethereum',
            100, 100.1, 99.99,0,0, "ethereum",1]
swap_df.loc[len(swap_df)] = list_row

list_row = ["USDC", "0x0b2C639c533813f4Aa9D7837CAf62653d097Ff85", 6,
            "sUSD", "0x8c6f28f2F1A3C87F0f938b96d27520d9751ec8d9", 18,
            #'https://apiv5.paraswap.io/prices/?srcToken=0x0b2C639c533813f4Aa9D7837CAf62653d097Ff85&destToken=0x8c6f28f2F1A3C87F0f938b96d27520d9751ec8d9&amount=100000000000&srcDecimals=6&destDecimals=18&side=SELL&network=10',
            #'https://app.paraswap.io/#/0x0b2c639c533813f4aa9d7837caf62653d097ff85-0x8c6f28f2F1A3C87F0f938b96d27520d9751ec8d9/100000/SELL?network=optimism',
            100000, 100300, 99950, 0, 0,"optimism",10]
swap_df.loc[len(swap_df)] = list_row

list_row = ["USDC", "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48", 6,
            "FRAX", "0x853d955acef822db058eb8505911ed77f175b99e", 18,
            #'https://apiv5.paraswap.io/prices/?srcToken=0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48&destToken=0x853d955acef822db058eb8505911ed77f175b99e&amount=100000000000&srcDecimals=6&destDecimals=18&side=SELL&network=1',
            #'https://app.paraswap.io/#/0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48-0x853d955aCEf822Db058eb8505911ED77F175b99e/100000/SELL?network=ethereum',
            100000, 100300, 99950, 0, 0,"ethereum",1]
swap_df.loc[len(swap_df)] = list_row

list_row = ["USDC", "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48", 6,
            "crvUSD", "0xf939E0A03FB07F59A73314E73794Be0E57ac1b4E", 18,
            #'https://apiv5.paraswap.io/prices/?srcToken=0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48&destToken=0xf939E0A03FB07F59A73314E73794Be0E57ac1b4E&amount=100000000000&srcDecimals=6&destDecimals=18&side=SELL&network=1',
            #'https://app.paraswap.io/#/0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48-0xf939e0a03fb07f59a73314e73794be0e57ac1b4e/100000/SELL?network=ethereum',
            100000, 100300, 99950, 0, 0,"ethereum",1]
swap_df.loc[len(swap_df)] = list_row

list_row = ["USDC", "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48", 6,
            "GUSD", "0x056fd409e1d7a124bd7017459dfea2f387b6d5cd", 2,
            #'https://apiv5.paraswap.io/prices/?srcToken=0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48&destToken=0x056fd409e1d7a124bd7017459dfea2f387b6d5cd&amount=100000000000&srcDecimals=6&destDecimals=2&side=SELL&network=1',
            #'https://app.paraswap.io/#/0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48-0x056Fd409E1d7A124BD7017459dFEa2F387b6d5Cd/100000/SELL?network=ethereum',
            100000, 100300, 99950, 0, 0,"ethereum",1]
swap_df.loc[len(swap_df)] = list_row

def get_price():
    try:
        # current_time = datetime.now()
        # formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        # print("Formatted time:", formatted_time)

        # ######
        # SWAP
        # ######
        for index, row in swap_df.iterrows():
            #print(row['destToken_name'])

            api_url = "https://apiv5.paraswap.io/prices/?srcToken="+row["srcToken_address"]+"&destToken="+row["destToken_address"]+"&amount="+str(row["srcToken_amount"]*10**row["srcToken_decimals"])+"&srcDecimals="+str(row["srcToken_decimals"])+"&destDecimals="+str(row["destToken_decimals"])+"&side=SELL&network="+str(row["network_code"])
            #print(api_url)
            
            response = requests.get(api_url)
            data = response.json()
            srcAmount = float(data['priceRoute']['srcAmount'])/(10**(data['priceRoute']['srcDecimals']))
            destAmount = float(data['priceRoute']['destAmount'])/(10**(data['priceRoute']['destDecimals']))
            gasCostUSD = float(data['priceRoute']['gasCostUSD'])
            
            if destAmount > row['threshold'] :
                if row['updateTimer']==0 :

                    url="https://app.paraswap.io/#/"+row["srcToken_address"]+"-"+row["destToken_address"]+"/"+str(row["srcToken_amount"])+"/SELL?network="+row["network"]

                    message = f'SWAP : {srcAmount:.2f} {row["srcToken_name"]} = {destAmount:.2f} {row["destToken_name"]} (gas cost of ${gasCostUSD:.2f})\n{url}'
                    #print("price interesting!")
                    print(message)
                    requests.post(
                        f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage',
                        data={'chat_id': CHAT_ID, 'text': message, 'disable_web_page_preview': True}
                    )
                    swap_df.loc[index,'updateTimer']+=1
                # elif row['updateTimer']==29:
                #     swap_df.loc[index,'updateTimer']=0
                # else :
                #     swap_df.loc[index,'updateTimer']+=1
            else:
                swap_df.loc[index,'updateTimer']=0

        # #########
        # SWAP BACK
        # #########
        for index, row in swap_df.iterrows():
            #print(row['destToken_name'])

            api_url = "https://apiv5.paraswap.io/prices/?srcToken="+row["destToken_address"]+"&destToken="+row["srcToken_address"]+"&amount="+str(row["srcToken_amount"]*10**row["destToken_decimals"])+"&srcDecimals="+str(row["destToken_decimals"])+"&destDecimals="+str(row["srcToken_decimals"])+"&side=SELL&network="+str(row["network_code"])
            #print(api_url)
            
            response = requests.get(api_url)
            data = response.json()
            srcAmount = float(data['priceRoute']['srcAmount'])/(10**(data['priceRoute']['srcDecimals']))
            destAmount = float(data['priceRoute']['destAmount'])/(10**(data['priceRoute']['destDecimals']))
            gasCostUSD = float(data['priceRoute']['gasCostUSD'])
            
            if destAmount > row['thresholdSwapBack'] :
                if row['updateTimerSwapBack']==0 :

                    url="https://app.paraswap.io/#/"+row["destToken_address"]+"-"+row["srcToken_address"]+"/"+str(row["srcToken_amount"])+"/SELL?network="+row["network"]

                    message = f'SWAP BACK : {srcAmount:.2f} {row["destToken_name"]} = {destAmount:.2f} {row["srcToken_name"]} (gas cost of ${gasCostUSD:.2f})\n{url}'
                    #print("price interesting!")
                    print(message)
                    requests.post(
                        f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage',
                        data={'chat_id': CHAT_ID, 'text': message, 'disable_web_page_preview': True}
                    )
                else :
                    swap_df.loc[index,'updateTimerSwapBack']+=1
            else:
                swap_df.loc[index,'updateTimerSwapBack']=0




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
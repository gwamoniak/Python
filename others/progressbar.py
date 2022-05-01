import math
import pandas_datareader as web
import colorama # pip install colorama

def progress_bar(progress, total, color=colorama.Fore.YELLOW):
    percent = 100 * (progress / float(total))
    bar = '█' * int(percent) + '-' * (100 - int(percent))
    print(color + f"\r|{bar}| {percent:.2f}%", end ="\r")
    if progress == total:
        print(colorama.Fore.GREEN + f"\r|{bar}| {percent:.2f}%", end ="\r")
    

ticker = ["APPL", "FB", "NVDA", "WFC"]
clossing_prices = []

progress_bar(0,len(tickers))
for index, ticker in enumerate(tickers):
    last_price = web.DataReader(ticker, "yahoo").iloc[-1]['Close']
    clossing_prices.append(last_price)
    progress_bar(index + 1,len(tickers))

 # only for testing   
numbers =[x * 5 for x in range(2000, 3000)]
result = []

for i, x in enumerate(numbers):
    result.append(math.factorial(x))
    progress_bar(i + 1, len(numbers))

print(colorama.Fore.RESET)
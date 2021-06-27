from nepse import NEPSE

init = NEPSE()

# GET ALL REGISTERED BROKERS
brokers = init.brokers()

# GET ALL NEWS & ALERTS Published By NEPSE on Newweb
news = init.alerts()

# Check IF MARKET IS OPEN
isOpen = init.isOpen()  # Returns TRUE IF market is open

# Check live price of specific scrip or get all prices
allPrices = init.todayPrice()
cghPrice = init.todayPrice('CGH')  # returns information for CGH

# CHARTS
chartHistory = init.getChartHistory('CGH')  # Get History Prices for CGH
chartHistoryButFiltered = init.getChartHistory('CGH', start_date='2017-01-01', end_date='2021-06-21')

makeChart = init.createChart('CGH', theme='dark', high=False, low=False)  # returns abspath of chart saved

csv = init.saveCSV('CGH', start_date='2017-01-01')  # filename,start_date and  end_date are optional

indices = init.indices(sector='NEPSE Index', start_date='2017-01-01', end_date='2021-06-21')

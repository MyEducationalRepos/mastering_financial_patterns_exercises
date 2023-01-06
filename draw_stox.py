import yfinance as yf

stocks_list =  ['AAL', 'AAPL', 'AAPL', 'ABBV', 'ABT', 'ADBE', 'ADI', 'ADI', 
                'ADM', 'ADP', 'ADSK', 'ALGN', 'ALL', 'AM', 'AMAT', 'AMAT', 'AMD', 
                'AMGN', 'AMZN', 'AMZN', 'ANSS', 'APA', 'APTV', 'ASML', 'ATVI', 
                'AUY', 'AVGO', 'BA', 'BA', 'BAC', 'BDX', 'BIDU', 'BIIB', 'BKNG', 
                'BMRN', 'BSX', 'C', 'CAMP', 'CCL', 'CCL', 'CDNS', 'CDW',
                'CHE', 'CHK', 'CHKP', 'CHRW', 'CHTR', 'CIM', 'CLR', 'CMCSA', 'CMCSA', 
                'CNP', 'COLM', 'COP', 'COP', 'COST', 'COST', 'CPE', 'CPRT', 'CSCO',
                'CSGP', 'CSX', 'CTAS', 'CTSH', 'CVS', 'CVX', 'CVX', 'DAKT', 
                'DAL', 'DE', 'DGX', 'DIS', 'DLTR', 'DVN', 'DVN', 'EA', 'EBAY', 'EMN', 
                'EPD', 'ESRT', 'EXPE', 'F', 'FAST', 'FCX', 'FDP', 'FDX', 
                'FICO', 'FISV', 'FOX', 'FOXA', 'FSLR', 'GCI', 'GE', 'GGB', 'GILD', 
                'GLW', 'GM', 'GOOG', 'GOOGL', 'GPS', 'HAL', 'HD', 'HON', 'HPQ',
                'IDXX', 'IFF', 'ILMN', 'INCY', 'INTC', 'INTU', 'ISRG', 'ITW',
                'JD', 'JNJ', 'JPM', 'KEY', 'KGC', 'KHC', 'KLAC', 'KMX', 'KO', 'KR',
                'KSS', 'LBTYA', 'LBTYK', 'LRCX', 'LULU', 'LUV', 'M', 'MAC', 'MAR', 
                'MCHP', 'MCHP', 'MCK', 'MDLZ', 'MDT', 'MELI', 'META','MFA', 'MGM', 
                'MMM', 
                'MNST', 'MOS', 'MRO', 'MS', 'MSFT', 'MU', 'MUR', 'MYGN', 'NBR', 
                'NEM', 'NFLX', 'NKE', 'NLY', 'NSC', 'NTAP', 'NTES', 'NVDA', 
                'NVO', 'NXPI', 'ORA', 'ORCL', 'ORLY', 'OXY', 'PAYX', 'PAYX', 'PCAR', 
                'PCG', 'PEP', 'PFE', 'PG', 'PLD', 'PRGO', 'PRU', 'PSA', 'PYPL', 
                'QCOM', 'RCL', 'REGN', 'RF', 'RIG', 'RMD', 'ROST', 'ROST', 
                'RRC', 'SBUX', 'SBUX', 'SCHN', 'SEE', 'SGEN', 'SIEGY', 'SIRI', 'SJM', 
                'SLB', 'SLB', 'SM', 'SMG', 'SNPS', 'SPLK', 'SQ', 'STT', 'SU', 'SWKS', 
                'SWN', 'SYK', 'SYY', 'T', 'TCOM', 'TGT', 'TKR', 'TMUS', 'TREX', 'TSLA', 
                'TTWO', 'TUP', 'TXN', 'UAL', 'ULTA', 'UNH', 'UNP', 'UPS', 'V', 'VLO',
                'VMI', 'VOD', 'VRSK', 'VRSN', 'VRTX', 'VZ', 'WBA', 'WDC',
                'WFC', 'WHR', 'WM', 'WMB', 'WTI', 'X', 'XEL', 'XOM',
                'XRAY', 'ZBRA']

        
data = yf.download(stocks_list, auto_adjust=True)['Close']
yields = data.pct_change()
zscores = (yields - yields.mean())/yields.std()
#Ojo con el plot 
'''
zscores.iloc[-252:,:3].plot(figsize=(10,6), 
             grid=True, 
             title='Zscores de variaciones diarias',
             alpha=0.3)
'''

tabla = zscores.tail(1).T
tabla.columns = ['cierre']
tabla.sort_values(by='cierre',ascending=True,inplace=True)


columnas = tabla.tail(5).columns
print(tabla.head(5).round(2))

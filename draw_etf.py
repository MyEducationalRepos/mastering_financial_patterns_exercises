import yfinance as yf

etf_list = ['ACWI','AGG','ARKK','ASHR','BIL','BITO','BKLN','BND','BOIL','EEM','EFA','EMB','EWZ',
            'FXI','GDX','GDXJ','GLD','GOVT','HYG','HYLB','IAU','ICLN','IEF','IEFA','IEMG','IGSB',
            'IWM','IYR','JDST','JNK','JPST','KOLD','KRE','KWEB','LABD','LABU','LQD','MCHI','MUB',
            'PDBC','PGX','PSQ','QID','QLD','QQQ','RSX','SCHF','SDOW','SDS','SH','SHY','SJNK','SLV',
            'SOXL','SOXS','SPDW','SPIB','SPTL','SPXL','SPXS','SPXU','SPY','SQQQ','SSO','TLT','TMF',
            'TNA','TQQQ','TSLL','TZA','UNG','UPRO','USHY','UVIX','UVXY','VCIT','VCSH','VEA','VEU',
            'VGK','VIXY','VNQ','VTEB','VWO','VXUS','VXX','XBI','XLB','XLC','XLE','XLF','XLI','XLK',
            'XLP','XLRE','XLU','XLV','XLY','XOP','YANG']        

data = yf.download(etf_list, auto_adjust=True)['Close']
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

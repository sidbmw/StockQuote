from qtrade import Questrade
import os
import json

# x = (curl 'https://app.quotemedia.com/datatool/getQuotes.json?symbols=AC' \
#       '&afterhours=true&timezone=true&premarket=true&currencyInd=true&countryInd=true&marketstatus=true&limit=25&token=a2f912523e48d72ed0266a82857b5fb58f45f18ba2f0c355f73710e8943c2cef' \
#   -H 'authority: app.quotemedia.com' \
#   -H 'accept: */*' \
#   -H 'dnt: 1' \
#   -H 'accept-language: en' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36' \
#   -H 'origin: https://web.tmxmoney.com' \
#   -H 'sec-fetch-site: cross-site' \
#   -H 'sec-fetch-mode: cors' \
#   -H 'sec-fetch-dest: empty' \
#   -H 'referer: https://web.tmxmoney.com/quote.php?qm_symbol=ac' \
#   -H 'cookie: lastQuote=ac; JSESSIONID=082C7176023DBDCEFF07B2F0C4510997.jboss-qt-d' \
#   --compressed)


# x = str(os.system("curl 'https://app.quotemedia.com/datatool/getQuotes.json"
#                   "?symbols=AC&afterhours=true&timezone=true&premarket=true&currencyInd=true&countryInd=true&marketstatus=true&limit=25&token=a2f912523e48d72ed0266a82857b5fb58f45f18ba2f0c355f73710e8943c2cef' \
#      -H 'authority: app.quotemedia.com' \
#      -H 'accept: */*' \
#      -H 'dnt: 1' \
#      -H 'accept-language: en' \
#      -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36' \
#      -H 'origin: https://web.tmxmoney.com' \
#      -H 'sec-fetch-site: cross-site' \
#      -H 'sec-fetch-mode: cors' \
#      -H 'sec-fetch-dest: empty' \
#      -H 'referer: https://web.tmxmoney.com/quote.php?qm_symbol=ac' \
#      -H 'cookie: lastQuote=ac; JSESSIONID=082C7176023DBDCEFF07B2F0C4510997.jboss-qt-d' \
#      --compressed | json_pp"))
# # {"results":{"copyright":"Copyright (c) 2020 QuoteMedia, Inc.","symbolcount":1,"quote":[{"key":{"symbol":"AC:CA","exchange":"TSX","exLgName":"Toronto Stock Exchange","exShName":"TSX","isopen":"true","iscurrentlyopen":"true","timezone":"EDT","currency":"CAD","country":"CAN","exchangecountry":"CA"},"equityinfo":{"longname":"Air Canada Voting and Variable Voting Shares","shortname":"AC:CA"},"status":{},"pricedata":{"last":17.96,"change":-1.55,"changepercent":-7.944644,"tick":0,"open":17.50,"high":18.83,"low":17.05,"prevclose":19.51,"bid":17.95,"ask":17.97,"bidsize":1100,"asksize":900,"rawbidsize":1100,"rawasksize":900,"tradevolume":32367,"sharevolume":8827387,"vwap":17.9787821,"lasttradedatetime":"2020-06-11T12:38:09-04:00","totalvalue":158678622.00,"lastmarketidentificationcode":"TSX","bidmarketidentificationcode":"TSX","askmarketidentificationcode":"TSX","imbalance":{"imbalancesize":0}},"premarket":{"last":"N/A","change":"N/A","changepercent":"N/A","sharevolume":0,"lasttradedatetime":"N/A"},"afterhours":{"last":"N/A","change":"N/A","changepercent":"N/A","sharevolume":0,"lasttradedatetime":"N/A"},"fundamental":{"sharesoutstanding":296615860,"shareclasslevelsharesoutstanding":296615860,"totalsharesoutstanding":296353172,"marketcap":5322502969,"eps":0.239999994,"peratio":81.3,"pbratio":1.249,"week52high":{"date":"2020-01-14","content":52.71},"week52low":{"date":"2020-03-18","content":9.27}},"symbolstring":"AC","datatype":"equity","entitlement":"RT","datetime":"2020-06-11T12:38:07-04:00"}]}}0


# print(x)

# y = json.loads((x))
# print(y["last"])

# q = Questrade(refresh_token='eu01Brq8NVsBGmptnvMLBuEsrSm9teM30')
qtrade = Questrade(access_code='<eu01Brq8NVsBGmptnvMLBuEsrSm9teM30>')

aapl, amzn = qtrade.ticker_information(['AAPL', 'AMZN'])

print(aapl, amzn)
# q = Questrade()
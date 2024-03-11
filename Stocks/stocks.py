import pandas as pd
import yfinance as yf
from send_email import compile_send_email
import os
from email.message import EmailMessage
import smtplib
from email.mime.base import MIMEBase
from email import encoders

with open ('previous_day_close.txt') as yesterday:
    old_total = yesterday.read()
    
# new = 2

cb_cdlr = 200 * 18.31
cost_b_cdlr = (cb_cdlr)

cb_fcx_lot1 = 51 * 39.62569
cb_fcx_lot2 = .226 * 33.84956
cost_b_fcx = (cb_fcx_lot1 + cb_fcx_lot2)

# Moved these tickers to a different portfolio
# cb_brkb = 24 * 325.00
# cost_b_brkb = (cb_brkb)

# cb_nke_lot1 = 30 * 110.37633
# cb_nke_lot2 = .09 * 101.66667
# cb_nke_lot3 = .11 * 83.45455
# cb_nke_lot4 = .087 * 118.04598
# cb_nke_lot5 = .084 * 122.61905
# cb_nke_lot6 = .095 * 108.73684
# cb_nke_lot7 = .108 * 95.92593

# cost_b_nke = (cb_nke_lot1 + cb_nke_lot2 + cb_nke_lot3 + cb_nke_lot4 + cb_nke_lot5 + cb_nke_lot6 + cb_nke_lot7)

# FCX 51 @ 39.62569 and .226 @33.84956


cb_eose_lot1 = 500 * 1.522
cb_eose_lot2 = 500 * 2.18266
cost_b_eose = (cb_eose_lot1 + cb_eose_lot2)

cb_f_lot1 = 300 * 7.90387
cb_f_lot2 = 2.155 * 13.92111
cb_f_lot3 = 3.004 * 15.08655
cb_f_lot4 = 3.25 * 14.08308
cb_f_lot5 = 16.217 * 12.36172
cb_f_lot6 = 3.742 * 12.36237
cb_f_lot7 = 4.1 * 12.01463
cb_f_lot8 = 4.109 * 12.13677
cb_f_lot9 = 4.909 + 10.28519
cost_b_f = (cb_f_lot1 + cb_f_lot2 + cb_f_lot3 + cb_f_lot4 + cb_f_lot5 + cb_f_lot6 + cb_f_lot7 + cb_f_lot8 + cb_f_lot9)

cb_googl_lot1 = 20 * 153.2285
cb_googl_lot2 = 40 * 108.67425
cb_googl_lot3 = 40 * 92.22125
cost_b_googl = (cb_googl_lot1 + cb_googl_lot2 + cb_googl_lot3)

cb_amzn_lot1 = 20 * 145.5285
cb_amzn_lot2 = 40 * 106.96525
cb_amzn_lot3 = 40 * 85.2265
cost_b_amzn = (cb_amzn_lot1 + cb_amzn_lot2 + cb_amzn_lot3)

cb_clsd = 500 * 1.249
cost_b_clsd = (cb_clsd)

cb_csx_lot1 = 27 * 27.63259
cb_csx_lot2 = 54 * 27.63278
cb_csx_lot3 = .273 * 29.67033
cb_csx_lot4 = .26 * 31.26923
cb_csx_lot5 = .254 * 32.08661
cb_csx_lot6 = .31 * 29.03226
cb_csx_lot7 = .273 * 33.07692
cb_csx_lot8 = .292 + 31.0274
cb_csx_lot9 = .269 * 33.79182
cost_b_csx = (cb_csx_lot1 + cb_csx_lot2 + cb_csx_lot3 + cb_csx_lot4 + cb_csx_lot5 + cb_csx_lot6 + cb_csx_lot7 + cb_csx_lot8 + cb_csx_lot9)

cb_qcln_lot1 = 50 * 60.7788
cb_qcln_lot2 = 36 * 63.63306
cb_qcln_lot3 = .019 * 51.57895
cb_qcln_lot4 = .087 * 56.89655
cb_qcln_lot5 = .159 * 46.28931
cb_qcln_lot6 = .088 * 51.13636
cb_qcln_lot7 = .272 * 50.58824
cb_qcln_lot8 = .052 * 43.46154
cb_qcln_lot9 = .166 * 42.83133
cost_b_qcln = (cb_qcln_lot1 + cb_qcln_lot2 + cb_qcln_lot3 + cb_qcln_lot4 + cb_qcln_lot5 + cb_qcln_lot6 + cb_qcln_lot7 + cb_qcln_lot8 + cb_qcln_lot9)

cb_jbl_lot1 = 100 * 56.8086
cb_jbl_lot2 = .135 * 59.25926
cb_jbl_lot3 = .112 * 71.51786
cb_jbl_lot4 = .096 * 83.854167
cb_jbl_lot5 = .089 * 90.22472
cb_jbl_lot6 = .07 * 114.71429
cb_jbl_lot7 = .069 * 116.52174
cost_b_jbl = (cb_jbl_lot1 + cb_jbl_lot2 + cb_jbl_lot3 + cb_jbl_lot4 + cb_jbl_lot5 + cb_jbl_lot6 + cb_jbl_lot7)

cb_mrvl_lot1 = 51 * 44.44216
cb_mrvl_lot2 = 49 * 75.04082
cb_mrvl_lot3 = .117 * 51.28205
cb_mrvl_lot4 = .151 * 39.80132
cb_mrvl_lot5 = .145 * 41.51724
cb_mrvl_lot6 = .16 * 37.625
cb_mrvl_lot7 = .096 * 62.8125
cb_mrvl_lot8 = .124 * 48.70968
cb_mrvl_lot9 = .09 * 67.22222
cost_b_mrvl = (cb_mrvl_lot1 + cb_mrvl_lot2 + cb_mrvl_lot3 + cb_mrvl_lot4 + cb_mrvl_lot5 + cb_mrvl_lot6 + cb_mrvl_lot7 + cb_mrvl_lot8 + cb_mrvl_lot9)

cb_xlp_lot1 = 36 * 68.23639
cb_xlp_lot2 = .256 * 72.10938
cb_xlp_lot3 = .236 * 70.76271
cb_xlp_lot4 = .26 * 74.80769
cb_xlp_lot5 = .175 * 72.40
cb_xlp_lot6 = .261 * 74.40613
cb_xlp_lot7 = .253 * 71.30435
cb_xlp_lot8 = .285 * 70.49123
cost_b_xlp = (cb_xlp_lot1 + cb_xlp_lot2 + cb_xlp_lot3 + cb_xlp_lot4 + cb_xlp_lot5 + cb_xlp_lot6 + cb_xlp_lot7 + cb_xlp_lot8)

cb_xlv_lot1 = 22 * 111.13
cb_xlv_lot2 = .087 * 127.47126
cb_xlv_lot3 = .091 * 122.74725
cb_xlv_lot4 = .091 * 135.49451
cb_xlv_lot5 = .086 * 126.62791
cb_xlv_lot6 = .092 * 131.84783
cb_xlv_lot7 = .092 * 131.63043
cb_xlv_lot8 = .101 * 133.36634
cost_b_xlv = (cb_xlv_lot1 + cb_xlv_lot2 + cb_xlv_lot3 + cb_xlv_lot4 + cb_xlv_lot5 + cb_xlv_lot6 + cb_xlv_lot7 + cb_xlv_lot8)

cb_xlk_lot1 = 20 * 125.1405
cb_xlk_lot2 = .05 * 129.20
cb_xlk_lot3 = .05 * 127.00
cb_xlk_lot4 = .058 * 126.55172
cb_xlk_lot5 = .044 * 144.54545
cb_xlk_lot6 = .043 * 169.76744
cb_xlk_lot7 = .044 * 165.68182
cb_xlk_lot8 = .045 * 190.22222
cost_b_xlk = (cb_xlk_lot1 + cb_xlk_lot2 + cb_xlk_lot3 + cb_xlk_lot4 + cb_xlk_lot5 + cb_xlk_lot6 + cb_xlk_lot7 + cb_xlk_lot8)

cb_spir = 80 * 11.15
cost_b_spir = (cb_spir)

cb_anefx_lot1 = 19.929 * 64.91344
cb_anefx_lot2 = 1.532 * 64.90862
cb_anefx_lot3 = .052 * 53.26923
cb_anefx_lot4 = .812 * 53.0665
cost_b_anefx = (cb_anefx_lot1 + cb_anefx_lot2 + cb_anefx_lot3 + cb_anefx_lot4)

cost_basis_total = (cost_b_spir + cost_b_xlk + cost_b_xlv + cost_b_xlp + cost_b_mrvl + cost_b_jbl
                    + cost_b_qcln + cost_b_csx + cost_b_clsd + cost_b_amzn + cost_b_googl + cost_b_f + cost_b_eose
                    + cost_b_anefx + cost_b_cdlr)

tickers = {'EOSE':[1000,cost_b_eose], 'F':[336.577,cost_b_f], 'XLV':[22.447,cost_b_xlv], 'XLK':[20.245,cost_b_xlk],
           'XLP':[37.188,cost_b_xlp], 'CSX':[82.37,cost_b_csx], 'SPIR':[80,cost_b_spir],
           'GOOGL':[100,cost_b_googl], 'AMZN':[100,cost_b_amzn],
           'MRVL':[100.669,cost_b_mrvl], 'JBL':[100.502,cost_b_jbl], 'QCLN':[86.625,cost_b_qcln], 'CLSD':[500,cost_b_clsd],
           'ANEFX':[21.461,cost_b_anefx], 'FCX':[51.226,cost_b_fcx], 'CDLR':[200,cost_b_cdlr]
           }
total = 0

d = []

for ticker, shares in tickers.items():
    ticker_yahoo = yf.Ticker(ticker)
    data = ticker_yahoo.history()
    last_quote = data['Close'].iloc[-1]
    d.append(
        {
            'Stock' : ticker,
            'Total Shares' : f'{shares[0]:.2f}',
            'Current Price' : f'{last_quote:.2f}',
            'Value' : f'{(shares[0] * last_quote):.2f}',
            'Cost Basis' : f'{shares[1]:.2f}',
            'Gain/Loss' : f'{(shares[0] * last_quote - shares[1]):.2f}'
        }
    )
    total += last_quote * shares[0]
result = pd.DataFrame(d)
# new_result = result.to_html()
html = result.to_html()
text_file = open("index.html", "w")
text_file.write(html)
text_file.write(f'Total Assets Value: {total:.2f}<br>\nCost Basis: {cost_basis_total:.2f}<br>\nTotal Gain/Loss: {total - cost_basis_total:.2f}')
text_file.write(f"\nChange from yesterday: ${total - float(old_total):.2f}")
text_file.close()
print('-'*73)
print(result)
print('-'*73)
print(f'Total Assets Value: {total:.2f}\nCost Basis: {cost_basis_total:.2f}\nTotal Gain/Loss: {total - cost_basis_total:.2f}')
result.to_csv('data.txt', sep='\t', index=False)

prev_day = total
with open('previous_day_close.txt','w') as prev_d:
    prev_d.write(str(prev_day))
print(f"\nChange from yesterday: ${total - float(old_total):.2f}")

compile_send_email()
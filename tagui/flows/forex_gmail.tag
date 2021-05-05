https://www.dbs.com.sg/personal/rates-online/foreign-currency-foreign-exchange.page

dump Currency,Rate to number.csv

rows = count('//tbody/tr[@class="mobile-hide active"]')

for row from 1 to rows
    read ((//*[contains(@class,  "tb1-primary")]/tbody/tr)[`row`]//td)[1] to currency
    read ((//*[contains(@class,  "tb1-primary")]/tbody/tr)[`row`]//td)[3] to rate
    forex_rate = [currency, 'S$' + rate]        
    write `csv_row(forex_rate)` to number.csv

keyboard [win]r
wait 1
keyboard chrome[enter]
wait 1bu
keyboard [win][up]


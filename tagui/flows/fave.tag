https://myfave.com/cities/singapore/best-new-deals

wait 5

dump Deal, Link to deals.csv

cards = count('//div[@class="ui card segment offer-card borderless"]')

for card from 1 to cards
    read (//div[@class="ui card segment offer-card borderless"])[`card`]/a[@class="content"]/h3 to deal
    if deal contains "MOTHER'S DAY"
        read (//div[@class="ui card segment offer-card borderless"])[`card`]/a[@class="content"]/@href to link
        dealrow = [deal, 'https://myfave.com' + link]
        write `csv_row(dealrow)` to deals.csv
    /
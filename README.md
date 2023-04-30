# CMS_Price_Transparency

This is an attempt to perform data transformation for a Price Transparency requirement.
Txt file will be ingested via Azure data factory,saved into a landing page.
From the landing page Azure databrick will be use to perform data manipulation.
Currently the code is able to performa desired output which is a:
1. A simple pivot table that extract by Plan(s) pivoted by IP and OP,
2. A MIN , MAX is added to the last 4 columns.

The issue which needs to be resolve is it is erroring if ther are duplicate rows but with different IP/OP price. The intent is to 
perform mean on those rows that have duplicate dimension but with different IP/OP values. 
...Will continue to research. but so far the base code is acceptable.

Note. The priceTest is the raw data
         Output 2 is the pase output for the first phase.

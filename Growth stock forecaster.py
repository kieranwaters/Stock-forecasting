print('This program is to estimate future stock returns based on past performance of fundamentals. This program is aimed to estimate returns of early stage growth stocks that have experiemced rapid growth in the last couple of years')

YoRG = input('\n Enter the years of reveneue growth you which to extrapolate')

PG = input(' enter the percentage revenue growth during this period')

SP = input(' Enter the stock price')

Years = float(input( 'Enter the years to forecast.    (Please note the higher the years, the lower the accuracy'))

Stock = input( 'Enter the name of the Stock')

Annualgrowth = float(PG)/float(YoRG)
      
print( 'The average annual revuenue growth rate of',Stock ,'is', Annualgrowth)

print('the estimated stock price of', Stock ,'in', Years ,'years is', float(Annualgrowth)/100 +1*float(Years) )


if Years > 5:
    print('extrapolating the data too far increases unpredictability exponentially.')

else:
    print('This is within the recommended forecast range')

if Annualgrowth < 7:
    print('This stock is predicted to underperform the average US stock of 7%pa')
if Annualgrowth > 7:
    print('This stock is predicted to outperform the average US stock of 7%pa')
if Annualgrowth > 19:
    print('This stock is predicted to outperform Warren Buffets investing portfolio of 19&pa')
if Annualgrowth > 30:
    print("This stock is predicted to outperform Peter Lynch's investing record of 30%pa")


                      
        


        
    

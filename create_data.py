from genovia import db
from genovia.models import User, Post
import random

i = 1
incrementingTitle = "0"
incrementingDesc = "0"
rotatingUser_id = 1
while(i <= 100):
    # generate random values for the prices
    daily_price = float(random.randrange(277, 999))/100
    weekly_price = float(random.randrange(1000, 3000))/100
    monthly_price = float(random.randrange(5000, 9999))/100

    post = Post(title='ANOTHER Test Listing ' + incrementingTitle, description='yes, even more dummy desc. # ' + incrementingDesc, price_per_day=daily_price,
    price_per_week=weekly_price, price_per_month=monthly_price, location='Chattanooga, Tennessee',
    contact='(680)447-2279', user_id=6)
    db.session.add(post)
    db.session.commit()

    #print(post)
    incrementingTitle = str(i)
    incrementingDesc = str(i)
    i = i + 1

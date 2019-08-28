

import pandas as pd
df = pd.read_csv('amazon_reviews_us_Home_Entertainment_v1_00.tsv',delimiter='\t',nrows=6000,encoding='utf-8-sig')
dd=df.groupby(by='customer_id').count()
dd = dd.reset_index()


product = df[['product_id','product_title']]

review = df[['review_id','customer_id','product_id','product_parent','review_date' ]]

vine = df[['review_id','star_rating','helpful_votes','total_votes','vine']]

customers = dd[['customer_id','review_id']]
customers= customers.rename(columns={'review_id':'customer_count'})

customers.to_csv('customers1.csv')

product.to_csv('products1.csv')

review.to_csv('reviews1.csv')

vine.to_csv('vine1.csv')
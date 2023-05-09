import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


data=pd.DataFrame(pd.read_csv('Sales2016-2019.csv'))



#MOST POPULAR ITEM PER ZIP CODE.

Most_pop_zipcode = pd.DataFrame(data.groupby(by=['zip_code','item_description',]).sum()['bottles_sold']).reset_index()
Most_pop_zipcode.to_csv('Most_Pop_Zip_Code.csv')

#PERCENTAGE OF SALES PER STORE.

Sales_per_store = pd.DataFrame(data.groupby(by=['store_number','store_name']).sum()['sale_dollars']).reset_index()
Sales_per_store['percentage'] = Sales_per_store['sale_dollars'].apply(lambda x: (x/data['sale_dollars'].sum())*100)
Sales_per_store.to_csv('Sales_per_store.csv')

#MATPLOLIB

#MOST POPULAR ITEM PER ZIP CODE.

x=np.array(Most_pop_zipcode['zip_code'])
y=np.array(Most_pop_zipcode['bottles_sold'])
N=72
colors=np.random.rand(N)
plt.scatter(x, y, c=colors, alpha=0.7)
plt.title('Most Popular Item Per ZipCode',color='black')
plt.xlabel('Zip_codes',color='black')
plt.ylabel('Sold Bottles',color='black')
plt.show()

#PERCENTAGE OF SALES PER STORE.
Sales_per_store['store_number'] = Sales_per_store['store_number'].astype(str)
plt.figure(figsize=(14,8))
sns.barplot(x=Sales_per_store['percentage'],y=Sales_per_store['store_number'],data=Sales_per_store,palette='viridis')
plt.title('Percentage % of Sales Per Store',color='black')
plt.xlabel('Percentage %',color='black')
plt.ylabel('Store Numbers',color='black')
plt.show()



# generate_clean_data.py

import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta

# Initialize Faker for generating random data
fake = Faker()

# Create a synthetic customers dataframe with clean data
customers_data = []
for _ in range(100):
    customers_data.append({
        'customer_id': fake.uuid4(),
        'customer_name': fake.name(),
        'customer_email': fake.email(),
        'customer_phone': fake.phone_number()
    })

customers_df = pd.DataFrame(customers_data)

# Create a synthetic products dataframe with clean data
products_data = []
for _ in range(10):
    products_data.append({
        'product_id': fake.uuid4(),
        'product_name': fake.word(),
        'product_price': round(random.uniform(10, 100), 2)
    })

products_df = pd.DataFrame(products_data)

# Create a synthetic orders dataframe with clean data
orders_data = []
for _ in range(100):
    order = {
        'order_id': fake.uuid4(),
        'customer_id': random.choice(customers_df['customer_id']),
        'product_id': random.choice(products_df['product_id']),
        'customer_email': fake.email(),
        'quantity': random.randint(1, 20),
        'customer_phone': fake.phone_number(),
        'order_timestamp': (datetime.now() - timedelta(days=random.randint(1, 30))).strftime('%Y-%m-%d %H:%M:%S')
    }
    orders_data.append(order)

orders_df = pd.DataFrame(orders_data)

# Save clean dataframes as CSV files or load them into a database
customers_df.to_csv('clean_customers.csv', index=False)
products_df.to_csv('clean_products.csv', index=False)
orders_df.to_csv('clean_orders.csv', index=False)

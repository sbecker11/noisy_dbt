# add_noise_and_errors.py

import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta

# Load the clean dataframes
clean_customers_df = pd.read_csv('clean_customers.csv')
clean_products_df = pd.read_csv('clean_products.csv')
clean_orders_df = pd.read_csv('clean_orders.csv')

# Initialize Faker for generating random data
fake = Faker()

# Noisy Customers DataFrame
noisy_customers_data = []
for index, row in clean_customers_df.iterrows():
    # Add alternate name spellings (10% chance)
    if random.random() < 0.1:
        alternate_name = row['customer_name'].replace(random.choice(row['customer_name']), random.choice(['A', 'B', 'C']))
    else:
        alternate_name = row['customer_name']

    # Introduce partial and invalid email addresses (10% chance)
    if random.random() < 0.1:
        partial_email = fake.word()
    else:
        partial_email = row['customer_email']

    # Introduce partial and invalid phone numbers (10% chance)
    if random.random() < 0.1:
        partial_phone = fake.word()
    else:
        partial_phone = row['customer_phone']

    noisy_customers_data.append({
        'customer_id': row['customer_id'],
        'customer_name': alternate_name,
        'customer_email': partial_email,
        'customer_phone': partial_phone
    })

noisy_customers_df = pd.DataFrame(noisy_customers_data)

# Noisy Products DataFrame
noisy_products_data = []
for index, row in clean_products_df.iterrows():
    # Add alternate name spellings (10% chance)
    if random.random() < 0.1:
        alternate_name = row['product_name'].replace(random.choice(row['product_name']), random.choice(['X', 'Y', 'Z']))
    else:
        alternate_name = row['product_name']

    # Introduce outlier prices (5% chance)
    if random.random() < 0.05:
        outlier_price = round(random.uniform(1000, 5000), 2)
    else:
        outlier_price = row['product_price']

    noisy_products_data.append({
        'product_id': row['product_id'],
        'product_name': alternate_name,
        'product_price': outlier_price
    })

noisy_products_df = pd.DataFrame(noisy_products_data)

# Noisy Orders DataFrame
noisy_orders_data = []
for index, row in clean_orders_df.iterrows():
    # Introduce random null values (10% chance)
    if random.random() < 0.1:
        customer_id = None
    else:
        customer_id = row['customer_id']

    # Corrupt some percentage of order dates (10% chance)
    if random.random() < 0.1:
        order_timestamp = fake.word()  # Invalid date format
    elif random.random() < 0.1:
        order_timestamp = '2022-02-30'  # Invalid date
    else:
        order_timestamp = row['order_timestamp']

    # Introduce alternate character encodings (5% chance)
    if random.random() < 0.05:
        customer_name = row['customer_name'].encode('utf-16').decode('utf-8')
    else:
        customer_name = row['customer_name']

    # Introduce missing or invalid delimiters (5% chance)
    if random.random() < 0.05:
        customer_email = row['customer_email'].replace('@', '')
    else:
        customer_email = row['customer_email']

    # Introduce outlier #units (5% chance)
    if random.random() < 0.05:
        quantity = str(random.randint(100, 1000))
    else:
        quantity = row['quantity']

    # Introduce outlier prices (5% chance)
    if random.random() < 0.05:
        product_price = str(round(random.uniform(1000, 5000), 2))
    else:
        product_price = row['product_price']

    # Create some percentage of data integrity errors (5% chance)
    if random.random() < 0.05:
        customer_id = fake.uuid4()  # Change foreign key

    noisy_orders_data.append({
        'order_id': row['order_id'],
        'customer_id': customer_id,
        'product_id': row['product_id'],
        'customer_email': customer_email,
        'quantity': quantity,
        'customer_phone': row['customer_phone'],
        'order_timestamp': order_timestamp,
        'customer_name': customer_name
    })

noisy_orders_df = pd.DataFrame(noisy_orders_data)

# Save noisy dataframes as CSV files or load them into a database
noisy_customers_df.to_csv('noisy_customers.csv', index=False)
noisy_products_df.to_csv('noisy_products.csv', index=False)
noisy_orders_df.to_csv('noisy_orders.csv', index=False)

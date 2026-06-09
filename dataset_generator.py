import pandas as pd
import numpy as np
from faker import Faker
import random
from pathlib import Path

fake = Faker()
# Fixes the random values generated to make data reproducible
np.random.seed(42)
random.seed(42)

N_CUSTOMERS   = 2000
N_TRANSACTIONS = 10000

# ── 1. Product Catalog ─────────────────────────────────────────────
CATEGORIES = ['Electronics', 'Fashion', 'Home & Living',
              'Food & Grocery', 'Health & Beauty', 'Sports', 'Books']
PRODUCTS = []
for pid in range(1, 201):
    PRODUCTS.append({
        'product_id': f'P{pid:04d}',
        'category': random.choice(CATEGORIES),
        'price': round(np.random.uniform(5, 500), 2),
        'avg_rating': round(np.random.uniform(2.5, 5.0), 1),
        'stock_quantity': np.random.randint(0, 500)
    })
products_df = pd.DataFrame(PRODUCTS)
# print(products_df)

# ── 2. Customer Demographics ───────────────────────────────────────
customers = []
for i in range(N_CUSTOMERS):
    customers.append({
        'customer_id': f'C{i+1:04d}',
        'age': np.random.randint(18, 70),
        'gender': random.choice(['Male', 'Female']),
        'region': random.choice(['Accra', 'Kumasi', 'Takoradi', 'Tamale', 'Cape Coast']),
        'signup_date': fake.date_between(start_date='-3y', end_date='-6m'),
        'preferred_device': random.choice(['Mobile', 'Desktop', 'Tablet']),
        'loyalty_tier': random.choice(['Bronze', 'Silver', 'Gold', 'Platinum'])
    })
customers_df = pd.DataFrame(customers)
# print(customers_df)

# ── 3. Browsing Events ─────────────────────────────────────────────
browsing = []
for _ in range(5000):
    browsing.append({
        'customer_id': f'C{np.random.randint(1, N_CUSTOMERS+1):04d}',
        'product_id': f'P{np.random.randint(1, 201):04d}',
        'browse_date': fake.date_time_between(start_date='-1y', end_date='now'),
        'time_spent_seconds': np.random.randint(5, 600),
        'pages_viewed': np.random.randint(1, 15),
        'added_to_cart': random.choice([0, 0, 0, 1])  # 25% add-to-cart rate
    })
browsing_df = pd.DataFrame(browsing)
# print(browsing_df)

# ── 4. Purchase History ────────────────────────────────────────────
purchases = []
for i in range(N_TRANSACTIONS):
    pid = f'P{np.random.randint(1, 201):04d}'
    product = products_df[products_df['product_id'] == pid].iloc[0]
    # 1. products_df['product_id'] == pid creates a Boolean filter checking for our random ID.
    # 2. products_df[...] filters the DataFrame to return only rows matching that specific ID.
    # 3. .iloc[0] extracts the very first matching row object from that filtered subset.
    # This allows the loop to look up real information (like price) about the randomly selected product.
    
    qty = np.random.randint(1, 5)
    purchases.append({
        'transaction_id': f'T{i+1:05d}',
        'customer_id': f'C{np.random.randint(1, N_CUSTOMERS+1):04d}',
        'product_id': pid,
        'purchase_date': fake.date_time_between(start_date='-1y', end_date='now'),
        'quantity': qty,
        'unit_price': product['price'],
        'total_amount': round(qty * product['price'], 2),
        'payment_method': random.choice(['Card', 'Mobile Money', 'Cash on Delivery']),
        'returned': random.choice([0, 0, 0, 0, 1])
    })
purchases_df = pd.DataFrame(purchases)
# print(purchases_df)

# ── 5. Add Noise (missing values + duplicates) ─────────────────────
for col in ['age', 'preferred_device']:
    # This creates a 'Boolean Mask' (an array of True/False values) of the same length as the DataFrame.
    mask = np.random.rand(len(customers_df)) < 0.05 
    customers_df.loc[mask, col] = np.nan

dupes = customers_df.sample(frac=0.02, random_state=1)
# frac=0.02 specifies that exactly 2% of the total dataset should be extracted.
# random_state=1 acts as a fixed seed so that the exact same 2% of rows are copied every time the code runs.

customers_df = pd.concat([customers_df, dupes], ignore_index=True)
# ignore_index=True discards the original row numbers of the duplicates and re-indexes the entire 
# combined table sequentially from 0 down to the new total length, preventing duplicate index numbers.

# ── Sending dataset files to data-bin folder ────────────────────────────────────────────────────

# 1. Get the exact folder where this Python file is saved
DATA_DIR = Path(__file__).resolve().parent

# 2. Target directory for storing the data
TARGET_FOLDER = DATA_DIR / "data-bin"

# 3. Automatically create the folder if it doesn't exist yet
TARGET_FOLDER.mkdir(exist_ok=True)

# ── Save to CSV ────────────────────────────────────────────────────
# Use TARGET_FOLDER / "filename.csv" to combine the directory path and the file name
customers_df.to_csv(TARGET_FOLDER / 'customers.csv', index=False)
products_df.to_csv(TARGET_FOLDER / 'products.csv', index=False)
browsing_df.to_csv(TARGET_FOLDER / 'browsing.csv', index=False)
purchases_df.to_csv(TARGET_FOLDER / 'purchases.csv', index=False)

# print(f"All files successfully saved inside: {TARGET_FOLDER}")

# customers_df.to_csv('customers.csv', index=False)
# products_df.to_csv('products.csv', index=False)
# browsing_df.to_csv('browsing.csv', index=False)
# purchases_df.to_csv('purchases.csv', index=False)

print("Dataset generated!")
print(f"Customers: {len(customers_df)} | Products: {len(products_df)}")
print(f"Browsing: {len(browsing_df)} | Purchases: {len(purchases_df)}")
import couchdb
import pandas as pd
import os

# ── Config ────────────────────────────────────────────────────────
DATA_PATH   = 'data/'
IMPORT_LIMIT = 500

def import_dataset():
    # Connect to CouchDB
    couch = couchdb.Server('http://admin:admin123@localhost:5984/')
    db = couch['ecommerce']

    print("📂 Loading CSV files...")
    orders    = pd.read_csv(os.path.join(DATA_PATH, 'olist_orders_dataset.csv'))
    customers = pd.read_csv(os.path.join(DATA_PATH, 'olist_customers_dataset.csv'))
    items     = pd.read_csv(os.path.join(DATA_PATH, 'olist_order_items_dataset.csv'))

    print("🔗 Merging datasets...")
    df = orders.merge(customers, on='customer_id', how='left')
    df = df.merge(items, on='order_id', how='left')

    # Keep relevant columns only
    df = df[[
        'order_id', 'customer_id', 'order_status',
        'order_purchase_timestamp', 'customer_city',
        'customer_state', 'price', 'product_id'
    ]].dropna().head(IMPORT_LIMIT)

    print(f"📥 Inserting {len(df)} documents into CouchDB...")
    for _, row in df.iterrows():
        db.save(row.to_dict())

    print(f"✅ Successfully imported {len(df)} documents!")

if __name__ == '__main__':
    import_dataset()

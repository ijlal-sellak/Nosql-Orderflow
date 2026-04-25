import couchdb

def create_database():
    couch = couchdb.Server('http://admin:admin123@localhost:5984/')
    db_name = 'ecommerce'

    if db_name not in couch:
        couch.create(db_name)
        print(f"✅ Database '{db_name}' created successfully!")
    else:
        print(f"⚠️  Database '{db_name}' already exists.")

if __name__ == '__main__':
    create_database()

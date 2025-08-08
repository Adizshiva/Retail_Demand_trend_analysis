import pandas as pd
from sqlalchemy import create_engine ,text

#df = pd.read_csv('orders.csv')
df = pd.read_csv('orders.csv',na_values=['Not Available','unknown'])

#print(df.head(20))

print(df['Ship Mode'].unique())

#print(df.columns)
#print(df.columns.str.lower())
df.columns=df.columns.str.lower()

df.columns = df.columns.str.replace(' ','_')
print(df.columns)

# step deriving discount columns
print(df['list_price']*df['discount_percent']*.01)
df['discount']=df['list_price']*df['discount_percent']*.01

#step calculating sales
df['sale_price']=df['list_price']-df['discount']
print(df)

#calculate profit
df['profit']=df['sale_price']-df['cost_price']
print(df)

# converting datatypes - order data from object to datetime
print(df.dtypes)
#print(pd.to_datetime(df['order_date'],"format=%Y-%m-%d"))

df['order_date']= pd.to_datetime(df['order_date'],format="%Y-%m-%d")
print(df.dtypes)

# dropping unnecessary colums
df.drop(columns=['list_price','cost_price','discount_percent'],inplace=True)
print(df)






username = 'root'
password = '1234'  
host = 'localhost'
port = '3306'
database = 'test_db'

# Use no database in URL, just connect to MySQL server
engine = create_engine("mysql+pymysql://root:1234@127.0.0.1:3306")

try:
    with engine.connect() as conn:
        conn.execute(text("CREATE DATABASE IF NOT EXISTS test_db"))
        print("✅ Database 'test_db' created or already exists.")
except Exception as e:
    print("❌ Failed to create database:", e)




# Connect to the specific database now
engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}")

try:
    df.to_sql(name='orders', con=engine, if_exists='replace', index=False)
    print("✅ Data uploaded to MySQL successfully!")
except Exception as e:
    print("❌ Upload failed:", e)
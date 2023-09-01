import pandas as pd
import psycopg2

# function to connect to redshift

def connect_to_redshift(dbname, host, port, user, password):
    """Method that connects to redshift. This gives a warning so will look for another solution"""

    connect = psycopg2.connect(
        dbname=dbname, host=host, port=port, user=user, password=password
    )

    print("connection to redshift made")

    return connect


# function to extract, join and clean transactional data

def extract_transactional_data(dbname, host, port, user, password):
    """
        This function:
        Extracts from redshift online_transaction and stock_description tables
        Selects everything from online_transaction table and description from stock description table.
        Filters on where customer_id is not equal to ‘’
        Filters on where stock_code not in BANK CHARGES, POST, D, M, CRUK
        If the description is null replaces it with 'Unknown'
        Fixes the invoice_date field from object to datetime
        Removes '?' from stock codes

        @param connection to redshift

        @return a DataFrame of joined cleaned tables
       """

    # connect to redshift
    connect = connect_to_redshift(dbname, host, port, user, password)

    query = '''SELECT t1.invoice, 
                    t1.stock_code, 
                    t1.quantity, 
                    t1.price, 
                    t1.customer_id, 
                    t1.country,
                    t1.quantity*t1.price as total_order_value,
                    CASE WHEN t2.description IS NULL THEN 'Unknown' 
                        ELSE description END AS description,
                        CAST(t1.invoice_date AS datetime) AS invoice_date
                FROM bootcamp.online_transactions t1
                LEFT JOIN (SELECT *
                         FROM bootcamp.stock_description
                         WHERE description <> '?') t2 ON t1.stock_code = t2.stock_code
                         WHERE t1.stock_code NOT IN ('BANK CHARGES', 'POST', 'D', 'M', 'CRUK')
                         AND customer_id <> '';'''

    # read the dataframe and show 5 top lines
    joined_table_clean = pd.read_sql(query, connect)

    print('Preview of the online transactions data: ',joined_table_clean.head())

    connect.close()

    return joined_table_clean
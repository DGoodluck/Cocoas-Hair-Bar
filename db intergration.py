import psycopg2
from psycopg2.errors import UniqueViolation
from bs4 import BeautifulSoup
import requests

def connect_to_db():
    return psycopg2.connect(host='127.0.0.1', dbname='hair services', user='postgres', password='L$zj%WU', port='5433')

# def insert_into_table(cursor, num, name, category, price, description, language):
#     try:
#         cursor.execute("""
#             INSERT INTO services (id, name, category, price, description, language)
#             VALUES (%s, %s, %s, %s, %s, %s)
#         """, (num, name, category, price, description, language))
#         num += 1
        
#     except UniqueViolation:
#         print("Values are already created")
#         conn.rollback()
#     return num

# url = 'https://www.cocoashairbar.com/services/fr'
# response = requests.get(url)
# html_content = response.text

# # Assuming 'html_content' contains the HTML content of your page
# soup = BeautifulSoup(html_content, 'html.parser')

# # Find all item-menu containers
# item_menus = soup.find_all('div', class_='item-menu container')

def select_data(cursor):
    cursor.execute("SELECT * FROM services WHERE language = 'en'")
    for row in cursor.fetchall():
        print(row)
    
        
if __name__ == "__main__":
    conn = connect_to_db()
    cursor = conn.cursor()
    
    
    # num = 113

    # for item_menu in item_menus:
    #     # Get the category
    #     category = item_menu.find('span', class_='hover-underline-animation').text

    #     # Get all menu blocks within the current item-menu container
    #     menu_blocks = item_menu.find_all('div', class_='menu-block')

    #     for menu_block in menu_blocks:
    #         # Get the title
    #         title = menu_block.find('div', class_='menu-title newprice').text

    #         # Get the price and remove the dollar sign
    #         price = menu_block.find('div', class_='price').text.replace('$', '')

    #         # Get the description
    #         description = menu_block.find('p', class_='p2 pricedetail').text
            
    #         language = 'fr'

    #         # Insert the data into the table
    #         num = insert_into_table(cursor, num, title, category, price, description, language)
    
    select_data(cursor)
    
    conn.commit()
    cursor.close()
    conn.close()
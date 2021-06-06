import pymysql
from config import host, user, password, db_name, port

try:
    connection = pymysql.connect(
        host = host,
        port = port,
        user = user,
        password = password,
        database = db_name,
        cursorclass = pymysql.cursors.DictCursor
    )
    print("success")

    try:
        def first_menu_func():
            stop = True
            while stop:
                first_menu = int(input("Type interested number:\n"
                               "Clients - 1\n"
                               "Products — 2\n"
                               "Orders — 3\n"
                               "Overview — 4\n"
                               "Stop — 5\n"))
                if first_menu == 1:
                    print('--Сlients--\n')
                    clients = int(input("What do you want to do?\n"
                            "Add new client — 1\n"
                            "Delete client — 2 \n"
                            "Update client info — 3\n"
                            "Stop — 4\n"
                            "Start again — 5\n"))
                    if clients == 1:
                        print('--Add new client--')
                        print("Fill in the fields\n"
                              "Skip one of them by pressing ENTER\n")
                        name = input("Type new clients name: ")
                        surname = input("Type new clients surname: ")
                        phone = input("Type new clients phone(xxx-xxx-xx-xx): ")
                        email = input("Type new clients email: ")
                        address = input("Type new clients address: ")

                        with connection.cursor() as cursor:
                            add_client_query = "INSERT INTO clients (name, surname, phone, email,address) VALUES ('%s', '%s', '%s', '%s', '%s');" % (name, surname, phone, email, address)
                            cursor.execute(add_client_query)
                            connection.commit()
                            print('--Client succesfully added--')
                    elif clients == 2:
                        print('--Delete client--')
                        id_input = int(input("Type id of a client you want to delete: "))
                        with connection.cursor() as cursor:
                            delete_query = "DELETE FROM clients WHERE clients_id = '%s';"
                            cursor.execute(delete_query, id_input)
                            connection.commit()
                            print("--Client deleted successfully!--")
                    elif clients == 3:
                        print('--Update client info--')
                        print()
                        updated_client_id = int(input("Type id of a client you want to update: "))
                        update_client_column = input('Type what info you want to update:\n'
                              '(name, surname, phone, email,address)\n')
                        updated_info = input("Type updated info for this client: ")
                        update_data = [update_client_column, updated_info, updated_client_id]
                        with connection.cursor() as cursor:
                            update_query = "UPDATE clients SET %s = '%s' WHERE clients_id = '%s';" % (update_client_column, updated_info, updated_client_id)
                            cursor.execute(update_query)
                            connection.commit()
                            print("--Info updated succesfully!--")
                    elif clients == 4:
                        print('--Program stopped--')
                        stop = False
                    elif clients == 5:
                        print('--Returning to menu 1--')
                    else:
                        print("--No such number, try again!--")
                elif first_menu == 2:
                    print('--Сlients--\n')
                    products = int(input("What do you want to do?\n"
                                        "Add new product — 1\n"
                                        "Delete product — 2 \n"
                                        "Update product specs — 3\n"
                                        "Stop — 4\n"
                                        "Start again — 5\n"))
                    if products == 1:
                        print('--Add new product--')
                        product_name = input("Type new products name: ")
                        with connection.cursor() as cursor:
                            add_product_query = "INSERT INTO products (product_name) VALUES ('%s');" % (product_name)
                            cursor.execute(add_product_query)
                            connection.commit()
                        # print('Do you want to add specs for this product?')
                        # add_specs = int(input("Yes — 1\n"
                        #                       "No — 2\n"))
                        # if add_specs == 1:
                        #     print("Fill in the fields\n"
                        #           "Skip one of them by pressing ENTER\n")
                        #     cpu = input("Type new products CPU: ")
                        #     gpu = input("Type new products GPU: ")
                        #     cpu_cores = input("Type new products CPU cores: ")
                        #     ram = input("Type new products RAM: ")
                        #     storage_type = input("Type new products storage type(SSD/HDD): ")
                        #     storage_capacity = input("Type new products storage capacity(in Gb): ")
                        #     display_size = input("Type new products display size: ")
                        #     display_resolution = input("Type new products display resolution(AxB): ")
                        #     year = input("Type production year: ")
                        #     price = input("Type new products price(in USD): ")
                        #     quantity = input("Type quantity in stock: ")
                        #     stock = input("Is it in stock?(Yes-1, No-0): ")
                        #     with connection.cursor() as cursor:
                        #         add_client_query = "INSERT INTO product_specs (cpu, gpu, cpu_cores, ram, storage_type, storage_capacity, display_size, display_resolution, year) " \
                        #                            "VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s') WHERE MAX(product_id);" % (
                        #         cpu, gpu, cpu_cores, ram, storage_type, storage_capacity, display_size, display_resolution, year)
                        #         cursor.execute(add_client_query)
                        #     with connection.cursor() as cursor:
                        #         add_product_query = "INSERT INTO product_store (price, quantity, stock) VALUES ('%s', '%s', '%s');" % (
                        #             price, quantity, stock)
                        #         cursor.execute(add_product_query)
                        #         connection.commit()
                        #         print('--Product succesfully added--')

                            print('--product succesfully added--')
                    elif products == 2:
                        print('--Delete product--')
                        id_input = int(input("Type id of a product you want to delete: "))
                        with connection.cursor() as cursor:
                            delete_query = "DELETE FROM products WHERE products_id = '%s';" % (id_input)
                            cursor.execute(delete_query)
                            connection.commit()
                            print("--product deleted successfully!--")
                    elif products == 3:
                        print('--Update product specs--')
                        print()
                        updated_product_id = int(input("Type id of a product you want to update: "))
                        update_product_column = input('Type what info you want to update:\n'
                                                     '(name, cpu, gpu, cpu_cores, ram, storage_type, storage_capacity,\ndisplay_size, display_resolution, year\nprice,quantity, stock)')
                        updated_info = input("Type updated info for this product: ")

                        if update_product_column == "name":
                            with connection.cursor() as cursor:
                                update_query = "UPDATE products SET %s = '%s' WHERE product_id = '%s';" % (
                                    update_product_column, updated_info, updated_product_id)
                                cursor.execute(update_query)
                                connection.commit()
                                print("--Info updated succesfully!--")
                        elif update_product_column == ("cpu" or 'gpu'or'cpu_cores'or 'ram'or "storage_type"or "storage_capacity"or "display_size"or "display_resolution"or "year"):
                            with connection.cursor() as cursor:
                                update_query = "UPDATE product_specs SET %s = '%s' WHERE product_id = '%s';" % (
                                    update_product_column, updated_info, updated_product_id)
                                cursor.execute(update_query)
                                connection.commit()
                                print("--Info updated succesfully!--")
                        elif update_product_column == ("price" or"quantity" or "stock"):
                            with connection.cursor() as cursor:
                                update_query = "UPDATE product_store SET '%s' = '%s' WHERE product_id = '%s';" % (
                                    update_product_column, updated_info, updated_product_id)
                                cursor.execute(update_query)
                                connection.commit()
                                print("--Info updated succesfully!--")
                        else:
                            print("--No spec like that, try again!--")
                    elif products == 4:
                        print('--Program stopped--')
                        stop = False
                    elif products == 5:
                        print('--Returning to menu 1--')
                    else:
                        print("--No such number, try again!--")
                elif first_menu == 3:
                    print('--Orders--')
                    orders = int(input("What do you want to do?\n"
                                         "Add new order — 1\n"
                                         "Delete order — 2 \n"
                                         "Update order info — 3\n"
                                         "Stop — 4\n"
                                         "Start again — 5\n"))
                    if orders == 1:
                        print('--Add new order--')
                        print("Fill in the fields\n"
                              "Skip one of them by pressing ENTER\n")
                        order_client_id = input("Who ordered?(client ID): ")
                        order_date_i = input("Order date: ")
                        comments_i = str(input("Any comments?: "))
                        shipped_date_i = input("Shipped date(press ENTER if not yet) YYYY_MM_DD:  ")
                        with connection.cursor() as cursor:
                            add_order_query = "INSERT INTO orders (clients_id, order_date, comments, shipped_date) VALUES ('%s', '%s', '%s', '%s');" % (
                            order_client_id, order_date_i, comments_i, shipped_date_i)
                            cursor.execute(add_order_query)
                            connection.commit()
                            print('--Order succesfully added--')

                        # add_product_order = int(input("Do you want to add products to this order?\n"
                        #                               "Yes — 1\n"
                        #                               "No — 2\n"))
                        # if add_product_order == 1:
                        #     order_items_id = input("Type id ")
                        #     order_product_id = input('What was ordered?(product ID): ')
                        #     order_quantity = input('Quantity: ')
                        #     order_sum = input('Sum: ')
                        #     with connection.cursor() as cursor:
                        #         add_order_query = "INSERT INTO order_items (product_id, quantity, Sum) VALUES ('%s', '%s', '%s');" % (
                        #             order_product_id, order_quantity, order_sum)
                        #         cursor.execute(add_order_query)
                        #         connection.commit()
                        #         print('--Products succesfully added to the order--')
                        # elif add_product_order == 2:
                        #     print('--Order succesfully added--')
                    elif orders == 2:
                        print('--Delete order--')
                        id_input = int(input("Type id of a order you want to delete: "))
                        with connection.cursor() as cursor:
                            delete_query = "DELETE FROM orders WHERE order_id = '%s';" % (id_input)
                            cursor.execute(delete_query)
                            connection.commit()
                            print("--Order deleted successfully!--")
                    elif orders == 3:
                        print('--Update order info--')

                        updated_order_id = int(input("Type id of a order you want to update: "))
                        update_order_menu = int(input('What do you want to be updated?\n'
                                                    'Order info — 1\n'
                                                    'Order items info — 2\n'))
                        if update_order_menu == 1:
                            update_order_column = input("Type what info you want update?\n"
                                                        "clients_id, order_date, comments, shipped_date\n"
                                                        "One at a time.\n")
                            updated_info = input("Type updated info for this order: ")

                            with connection.cursor() as cursor:
                                update_query = "UPDATE orders SET %s = '%s' WHERE order_id = '%s';" % (
                                update_order_column, updated_info, updated_order_id)
                                cursor.execute(update_query)
                                connection.commit()
                                print("--Order info updated succesfully!--")
                        elif update_order_menu == 2:
                            update_order_it_column = input("Type what info you want update?\n"
                                                        "product_id, quantity, Sum\n"
                                                        "One at a time.\n")
                            with connection.cursor() as cursor:
                                updated_info = input("Type updated info for this order: ")
                                update_query = "UPDATE order_items SET %s = '%s' WHERE order_id = '%s';" % (
                                    update_order_it_column, updated_info, updated_order_id)
                                cursor.execute(update_query)
                                connection.commit()
                                print("--Order items info updated succesfully!--")
                        else:
                            print("--No such number, try again!--")
                    elif orders == 4:
                        print('--Program stopped--')
                        stop = False
                    elif orders == 5:
                        print('--Returning to menu 1--')
                    else:
                        print("--No such number, try again!--")
                elif first_menu == 4:
                    print('--Overview--\n')
                    overview = int(input("What do you want to do?\n"
                                         "Clients overview — 1\n"
                                         "Products overview — 2 \n"
                                         "Orders overview — 3\n"
                                         "Stop — 4\n"
                                         "Start again — 5\n"))
                    if overview == 1:
                        print("--Clients overview--")
                        clients_overview = int(input("What do you want to do?\n"
                                                     "See stats — 1\n"
                                                     "See all clients info — 2\n"
                                                     "Stop — 4\n"
                                                     "Start again — 5\n"))
                        if clients_overview == 1:
                            print("--See stats--")
                            clients_stats = int(input("What stat do you want to see?\n"
                                                         "Most active client — 1\n"
                                                         "Least active — 2\n"))
                            if clients_stats == 1:
                                with connection.cursor() as cursor:
                                    select_all_rows = "select clients_id,COUNT(clients_id) AS Orders_amount from orders group by clients_id order by Orders_amount DESC;"
                                    cursor.execute(select_all_rows)
                                    rows = cursor.fetchall()
                                    for row in rows:
                                        print(row)
                            elif clients_stats == 2:
                                with connection.cursor() as cursor:
                                    select_all_rows = "select clients_id,COUNT(clients_id) AS Orders_amount from orders group by clients_id order by Orders_amount ASC;"
                                    cursor.execute(select_all_rows)
                                    rows = cursor.fetchall()
                                    for row in rows:
                                        print(row)
                            else:
                                print("--No such number, try again!--")
                        elif clients_overview == 2:
                            print("--See all clients info--")
                            with connection.cursor() as cursor:
                                cursor.execute("SELECT * FROM clients")
                                rows = cursor.fetchall()
                                for row in rows:
                                    print(row)
                        elif clients_overview == 4:
                            print('--Program stopped--')
                            stop = False
                        elif clients_overview == 5:
                            print('--Returning to menu 1--')
                        else:
                            print("--No such number, try again!--")
                    elif overview == 2:
                        print("--Products overview--")
                        products_overview = int(input("What do you want to do?\n"
                                                     "See stats — 1\n"
                                                     "See all products info — 2\n"))
                        if products_overview == 1:
                            print("--See stats--")
                            products_stats = int(input("What stat do you want to see?\n"
                                                      "Most sold products — 1\n"
                                                      "Least sold — 2\n"))
                            if products_stats == 1:
                                with connection.cursor() as cursor:
                                    select_all_rows = "select product_id,COUNT(product_id) AS Products_sold from order_items group by product_id order by Products_sold DESC;"
                                    cursor.execute(select_all_rows)
                                    rows = cursor.fetchall()
                                    for row in rows:
                                        print(row)
                            elif products_stats == 2:
                                with connection.cursor() as cursor:
                                    select_all_rows = "select product_id,COUNT(product_id) AS Products_sold from order_items group by product_id order by Products_sold ASC;"
                                    cursor.execute(select_all_rows)
                                    rows = cursor.fetchall()
                                    for row in rows:
                                        print(row)
                        elif products_overview == 2:
                            print("--See all products info--")
                            with connection.cursor() as cursor:
                                cursor.execute("SELECT * FROM product_specs")
                                rows = cursor.fetchall()
                                for row in rows:
                                    print(row)
                        else:
                            print("--No such number, try again!--")
                    elif overview == 3:
                        print("--Orders overview--")
                        orders_overview = int(input("What do you want to do?\n"
                                                      "See stats — 1\n"
                                                      "See all orders made — 2\n"
                                                      "See all orders made by date — 3\n"))
                        if orders_overview == 1:
                            print("--See stats--")
                            orders_stats = int(input("What stat do you want to see?\n"
                                                       "Most active day — 1\n"
                                                       "Least active day — 2\n"))
                            if orders_stats == 1:
                                with connection.cursor() as cursor:
                                    select_all_rows = "select order_date,COUNT(order_date) AS Amount_of_orders_at_date from orders " \
                                                      "group by order_date order by Amount_of_orders_at_date DESC;"
                                    cursor.execute(select_all_rows)
                                    rows = cursor.fetchall()
                                    for row in rows:
                                        print(row)
                            elif orders_stats == 2:
                                with connection.cursor() as cursor:
                                    select_all_rows = "select order_date,COUNT(order_date) AS Amount_of_orders_at_date from orders " \
                                                      "group by order_date order by Amount_of_orders_at_date ASC;"
                                    cursor.execute(select_all_rows)
                                    rows = cursor.fetchall()
                                    for row in rows:
                                        print(row)
                        elif orders_overview == 2:
                            print("--See all orders info--")
                            with connection.cursor() as cursor:
                                cursor.execute("SELECT * FROM orders")
                                rows = cursor.fetchall()
                                for row in rows:
                                    print(row)
                        elif orders_overview == 3:
                            print("--See all orders made by date--")
                            orders_by_date = int(input("What do you want to see?\n"
                                                       "Orders on specific date — 1\n"
                                                       "Orders from new to old — 2\n"
                                                       "Orders from old to new — 3\n"))
                            if orders_by_date == 1:
                                order_date_input = input("Input date YYYY-MM-DD: ")
                                with connection.cursor() as cursor:
                                    output_by_date = cursor.execute("SELECT * FROM orders WHERE order_date = '%s'" %(order_date_input))
                                    if output_by_date > 0:
                                        rows = cursor.fetchall()
                                        for row in rows:
                                            print(row)
                                    else:
                                        print("--There are no orders for this date--")
                            elif orders_by_date == 2:
                                with connection.cursor() as cursor:
                                    cursor.execute("SELECT * FROM orders ORDER BY order_date DESC;")
                                    rows = cursor.fetchall()
                                    for row in rows:
                                        print(row)
                            elif orders_by_date == 3:
                                with connection.cursor() as cursor:
                                    cursor.execute("SELECT * FROM orders ORDER BY order_date ASC;")
                                    rows = cursor.fetchall()
                                    for row in rows:
                                        print(row)
                        else:
                            print("--No such number, try again!--")
                    elif overview == 4:
                        print('--Program stopped--')
                        stop = False
                    elif overview == 5:
                        print('--Returning to menu 1--')
                    else:
                        print("--No such number, try again!--")
                elif first_menu == 5:
                    stop = False
                else:
                    print("--No such number, try again!--")
        first_menu_func()
        # cursor = connection.cursor()

        # create table
        # with connection.cursor() as cursor:
        #     create_table_query = "CREATE TABLE `users`(id int AUTO_INCREMENT," \
        #                          " name varchar(32)," \
        #                          " password varchar(32)," \
        #                          " email varchar(32), PRIMARY KEY (id));"
        #     cursor.execute(create_table_query)
        #     print("Table created successfully")

        # insert data
        # with connection.cursor() as cursor:
        #     insert_query = "INSERT INTO `users` (name, password, email) VALUES ('Anna', 'qwerty', 'anna@gmail.com');"
        #     cursor.execute(insert_query)
        #     connection.commit()

        # with connection.cursor() as cursor:
        #     insert_query = "INSERT INTO `users` (name, password, email) VALUES ('Victor', '123456', 'victor@gmail.com');"
        #     cursor.execute(insert_query)
        #     connection.commit()
        #
        # with connection.cursor() as cursor:
        #     insert_query = "INSERT INTO `users` (name, password, email) VALUES ('Oleg', '112233', 'olegan@mail.ru');"
        #     cursor.execute(insert_query)
        #     connection.commit()

        # with connection.cursor() as cursor:
        #     insert_query = "INSERT INTO `users` (name, password, email) VALUES ('Oleg', 'kjlsdhfjsd', 'ole2gan@mail.ru');"
        #     cursor.execute(insert_query)
        #     connection.commit()
        #
        # with connection.cursor() as cursor:
        #     insert_query = "INSERT INTO `users` (name, password, email) VALUES ('Oleg', '889922', 'olegan3@mail.ru');"
        #     cursor.execute(insert_query)
        #     connection.commit()

        # update data
        # with connection.cursor() as cursor:
        #     update_query = "UPDATE `users` SET password = 'xxxXXX' WHERE name = 'Oleg';"
        #     cursor.execute(update_query)
        #     connection.commit()

        # delete data
        # with connection.cursor() as cursor:
        #     delete_query = "DELETE FROM `users` WHERE id = 5;"
        #     cursor.execute(delete_query)
        #     connection.commit()

        # drop table
        # with connection.cursor() as cursor:
        #     drop_table_query = "DROP TABLE `users`;"
        #     cursor.execute(drop_table_query)

        # select all data from table
        # # with connection.cursor() as cursor:
        #     select_all_rows = "SELECT *  FROM products AS pr JOIN product_specs AS ps ON pr.product_id=ps.product_id"
        #     cursor.execute(select_all_rows)
        #     # cursor.execute("SELECT * FROM `users`")
        #     rows = cursor.fetchall()
        #     for row in rows:
        #         print(row)
        #     print("#" * 20)
    finally:
        connection.close()

except Exception as ex:
    print("refused")
    print(ex)
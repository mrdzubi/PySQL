import psycopg2

def create_db(cur):
    cur.execute('''CREATE TABLE if not exists client(
    client_id SERIAL PRIMARY KEY,
    first_name VARCHAR(20) NOT NULL,
    last_name VARCHAR(40) NOT NULL,
    email VARCHAR(60) NOT NULL
    );''')
    cur.execute('''CREATE TABLE if not exists phone(
    phone_id SERIAL PRIMARY KEY,
    client_id INTEGER NOT NULL REFERENCES client(client_id),
    number VARCHAR(12) UNIQUE
    );''')
    conn.commit()

def add_client(cur, first_name, last_name, email):
    cur.execute('''
    INSERT INTO client(first_name, last_name, email) values (%s,%s,%s);
    ''',(first_name, last_name, email))

def add_phone(cur, client_id, phone_number):
    cur.execute('''
    INSERT INTO phone(client_id, number) values (%s, %s);
    ''',(client_id, phone_number))

def change_info(cur):
    print('Выберите пункт в меню, который хотите изменить:\n'
          '1.Имя клиента\n'
          '2.Фамилия килента\n'
          '3.Электронная почта клиента\n'
          '4. Номер телефона клиента')
    while True:
        number_main = int(input())
        if number_main == 1:
            id_client = int(input('Введите id клиента: '))
            name_client = input('Введите новое имя клиента: ')
            cur.execute('''
            UPDATE clientnumber SET first_name=%s where client_id=%s;
            ''',(name_client,id_client))
            break
        elif number_main == 2:
            id_client = int(input('Введите id клиента: '))
            last_name_client = input('Введите новую фамилию клиента: ')
            cur.execute('''
                        UPDATE clientnumber SET last_name=%s where client_id=%s;
                        ''', (last_name_client, id_client))
            break
        elif number_main == 3:
            id_client = int(input('Введите id клиента: '))
            email_client = input('Введите новый email клиента: ')
            cur.execute('''
                        UPDATE clientnumber SET email=%s where client_id=%s;
                        ''', (email_client, id_client))
            break
        elif number_main == 4:
            old_number_client = int(input('Введите старый номер клиента: '))
            new_number_client = input('Введите новый телефон клиента: ')
            cur.execute('''
                        UPDATE phone SET number=%s where number=%s;
                        ''', (new_number_client, old_number_client))
            break
        else:
            print('Неправильный Ввод команды')

def delete_phone(cur):
    delete_phone = input('Введите номер телефона, который хотите удалить: ')
    cur.execute('''
    DELETE FROM phone WHERE number = %s;
    ''',(delete_phone))

def delete_client(cur):
    id_delete = int(input('Введите id клиента, которого хотите удалить: '))
    cur.execute('''
    DELETE FROM phone WHERE client_id = %s;
    DELETE FROM client WHERE client_id = %s;
    '''(id_delete,id_delete))

def find_client(cur):
    print('Выберите пункт в меню,по которому хотите найти клиента:\n'
          '1.Имя клиента\n'
          '2.Фамилия килента\n'
          '3.Электронная почта клиента\n'
          '4.Номер телефона клиента')
    number_main = int(input())
    while True:
        if number_main == 1:
            name = input('Введите имя клиента: ')
            cur.execute('''
            SELECT id, first_name, last_name, email, number from client as cl
            JOIN LEFT phone as ph ON ph.phone_id = cl.id
            WHERE first_name = %s;  
            ''',(name))
            print(cur.fetchall())
        elif number_main == 2:
            last_name = input('Введите фамилию клиента: ')
            cur.execute('''
            SELECT id, first_name, last_name, email, number from client as cl
            JOIN LEFT phone as ph ON ph.phone_id = cl.id
            WHERE last_name = %s;  
            ''',(last_name))
            print(cur.fetchall())
        elif number_main == 3:
            email = input('Введите почту клиента: ')
            cur.execute('''
            SELECT id, first_name, last_name, email, number from client as cl
            JOIN LEFT phone as ph ON ph.phone_id = cl.id
            WHERE email = %s;  
            ''',(email))
            print(cur.fetchall())
        elif number_main == 4:
            phone = input('Введите номер телефона клиента: ')
            cur.execute('''
            SELECT id, first_name, last_name, email, number from client as cl
            JOIN LEFT phone as ph ON ph.phone_id = cl.id
            WHERE number = %s;  
            ''',(phone))
            print(cur.fetchall())
        else:
            print('Неправильный Ввод команды')




with psycopg2.connect(database="clientnumber", user='postgres', password='89246638407Ss') as conn:
    with conn.cursor as cur:
        create_db(cur)


conn.close()
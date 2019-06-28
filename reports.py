#!/usr/bin/python

import sqlite3
from sqlite3 import Error
import datetime

# What we want here?
# Ticket number, Client name, Close at , Requirer email, title, request, time spent, closed comment.
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        conn.text_factory = str
        return conn
    except Error as e:
        print(e)

    return None

def select_all_users(conn):
    """
    Query all rows in the users table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT distinct(first_name) FROM users")

    rows = cur.fetchall()

    for row in rows:
        print(row)

def select_all_comments_closed_by_ticket(conn, tkt):
    """
    Query all rows in the users table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    #cursor = cur.execute("SELECT * FROM comments WHERE is_public = 't'")
    #names = [description[0] for description in cursor.description]
    cur.execute("SELECT body FROM comments WHERE is_public = 't' AND body LIKE '%Ticket closed:%' AND ticket_id = " + str(tkt))
    #print(names)
    rows = cur.fetchall()

    #for row in rows:
        #print(row)
    return rows

def select_all_clients(conn):
    """
    Query all rows in the clients name table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT distinct(c_clientes) FROM tickets")

    rows = cur.fetchall()

    #for row in rows:
    #    print(row)
    return rows

def select_closed_tasks(conn):
    """
    Query tickets by user
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT tickets.closed_at, tickets.c_clientes, users.first_name from tickets inner join users ON tickets.assigned_to = users.id where tickets.status='closed'")
    rows = cur.fetchall()

    for row in rows:
        print(row)

def select_ticket_work_time_spent(conn, tkt):
    """
    Query tickets by user
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    #cursor = cur.execute("SELECT * FROM ticket_work")
    #names = [description[0] for description in cursor.description]
    #print(names)
    cur.execute("SELECT ticket_work.time_spent, users.first_name from ticket_work inner join users ON ticket_work.user_id = users.id WHERE ticket_work.ticket_id = " + str(tkt))
    rows = cur.fetchall()

    #for row in rows:
    #    print(row)
    return rows

def select_closed_tasks_by_client(conn, client, client_t, start_date, end_date, fee):
    """
    Query tickets by user
    :param conn: the Connection object
    :return:
    :The filter for dates, contains the start_date but not the end_date
    """
    cur = conn.cursor()
    #cursor = cur.execute("SELECT * FROM tickets")
    #names = [description[0] for description in cursor.description]
    #print(names)
    cur.execute("SELECT tickets.id, tickets.c_clientes, tickets.closed_at, users.email, tickets.summary, tickets.description, tickets.c_tipo_de_cliente from tickets inner join users ON tickets.created_by = users.id where tickets.status='closed' AND tickets.c_clientes = '" + str(client) + "' AND tickets.c_tipo_de_cliente = '" + str(client_t) + "' AND tickets.closed_at BETWEEN '"+ str(start_date) +"' AND '" + str(end_date) + "'")
    #cur.execute("SELECT created_by FROM tickets WHERE c_clientes = 'A3'")
    rows = cur.fetchall()
    total_time_spent = 0
    report = []
    for row in rows:
        closed_comment = select_all_comments_closed_by_ticket(conn,row[0])
        time_spent = select_ticket_work_time_spent(conn, row[0])
        for time, name in time_spent:
            total_time_spent += time
            seconds = int(total_time_spent)
            minutes, seconds = divmod(seconds, 60)
            hours, minutes = divmod(minutes, 60)
            try:
                comment = closed_comment[0]
            except IndexError:
                comment = ('null',)
            tmp_report = row + comment + (hours, minutes)

        report.append(tmp_report)
        #print(row,"Closed Comment: ",closed_comment,"Time Spent: ", time_spent)
    #seconds = int(total_time_spent)
    #minutes, seconds = divmod(seconds, 60)
    #hours, minutes = divmod(minutes, 60)
    #print("Total Time Spent: ", str(hours) +" hours and " + str(minutes) + " minutes")
    #total_value = hours * fee
    #total_value += minutes * (fee/60)
    #print("Total due to pay: ", "%.2f" % total_value)
    return report

def select_all(conn, table):
    """
    Query tickets by user
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    #cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
    #cur.execute("SELECT * FROM '" + table + "'")
    cursor = cur.execute("SELECT * FROM users")
    names = [description[0] for description in cursor.description]
    print(names)
    #rows = cur.fetchall()

    #for row in rows:
    #    print(row)

def main():
    database = "spiceworks_prod.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        #print("1. Query all users:")
        #select_all_users(conn)
        #select_ticket_work_time_spent(conn, 1222)
        #select_all_comments(conn)
        #select_all_comments_closed_by_ticket(conn, )
        #select_all(conn, "users")

        #print("2. Query all clients")
        result = select_closed_tasks_by_client(conn,'PEC', 'Fixo', '2018-09-01','2018-10-01', 80)
        #for line in result:
            #print(line[8])
        #clients = select_all_clients(conn)
        #total_total_total = 0
        #for cli in clients:
        #    total_total_total += select_closed_tasks_by_client(conn,cli[0], 'Fixo', '2018-01-01','2018-12-01', 80)

        #print("Toma ai o seu total total:", total_total_total)

#if __name__ == '__main__':
#    main()

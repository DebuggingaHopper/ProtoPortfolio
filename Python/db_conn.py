import sys
import psycopg2


def main():
    # Establish a connection to the database
    try:
        conn = psycopg2.connect(dbname="fish_tournament", user="Admin", password="F1$hP0tat0b0oze", host="192.168.12.214", port="32769")
    except psycopg2.Error as e:
        print("Connection to database failed:", e)
        return 1

    print("Connected to database successfully!")

    # Close the connection
    conn.close()
    return 0

if __name__ == "__main__":
    main()

    sys.exit(0)
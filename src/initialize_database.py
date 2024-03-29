from database_connection import get_database_connection


def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute(
        """
        drop table if exists ot;
    """
    )

    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute(
        """
        create table ot (
            id text primary key,
            mycolumn text
        );
    """
    )

    connection.commit()


def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)

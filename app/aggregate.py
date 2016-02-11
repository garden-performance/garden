# coding: utf8

from django.db import connection


def get_all_device_info():
    sql = """
        SELECT
            *
        FROM
            app_devices
        ORDER BY
            device_id
    """
    cursor = connection.cursor()
    cursor.execute(sql)
    for row in cursor.fetchall():
        yield row

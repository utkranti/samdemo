from abc import ABC,abstractmethod

class Service(ABC):

    @abstractmethod
    def fetch_single_data(self,cid):
        pass

    @abstractmethod
    def fetch_all_data(self):
        pass

    @abstractmethod
    def insert_data(self, cust):
        pass

    @abstractmethod
    def update_data(self, cust):
        pass

    @abstractmethod
    def delete_data(self, cid):
        pass

class ExcelConnection(Service):
    pass

from final_persist.databaseutil import *
from final_persist.sqlqueries import *
from final_persist.model import *
import pymysql


class Databaseop(Service):

    conn = None

    def __init__(self):
        Databaseop.conn = get_connection()

    def fetch_single_data(self, cid):
        channel = generic_way()
        # conn = get_connection()
        # channel = conn.cursor()
        channel.execute(FETCH_SINGLE_QUERY.format(cid))
        print(channel.fetchone())
        # conn.close()
        conn.commit()





    def fetch_all_data(self):
        conn = get_connection()
        channel = conn.cursor()
        channel.execute(FETCH_ALL_QUERY)
        res = channel.fetchall()
        print(res)
        # conn.close()
        conn.commit()


    def insert_data(self,emp):
        # conn = get_connection()
        # channel = conn.cursor()
        generic_way().execute(INSERT_QUERY.format(emp.empId,emp.empName,emp.empSalary))
        conn.commit()

    def update_data(self,emp):
        conn = get_connection()
        channel = conn.cursor()
        channel.execute(UPDATE_QUERY.format(emp.empName,emp.empSalary,emp.empId))
        conn.commit()
        # generic_way(UPDATE_QUERY.format(emp.empName,emp.empSalary,emp.empId))
        # channel  = generic_way()
        # channel.execute(UPDATE_QUERY.format(emp.empName,emp.empSalary,emp.empId))
        # channel.commit()
        # conn.close()

    def delete_data(self, eid):
        conn = get_connection()
        channel = conn.cursor()
        channel.execute(DELETE_QUERY.format(eid))
        conn.commit()

    def allinone(self, query):
        generic_way().execute(query).commit()




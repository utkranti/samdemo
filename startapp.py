from final_persist.databaseutil import *
from final_persist.operations import *
from final_persist.model import Employee
from final_persist.sqlqueries import *

if __name__ == '__main__':
    dbservice = Databaseop()
    print(dbservice)
    emp = Employee(eid=102,enm= 'axxxxxTTTT', esal= 9963.3)
    # dbservice.fetch_single_data(101)
    # dbservice.fetch_all_data()
    # dbservice.insert_data(emp)
    # dbservice.update_data(emp)
    # dbservice.delete_data(101)
    dbservice.allinone(INSERT_QUERY)
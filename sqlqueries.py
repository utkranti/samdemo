
CREATE_TABLE = ''' CREATE TABLE empinfo(
	e_id integer,
	e_nm varchar(50),
	e_age integer,
	primary key (e_id)
    )
    '''

INSERT_QUERY = '''insert into empinfo values({},'{}',{})'''

FETCH_SINGLE_QUERY = '''SELECT * FROM empinfo where e_id = {}'''

FETCH_ALL_QUERY = '''SELECT * FROM empinfo'''

UPDATE_QUERY = '''update empinfo set  e_nm = '{}', e_age = {} where e_id = {}'''

DELETE_QUERY = '''delete from empinfo where e_id = {}'''
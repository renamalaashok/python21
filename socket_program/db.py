import psycopg2 as db
con = db.connect(host="localhost",user="tcloudost",password="root",database='db2')
cur = con.cursor()

def browse(*args):
	q="select * from persons"
	if args:
		pid = args[0]
		condition = " where id={0}".format(pid)
		q=q+condition
	cur.execute(q)
	return cur.fetchall()


if __name__ == "__main__":
	print browse()
	print browse(2)
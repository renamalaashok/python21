import logging
import progr1

logging.basicConfig(level=logging.WARN, 
	filename="log1.txt", 
	format="%(asctime)s-->%(levelname)s;%(message)s")
print progr1.fun()
logging.info("program started")
def div(a,b):
	res=""
	logging.info("function statred")
	try:
	    res = a/b
	except Exception as err:
		logging.exception(err)
	logging.info("Result of the function: {0}".format(res))
	logging.info("function ended")
	return res
logging.info("taking info from user")
a=raw_input("Enter a value:")
b= raw_input("Enter b value:")
if not a.isdigit() or not b.isdigit():
    logging.warn("app expecting digits but you have given somehtig else")
try:
	a=int(a)
	b=int(b)
except Exception as er:
	logging.exception (er)
div(a,b)


logging.info('program ended')
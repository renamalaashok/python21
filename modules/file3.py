
def fun():
	return "this is fun in file3"

if __name__ == "__main__":
	def main():
		print "program started"
		print "__name__:",__name__
		print fun()
		print "other statements in proggram"
		print "program ended"
	main()
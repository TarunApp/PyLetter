from PyDoc import makedocument
import fire
import string, os


class pyletter_cli(object):

	def createdoc(self, month, day):
		x = str(month)
		y = str(day)
		makedocument(x, y)
		# x = str(os.path)
		# print("Created Document for {} in {}".format( (str(month)+str(day)), str(x[23:(len(x)-2)]) ) )

fire.Fire(pyletter_cli)
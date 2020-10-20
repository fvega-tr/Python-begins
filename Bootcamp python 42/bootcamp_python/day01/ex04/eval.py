class Evaluator():

	@staticmethod
	def zip_evaluate(coefs, words):
		res = 0
		if type(words) is not list or type(coefs) is not list or (len(words) != len(coefs)):
			return -1
		for w, c in zip(words, coefs):
			res += len(w) * c
		return res

	@staticmethod
	def enumerate_evaluate(coefs, words):
		res = 0
		if type(words) is not list or type(coefs) is not list or (len(words) != len(coefs)):
			return -1
		for n, w in enumerate(words):
			res += len(w) * coefs[n]
		return res

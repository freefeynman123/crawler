import re
import unidecode
import numpy as np


class tidy_texts(object):

	@staticmethod
	def tidy_string(text, rm_separators=True):
		"""
		"""
		tidy_text = str(text)
		tidy_text = unidecode.unidecode(tidy_text)
		tidy_text = re.sub('[\s]+', ' ', tidy_text)
		if rm_separators:
			tidy_text = re.sub('([a-z])[\W]([a-z])', r'\g<1> \g<2>', tidy_text)
			tidy_text = re.sub('[^a-zA-Z\d\s:-]', '', tidy_text)
		return tidy_text.lower()

	@staticmethod
	def tidy_numeric(text):
		"""
		"""
		tidy_text = str(text)
		tidy_text = re.sub('[\s]+', '', tidy_text)
		tidy_text = re.sub(',', '.', tidy_text)
		try:
			tidy_text = re.search('([\d.]+)', tidy_text).group(1)
			tidy_text = float(tidy_text)
		except Exception as e:
			tidy_text = np.nan
			print(e.args)
		return tidy_text

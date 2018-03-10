def search4vowels(phrase: str) -> set:
	"""Return a set of vowels found in the phrase"""
	return set('aeiou').intersection(set(phrase))


def search4letters(phrase: str, letters: str='aeiou') -> set():
	"""Return the set of 'letters' found in the 'phrase'"""
	return set(letters).intersection(set(phrase))

def get_name(artist_name):
	"""This function takes the name of artist whose music we want to look for in itunes
	:param artist_name:
	:return: complete_url, name
	"""
	if isinstance(artist_name, str):
		name = '' + artist_name
		name = ''.join(name.split())
	else:
		return 'Enter a valid artist_name: '
	if name:
		base_url = 'https://itunes.apple.com/search?term={}&entity=musicVideo'
		artist = name.lower()
		complete_url = base_url.format(artist)
		return complete_url, name
	return 'artist name is a requirement'


print(get_name("Rihanna"))

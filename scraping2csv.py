from lxml import html
import requests
import csv
page = requests.get('https://www.imdb.com/title/tt7638344/fullcredits?ref_=tt_cl_sm#cast')
tree = html.fromstring(page.content)

download_dir = "starcast1.csv" #where you want the file to be downloaded to
csv = open(download_dir, "w")
columnTitleRow = "Actor, Chracter\n"
csv.write(columnTitleRow)




movie_name =  tree.xpath('//div[@class="titleBar"]/div[@class="title_wrapper"]/h1/text()[normalize-space()]')
if movie_name:
	movie_name = movie_name[0].strip()
else:
	#movie name cound not be found
	movie_name = ''

heading =  tree.xpath('//div[@id="fullcredits_content"]/h4[@class="dataHeaderWithBorder"]/text')
content =  tree.xpath('//div[@id="fullcredits_content"]/table[@class="simpleTable simpleCreditsTable"]/tr')

for data in heading[1:]:

	print(heading)

cast_rows = table = tree.xpath('//div[@id="fullcredits_content"]/table[@class="cast_list"]/tr')
print (movie_name.center(100, "*").upper())
print('-'*100)

for row in cast_rows[1:]:
	tds = row.xpath('./td')

	# 1st td is icon, 2nd is Actor, and 4rd is Character
	actor = row.xpath('./td[2]/a/text()')

	if actor:
		actor = actor[0].strip()
		actor = " ".join(actor.split())
	else:
		actor = ''

	character = row.xpath('./td[4]/a/text()')

	if character:
		character = character[0].strip()
		character = " ".join(character.split())

	else:
		character = row.xpath('./td[4]/text()')
		if character:
			character = character[0].strip()
			character = " ".join(character.split())
		else:
			character = ''

	row = actor + "," + character + "\n"
	csv.write(row)
	print('{actor: <40}{chracter: <10}'.format(actor=actor,chracter=character))

class india:
	def capital(self):
		print("new delhi is the capital of hte india")
	def language(self):
			print("hindi is most widely spoken language of india")
	def type(self):
			print("india is developing country")
class usa():
	def capital(self):
		print("washington DC is the capital of usa")
	def language(self):
		print("english is the primary language of india")
	def type(self):
		print("usa is developed country")
ind = india()
usa = usa()
for country in (ind,usa):
	country.capital()
	country.language()
	country.type()
	
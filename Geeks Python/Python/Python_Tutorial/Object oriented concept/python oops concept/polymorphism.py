class bird:
	def intro(self):
		print("there are many type of birds")
	def flight(self):
		print("most are fly and some are not")
class sparrow(bird):
	def flight(self):
		print("sparrow can fly")
class cock(bird):
	def flight(self):
		print("cock cannot fly")
obj_birds = bird()
obj_sparrow = sparrow()
obj_cock = cock()
obj_birds.intro()
obj_birds.flight()
obj_sparrow.intro()
obj_sparrow.flight()
obj_cock.intro()
obj_cock.flight()

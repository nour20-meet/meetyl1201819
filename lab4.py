class Aminal(object):
	def __init__(self,age,name,favfood,sound):
		self.name = name 
		self.favfood = favfood
		self.age=age
		self.sound=sound
	def eat(self,food):
		print (self.name + 'is eating' + food)
	def description (self):
		print(self.name + ' is '+ self.age + ' years old ' + 'and is eating ' + self.favfood)
	def make_sound(self):
		print(self.name + ':'+ self.sound *3)
s=Aminal('2','mona', 'chocolate', ' meaw')
s.description()
class Person(object):
	def __init__(self,name,age,city,gender):
		self.name = name 
		self.age = age 
		self.city = city
		self.gender = gender
	def eat_fav_breakfast(self,fav_breakfast):
		print(self.name +' is eating '+ fav_breakfast)
	def play_sport(self,fav_sport):
		print(self.name + ' is playing '+ fav_sport)
g=Person ('mona','18' ,'germany','female')
g.eat_fav_breakfast('pancake')
g.play_sport('football')
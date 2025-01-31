import unittest

animal_leg_counts= {
    'lion':4, 'monkey':2,'deer':4,'snake':0,'elephant':4,'frog':2,
    'horse':4,'spider':8,'ant':6,'dog':4,'cat':4,'parrot':2,'ostrich':2,
    'worm':0,'centipede':100
}
def count_four_leg_animal(animals):
    return sum(1 for animal in animals if animal_leg_counts.get(animal,0) ==4)

def count_two_leg_animal(animals):
    return sum(1 for animal in animals if animal_leg_counts.get(animal,0) ==2)


#Example 1
animals1 = ['lion','monkey','deer','snake','elephant'] 


#Example 2
animals2 = ['frog', 'horse', 'spider', 'ant']

print(count_four_leg_animal(animals1)) #output: 3

print(count_four_leg_animal(animals2)) #output: 1
      

class TestCountFourLeggedAnimal(unittest.TestCase):
    def test_normal(self):
        #all animal with 4 legs
        self.assertEqual(count_four_leg_animal(['lion', 'deer', 'elephant', 'horse', 'dog', 'cat']),6)
        #some animal with 4 legs
        self.assertEqual(count_four_leg_animal(['lion', 'deer','monkey', 'parrot', 'ostrich']),2)
        #No animal with 4 legs
        self.assertEqual(count_four_leg_animal(['spider', 'ant', 'centipede']),0)


    def test_edge(self):
        #No animal
        self.assertEqual(count_four_leg_animal([]),0)
        #Animal that doesn't exist in the list
        self.assertEqual(count_four_leg_animal(['pikachu','charzard']),0)
        #animal in list and not in list
        self.assertEqual(count_four_leg_animal(['lion','pikachu']),1)

if __name__ == "__main__":
    unittest.main()
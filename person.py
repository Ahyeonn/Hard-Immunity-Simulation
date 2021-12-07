import random
random.seed(42)
from virus import Virus


class Person(object):
    ''' Person objects will populate the simulation. '''

    def __init__(self, _id, is_vaccinated, infection=None):
        ''' We start out with is_alive = True, because we don't make vampires or zombies.
        All other values will be set by the simulation when it makes each Person object.

        If person is chosen to be infected when the population is created, the simulation
        should instantiate a Virus object and set it as the value
        self.infection. Otherwise, self.infection should be set to None.
        '''
        self._id = _id  # int
        self.is_alive = True  # boolean
        self.is_vaccinated = is_vaccinated  # boolean
        self.infection = infection # Virus object or None

    def did_survive_infection(self):
        ''' Generate a random number and compare to virus's mortality_rate.
        If random number is smaller, person dies from the disease.
        If Person survives, they become vaccinated and they have no infection.
        Return a boolean value indicating whether they survived the infection.
        '''
        # Only called if infection attribute is not None.
        # TODO:  Finish this method. Should return a Boolean
        print("Checking if person is alive")
        if random.uniform(0,1) < self.infection.mortality_rate:
            print("alive")
            self.is_alive = False
            return False

        else:
            print("dead")
            self.is_vaccinated = True
            self.infection = None
            return True

''' These are simple tests to ensure that you are instantiating your Person class correctly. '''
def test_vacc_person_instantiation():
    # create some people to test if our init method works as expected
    person = Person(1, True)
    assert person._id == 1
    assert person.is_alive is True
    assert person.infection is None


def test_not_vacc_person_instantiation():
    person = Person(2, False)
    # TODO: complete your own assert statements that test
    # the values at each attribute
    # assert ...
    assert person._id == 2
    assert person.is_alive is True
    assert person.infection is None


def test_sick_person_instantiation():
    # Create a Virus object to give a Person object an infection
    virus = Virus("Dysentery", 0.7, 0.2)
    # Create a Person object and give them the virus infection
    person = Person(3, False, virus)
    # TODO: complete your own assert statements that test
    # the values at each attribute
    # assert ...
    assert person._id == 3
    assert person.is_alive is True
    assert isinstance(person.infection, Virus)
    # or assert person.infection == virus
    


def test_did_survive_infection():
    # TODO: Create a Virus object to give a Person object an infection
    virus = Virus("Dysentery", 0.7, 0.5)
    # TODO: Create a Person object and give them the virus infection
    person = Person(4, False, virus)

    # Resolve whether the Person survives the infection or not
    survived = person.did_survive_infection()
    # Check if the Person survived or not
    if survived:
        assert person._id == 4
        assert person.is_alive is True
        assert person.is_vaccinated is True
        assert person.infection is None
        # TODO: Write your own assert statements that test
        # the values of each attribute for a Person who survived
        # assert ...
    else:
        assert person._id == 4
        assert person.is_alive is False
        assert person.is_vaccinated is False
        assert person.infection == virus
        # TODO: Write your own assert statements that test
        # the values of each attribute for a Person who did not survive
        # assert ...

if __name__ == "__main__":
    virus = Virus("Ebola", .8, .3)
#     ahyeon = Person(2, False, virus)
#     print(ahyeon.did_survive_infection())
#     test_vacc_person_instantiation()
#     test_not_vacc_person_instantiation()
#     test_sick_person_instantiation()
#     test_did_survive_infection()
#     people = []
#     for id in range(100):
#        person = Person(id, False, virus)
#        people.append(person)
#        person.did_survive_infection()
#     survivals = 0
#     casualty = 0 
#     for person in people:
#         if person.is_alive:
#             survivals += 1
#         else:
#             casualty += 1
#     print(f"There are {survivals} survivals & {casualty} casualty.")
    
# # Two diff tests

#     infected_people = []
#     for id in range(100):
#         person = Person(id, False)
#         if random.uniform(0,1) < virus.repro_rate:
#             person.infection = virus
#             infected_people.append(person)
    
#     print(f"Num of infected people: {len(infected_people)}")

#combined tests

    infected_people = []
    for id in range(100):
        person = Person(id, False)
        if random.uniform(0,1) < virus.repro_rate:
            person.infection = virus
            infected_people.append(person)
            person.did_survive_infection()
        survivals = 0 
        casualty = 0
        for person in infected_people:
            if person.is_alive:
                survivals += 1 
            else: 
                casualty += 1 
        
    print(f"There are {survivals} survivals & {casualty} casualty.")
    print(f"Num of infected people: {len(infected_people)}")

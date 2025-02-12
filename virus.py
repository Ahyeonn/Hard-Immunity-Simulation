class Virus(object):
    '''Properties and attributes of the virus used in Simulation.'''

    def __init__(self, name, repro_rate, mortality_rate):
        self.name = name
        self.repro_rate = repro_rate
        self.mortality_rate = mortality_rate

if __name__ == "__main__":
    def test_virus_instantiation():
        #TODO: Create your own test that models the virus you are working with
        '''Check to make sure that the virus instantiator is working.'''
        virus = Virus("HIV", 0.8, 0.3)
        print(virus.name, virus.repro_rate, virus.mortality_rate)
        assert virus.name == "HIV" # throw an error if its not equal
        assert virus.repro_rate == 0.8
        assert virus.mortality_rate == 0.3

    test_virus_instantiation()

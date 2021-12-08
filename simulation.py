import random, sys
random.seed(42)
from person import Person
from logger import Logger
from virus import Virus


class Simulation(object):
    def __init__(self, virus, pop_size, vacc_percentage, initial_infected=1):
        self.pop_size = int(pop_size) # Int
        self.next_person_id = 0 # Int
        self.virus = virus # Virus object
        self.initial_infected = int(initial_infected) # Int
        self.total_infected = 0 # Int
        self.current_infected = 0 # Int
        self.vacc_percentage = float(vacc_percentage) # float between 0 and 1
        self.total_dead = 0 # Int
        self.current_dead = 0
        self.total_vacc = 0
        self.current_vacc = 0
        self.population = [] #List of Person objects
        self.file_name = f"{virus.name}_simulation_pop_{pop_size}_vp_{vacc_percentage}_infected_{initial_infected}.txt"
        self.logger = Logger(self.file_name)
        self.newly_infected = []
        self.infected = []
        self.time_step_counter = 0
        self.current_interaction_counter = 0
        self.interaction_counter = 0

    def _create_population(self):
        # 3 types of people here: Vaccinated, Unvaccinated, Infected People  
        vaccinated = round(self.pop_size * self.vacc_percentage)

        #infected
        for id in range(self.initial_infected):
            self.population.append(Person(id, False, self.virus))

        #vaccinated
        for id in range(vaccinated):
            self.population.append(Person(id, True))

        #not-vaccinated
        for id in range(self.pop_size - (vaccinated+self.initial_infected)):
            self.population.append(Person(id, False))

        return self.population
        

    def _simulation_should_continue(self):
        #not vaccinated or person is alive 
        for person in self.population: # [a = vac , b = not vac, c = is alive]
            if person.infection:
                print('Continue the Simulation')
                return True
                 
        print('End the Simulation \n')

        return False 

    def run(self):
        self.logger.write_metadata(self) 
        should_continue = True
        self._create_population()

        #Done at very beginning of the simulation 
        for person in self.population:
            if person.infection:
                self.infected.append(person)

        while should_continue:
            self.time_step_counter += 1
            print(f'\n- The simulation turns {self.time_step_counter}')
            self.time_step()
            should_continue = self._simulation_should_continue()
            self.logger.log_display_steps(self)
            self.total_dead += self.current_dead
            self.current_dead = 0
            self.total_vacc += self.current_vacc
            self.current_vacc = 0
            self.total_infected += self.current_infected
            self.current_infected = 0
            self.interaction_counter += self.current_interaction_counter
        
        self.logger.log_total(self)


    def time_step(self):
        for person in self.infected:
            for _ in range(100): #100 interactions w 1 infected person in the population
                random_person = self.population[random.randrange(0, self.pop_size-1)] # pull out random person from the list of population
                self.interaction(person, random_person)
                self.current_interaction_counter += 1

        print(f"- Interaction counter {self.current_interaction_counter}\n")
        self._infect_newly_infected()
        self.infected = self.newly_infected
        self.newly_infected = []

    def interaction(self, person, random_person):
        assert person.is_alive == True
        assert random_person.is_alive == True
        if not random_person.is_vaccinated and random_person.infection is None:
            if random.uniform(0,1) < person.infection.repro_rate:
                random_person.infection = person.infection
                self.newly_infected.append(random_person)

    def _infect_newly_infected(self):
        for person in self.infected:
            self.current_infected += 1
            if not person.did_survive_infection():
                self.current_dead += 1
                self.population.remove(person)
                self.pop_size -= 1
                
            else:
                self.current_vacc += 1


if __name__ == "__main__":
    params = sys.argv[1:]
    virus_name, repro_num, mortality_rate = str(params[0]), float(params[1]), float(params[2])

    pop_size, vacc_percentage, initial_infected = int(params[3]), float(params[4]), float(params[5])

    virus = Virus(virus_name, repro_num, mortality_rate)

    sim = Simulation(virus, pop_size, vacc_percentage, initial_infected)

    sim.run()

# python3 simulation.py "Ebola" 0.5 0.5 80 0 1
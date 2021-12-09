class Logger(object):
    def __init__(self, file_name):
        self.file_name = file_name

    def write_metadata(self, sim):
        with open(self.file_name, "w") as outfile:
            outfile.write(f'''< Virus Stats >
    Virus Name: {sim.virus.name}
    Reproduction Rate: {sim.virus.repro_rate}
    Mortality Rate: {sim.virus.mortality_rate}

< Simulation Stats >
    Population Size: {sim.pop_size}
    Vaccinated % = {sim.vacc_percentage}
            ''')

    def log_display_steps(self, sim): #write_metadatata append
        with open(self.file_name, "a") as outfile:
            outfile.write(f'''
Step: {sim.time_step_counter}
    Interactions: {sim.current_interaction_counter} New Infections: {sim.current_infected} Death: {sim.current_dead} People  Vaccinated: {sim.current_vacc} People
            ''')

    def log_total(self, sim):
        with open(self.file_name, "a") as outfile:
            outfile.write(f'''
Total Population: {sim.total_dead + sim.pop_size} Total Death: {sim.total_dead} Total Vaccination: {sim.total_vacc}
            ''')


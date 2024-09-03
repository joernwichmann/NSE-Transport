"""Contains local parameter configuration."""
### Experimentname
NAME_EXPERIMENT: str = "TH_noBC_init_poly_noise_Chorin"

### Algorithm
ALGORITHM_NAME: str =  "Chorin splitting" #see src.algorithms.select.py for available choices

### Data
INITIAL_CONDITION_NAME: str = "polynomial - no BC"    #see 'src.predefined_data' for available choices
NOISE_COEFFICIENT_NAME: str = "polynomial"  #see 'src.predefined_data' for available choices

### Discretisation
VELOCITY_ELEMENT: str = "CG"    #see firedrake doc for available spaces
VELOCITY_DEGREE: int = 2       

PRESSURE_ELEMENT: str = "CG"    #see firedrake doc for available spaces
PRESSURE_DEGREE: int = 1

################               FILE/DIRECTORY NAMES               ############################
#Log
NAME_LOGFILE_GENERATE: str = f"{NAME_EXPERIMENT}.log"

#Vtk
VTK_DIRECTORY: str = f"vtk"

#Convergence
TIME_DIRECTORYNAME: str = f"convergence_results/{NAME_EXPERIMENT}"

#Stability
STABILITY_DIRECTORYNAME: str = f"stability_results/{NAME_EXPERIMENT}"

#Energy
ENERGY_DIRECTORYNAME: str = f"energy_results/{NAME_EXPERIMENT}"

#Statistics
STATISTICS_DIRECTORYNAME: str = f"statistic_results/{NAME_EXPERIMENT}"

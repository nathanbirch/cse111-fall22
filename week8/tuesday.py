
# element = {
#     "symbol": "Ac",
#     "name": "Actinium",
#     "mass": 227
# }
# element2 = {
#     "symbol": "Al",
#     "name": "Aluminum",
#     "mass": 26.9815386
# }

# elements = [element, element2]

# print(elements)

def make_periodic_table():
    return [
        {"symbol": "Ac", "name": "Actinium", "mass": 227},
        {"symbol": "Al", "name": "Aluminum", "mass": 26.9815386},
        {"symbol": "Sb", "name": "Antimony", "mass": 121.76},
        {"symbol": "Ar", "name": "Argon", "mass": 39.948},
        {"symbol": "As", "name": "Arsenic", "mass": 74.9216},
        {"symbol": "At", "name": "Astatine", "mass": 210},
        {"symbol": "Ba", "name": "Barium", "mass": 137.327},
        {"symbol": "Be", "name": "Beryllium", "mass": 9.012182},
        {"symbol": "Bi", "name": "Bismuth", "mass": 208.9804},
        {"symbol": "B", "name": "Boron", "mass": 10.811},
        {"symbol": "Br", "name": "Bromine", "mass": 79.904},
        {"symbol": "Cd", "name": "Cadmium", "mass": 112.411},
        {"symbol": "Ca", "name": "Calcium", "mass": 40.078},
        {"symbol": "C", "name": "Carbon", "mass": 12.0107},
        {"symbol": "Ce", "name": "Cerium", "mass": 140.116},
        {"symbol": "Cs", "name": "Cesium", "mass": 132.9054519},
        {"symbol": "Cl", "name": "Chlorine", "mass": 35.453},
        {"symbol": "Cr", "name": "Chromium", "mass": 51.9961},
        {"symbol": "Co", "name": "Cobalt", "mass": 58.933195},
        {"symbol": "Cu", "name": "Copper", "mass": 63.546},
        {"symbol": "Dy", "name": "Dysprosium", "mass": 162.5},
        {"symbol": "Er", "name": "Erbium", "mass": 167.259},
        {"symbol": "Eu", "name": "Europium", "mass": 151.964},
        {"symbol": "F", "name": "Fluorine", "mass": 18.9984032},
        {"symbol": "Fr", "name": "Francium", "mass": 223},
        {"symbol": "Gd", "name": "Gadolinium", "mass": 157.25},
        {"symbol": "Ga", "name": "Gallium", "mass": 69.723},
        {"symbol": "Ge", "name": "Germanium", "mass": 72.64},
        {"symbol": 'Au', "name": 'Gold', "mass": 196.966569},
        {"symbol": "Hf", "name": "Hafnium", "mass": 178.49},
        {"symbol": "He", "name": "Helium", "mass": 4.002602},
        {"symbol": "Ho", "name": "Holmium", "mass": 164.93032},
        {"symbol": "H", "name": "Hydrogen", "mass": 1.00794},
        {"symbol": "In", "name": "Indium", "mass": 114.818},
        {"symbol": "I", "name": "Iodine", "mass": 126.90447},
        {"symbol": "Ir", "name": "Iridium", "mass": 192.217},
        {"symbol": "Fe", "name": "Iron", "mass": 55.845},
        {"symbol": "Kr", "name": "Krypton", "mass": 83.798},
        {"symbol": "La", "name": "Lanthanum", "mass": 138.90547},
        {"symbol": "Pb", "name": "Lead", "mass": 207.2},
        {"symbol": "Li", "name": "Lithium", "mass": 6.941},
        {"symbol": "Lu", "name": "Lutetium", "mass": 174.9668},
        {"symbol": "Mg", "name": "Magnesium", "mass": 24.305},
        {"symbol": "Mn", "name": "Manganese", "mass": 54.938045},
        {"symbol": "Hg", "name": "Mercury", "mass": 200.59},
        {"symbol": "Mo", "name": "Molybdenum", "mass": 95.96},
        {"symbol": "Nd", "name": "Neodymium", "mass": 144.242},
        {"symbol": "Ne", "name": "Neon", "mass": 20.1797},
        {"symbol": "Np", "name": "Neptunium", "mass": 237},
        {"symbol": "Ni", "name": "Nickel", "mass": 58.6934},
        {"symbol": "Nb", "name": "Niobium", "mass": 92.90638},
        {"symbol": "N", "name": "Nitrogen", "mass": 14.0067},
        {"symbol": "Os", "name": "Osmium", "mass": 190.23},
        {"symbol": "O", "name": "Oxygen", "mass": 15.9994},
        {"symbol": "Pd", "name": "Palladium", "mass": 106.42},
        {"symbol": "P", "name": "Phosphorus", "mass": 30.973762},
        {"symbol": "Pt", "name": "Platinum", "mass": 195.084},
        {"symbol": "Pu", "name": "Plutonium", "mass": 244},
        {"symbol": "Po", "name": "Polonium", "mass": 209},
        {"symbol": "K", "name": "Potassium", "mass": 39.0983},
        {"symbol": "Pr", "name": "Praseodymium", "mass": 140.90765},
        {"symbol": "Pm", "name": "Promethium", "mass": 145},
        {"symbol": "Pa", "name": "Protactinium", "mass": 231.03588},
        {"symbol": "Ra", "name": "Radium", "mass": 226},
        {"symbol": "Rn", "name": "Radon", "mass": 222},
        {"symbol": "Re", "name": "Rhenium", "mass": 186.207},
        {"symbol": "Rh", "name": "Rhodium", "mass": 102.9055},
        {"symbol": "Rb", "name": "Rubidium", "mass": 85.4678},
        {"symbol": "Ru", "name": "Ruthenium", "mass": 101.07},
        {"symbol": "Sm", "name": "Samarium", "mass": 150.36},
        {"symbol": "Sc", "name": "Scandium", "mass": 44.955912},
        {"symbol": "Se", "name": "Selenium", "mass": 78.96},
        {"symbol": "Si", "name": "Silicon", "mass": 28.0855},
        {"symbol": 'Ag', "name": 'Silver', "mass": 107.8682},
        {"symbol": "Na", "name": "Sodium", "mass": 22.98976928},
        {"symbol": "Sr", "name": "Strontium", "mass": 87.62},
        {"symbol": "S", "name": "Sulfur", "mass": 32.065},
        {"symbol": "Ta", "name": "Tantalum", "mass": 180.94788},
        {"symbol": "Tc", "name": "Technetium", "mass": 98},
        {"symbol": "Te", "name": "Tellurium", "mass": 127.6},
        {"symbol": "Tb", "name": "Terbium", "mass": 158.92535},
        {"symbol": "Tl", "name": "Thallium", "mass": 204.3833},
        {"symbol": "Th", "name": "Thorium", "mass": 232.03806},
        {"symbol": "Tm", "name": "Thulium", "mass": 168.93421},
        {"symbol": "Sn", "name": "Tin", "mass": 118.71},
        {"symbol": "Ti", "name": "Titanium", "mass": 47.867},
        {"symbol": "W", "name": "Tungsten", "mass": 183.84},
        {"symbol": "U", "name": "Uranium", "mass": 238.02891},
        {"symbol": "V", "name": "Vanadium", "mass": 50.9415},
        {"symbol": "Xe", "name": "Xenon", "mass": 131.293},
        {"symbol": "Yb", "name": "Ytterbium", "mass": 173.054},
        {"symbol": "Y", "name": "Yttrium", "mass": 88.90585},
        {"symbol": "Zn", "name": "Zinc", "mass": 65.38},
        {"symbol": "Zr", "name": "Zirconium", "mass": 91.22}
    ]

elements = make_periodic_table()

total_mass = 0
for element in elements:
    total_mass += element['mass']

print(total_mass)
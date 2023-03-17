import math
import matlab
import matplotlib
e = 2.11e5 * 0.006895 # Original modulus was provided in KSI. Converted to Gigapascals.

full_length = 88 / 100  # Convert mm to m
beam_width = 7 / 1000  # Convert mm to m
beam_depth = 8 / 1000  # Convert mm to m


#Equations sourced from the bottom of the Methodology section.#
######################################################################################
moment_of_inertia = (beam_width*(beam_depth**3))/12 
simple_maximum_perm_deflection = (164*(full_length**3))/48*e*moment_of_inertia
cantilever_maximum_perm_deflection = (7*242*(full_length**3))/768*e*moment_of_inertia
fixed_maximum_perm_deflection = (250*(full_length**3))/192*e*moment_of_inertia
######################################################################################

displacements = [0,2,4,6,8,10,12,14,16,18,20,22,24,26] ## kind of useless, couldn't find a use for it.
cantilever_applied_loads = [] 
fixed_applied_loads = []
simple_applied_loads = []


def Simple_Bending_Moment(applied_loads,L):
    for load in applied_loads:
        M_max = (load * L) / 4
        print(f"Applied Load: {load} N, Maximum Bending Moment: {M_max} Nm")
        Hookes_Law(M_max)

def Cantilever_Bending_Moment(applied_loads,L):
    for load in applied_loads:
        M_max = (load * (L**2)) / 8
        print(f"Applied Load: {load} N, Maximum Bending Moment: {M_max} Nm")
        Hookes_Law(M_max)

def Fixed_Bending_Moment(applied_loads,L):
    for load in applied_loads:
        M_max = (load * (L**2)) / 16
        print(f"Applied Load: {load} N, Maximum Bending Moment: {M_max} Nm")
        Hookes_Law(M_max)

def Hookes_Law(bendingmoment,L):
    return (bendingmoment*(full_length/2))/e


def main():
    print(f"Moment of inertia: {moment_of_inertia} m^4")
    print(f"Simple maximum deflection: {simple_maximum_perm_deflection}m")
    print(f"Cantilever maximum deflection: {cantilever_maximum_perm_deflection}m")
    print(f"Fixed maximum deflection: {fixed_maximum_perm_deflection}m")
    print(f"Modulus (E): {e}",  "Gigapascals")

main()
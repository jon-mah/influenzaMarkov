"""
The purpose of this script is to label the sites of interest in HA
    PyLabel_H1
        Calculates relative solvent accessibility (RSA) for each residue in H1
        and outlines a preset list of residues as red spheres.

It is intended to be run in the PyMOL terminal as:
        run label_HA.py

NOTE: This file can only be run using the PyMOL interface, it will not run
correctly when called straight from the command line.

Note: The structural file was annotated by Hugh Haddox, from the Bloom Lab.

JCM 7_31_2018
"""
import pymol
from pymol import cmd, stored

import collections

def PyLabel_H1():

    # Input variables
    structure = '../../Data/1RVX_trimer_sequentialnumbering.pdb'

    # Clear pymol, and get structure
    cmd.delete('all')
    cmd.load(structure) # type = 'pdb1'
    cmd.remove('chain B')
    cmd.remove('chain C')
    cmd.hide('all')
    cmd.show('cartoon')
    cmd.color('white')
    # cmd.set('cartoon_transparency', '0.5')
    # cmd.color('grey20', structure)
    # cmd.set('cartoon_transparency', '0', structure)

    # read sites into file as list
    # join into list when separated by '+'

    # Turn on SASA flag
    cmd.set('dot_solvent', '1')
    # Set to high accuracy of measurement.
    cmd.set('dot_density', '2')

        # Create individual objects for each of the identified sites
        # Need list of sites
    individualSites = [150, 161, 206, 237, 323]
    # for each individual site, highlight them as a red sphere.
    for x in individualSites:
        objectName = 'chain A and resi ' + str(x)
        cmd.select(x, objectName)
        cmd.color('red', objectName)
        cmd.show('spheres', objectName)

    cmd.set_view ('\
             1.000000000,    0.000000000,    0.000000000,\
             0.006956612,   -0.346267730,    0.938110232,\
            -0.007149160,   -0.938125551,   -0.346219748,\
             0.000000000,    0.000000000, -404.992340088,\
            66.348487854,   14.958191872,   14.620470047,\
            18.658756256,  896.364440918,  -20.000000000 ')

    cmd.set('bg_rgb', '[1,1,1]') # white
    cmd.set('antialias', '2')
    cmd.set('ray_opaque_background', 'off')
    cmd.deselect()

    png_width = 1600
    png_height = 1200

    # Uncomment to generate a png
    cmd.ray(png_width, png_height)
    cmd.png('viewA_1RVX_monomer_positiveSelection.png')

    cmd.set_view ('\
             0.590784729,   -0.273755223,   -0.758965433,\
             0.749687612,   -0.176127166,    0.637927651,\
            -0.082892060,   -0.982710958,   -0.165563077,\
             0.000000000,    0.000000000, -404.992340088,\
            66.348487854,   14.958191872,   14.620470047,\
            18.658756256,  896.364440918,  -20.000000000 ')

    # Uncomment to generate a png
    cmd.ray(png_width, png_height)
    cmd.png('viewB_1RVX_monomer_positiveSelection.png')

cmd.extend("PyLabel_H1", PyLabel_H1)

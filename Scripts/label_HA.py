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

def labelSub_0():

    # Input variables
    structure = '../Data/1rvx_trimer_sequentialnumbering.pdb'

    # Clear pymol, and get structure
    cmd.delete('all')
    cmd.load(structure) # type = 'pdb1'
    cmd.remove('chain B')
    cmd.remove('chain C')
    cmd.hide('all')
    cmd.show('cartoon')
    cmd.show('ribbon')
    cmd.color('white')
    cmd.set ("sphere_scale", 0.75)
    cmd.set('cartoon_transparency', 0.5)
    cmd.set('sphere_transparency', 0.5)
    cmd.set('label_size', 20)
    # cmd.color('grey20', structure)
    # cmd.set('cartoon_transparency', '0', structure)


    varDict = {} # maps from variability clas to a list of sites
    inputFile = '../Data/Subsample_0_PROT_variability.csv' # Reads off of variability.csv
    with open(inputFile, 'r') as f:
        for line in f:
            # Read csv, separate site and variation class information
            if 'Site' not in line:
                siteIndex, varClass = line.split(',')
                varClass = varClass[:-2]
                siteIndex = int(siteIndex)
                varClass = float(varClass)
                # Create a dictionary from variation class to a list of sites
                if varClass in varDict.keys():
                    varDict[varClass].append(siteIndex)
                else:
                    varDict[varClass] = [siteIndex]

    # The number of variation classes for this subsample.
    numClass = float(len(varDict.keys()))

    colorIndex = 0.0 # Used to iterate
    # Sorted in ascending order
    for key in sorted(varDict.iterkeys()):
        # Develop a color gradient named after variation class
        cmd.set_color(str(key), [0.00 + colorIndex / numClass, 0.00, 1.00 - colorIndex / numClass])
        colorIndex = colorIndex + 1

    # Color all the sites according to its variation class
    for key in sorted(varDict.iterkeys()):
        siteList_string = ''
        for x in varDict[key]:
            objectName = 'chain A and resi ' + str(x)
            cmd.select(x, objectName)
            cmd.color(str(key), objectName)
            cmd.deselect()

    # Capture image
    cmd.set_view ('\
          0.761710763,   -0.066203296,   -0.644522429,\
          0.641907752,   -0.058046252,    0.764584303,\
         -0.088030294,   -0.996115863,   -0.001718835,\
         -0.000290386,    0.000054881, -404.986755371,\
         76.299804688,    0.619804382,   19.037372589,\
        319.299041748,  490.685638428,  -20.000000000' )

    cmd.set('bg_rgb', '[1,1,1]') # white background
    cmd.set('antialias', '2') # Image option for clarity
    cmd.set('ray_opaque_background', 'off') # Image option for clarity
    cmd.deselect() # Do not cross object selection

    png_width = 1600
    png_height = 1200

    # Uncomment to generate a png
    cmd.ray(png_width, png_height)
    cmd.png('../Data/subsample_0_viewA.png')

    cmd.set_view ('\
          0.409883797,    0.010445972,    0.912075520,\
         -0.906124771,   -0.109993845,    0.408466846,\
          0.104589798,   -0.993877053,   -0.035619322,\
         -0.000290386,    0.000054881, -404.986755371,\
         76.299804688,    0.619804382,   19.037372589,\
        319.299041748,  490.685638428,  -20.000000000' )

    # Uncomment to generate a png
    cmd.ray(png_width, png_height)
    cmd.png('../Data/subsample_0_viewB.png')

def labelSub_1():

    # Input variables
    structure = '../Data/1rvx_trimer_sequentialnumbering.pdb'

    # Clear pymol, and get structure
    cmd.delete('all')
    cmd.load(structure) # type = 'pdb1'
    cmd.remove('chain B')
    cmd.remove('chain C')
    cmd.hide('all')
    cmd.show('cartoon')
    cmd.show('ribbon')
    cmd.color('white')
    cmd.set ("sphere_scale", 0.75)
    cmd.set('cartoon_transparency', 0.5)
    cmd.set('sphere_transparency', 0.5)
    cmd.set('label_size', 20)
    # cmd.color('grey20', structure)
    # cmd.set('cartoon_transparency', '0', structure)


    varDict = {} # maps from variability clas to a list of sites
    inputFile = '../Data/Subsample_0_PROT_variability.csv' # Reads off of variability.csv
    with open(inputFile, 'r') as f:
        for line in f:
            # Read csv, separate site and variation class information
            if 'Site' not in line:
                siteIndex, varClass = line.split(',')
                varClass = varClass[:-2]
                siteIndex = int(siteIndex)
                varClass = float(varClass)
                # Create a dictionary from variation class to a list of sites
                if varClass in varDict.keys():
                    varDict[varClass].append(siteIndex)
                else:
                    varDict[varClass] = [siteIndex]

    # The number of variation classes for this subsample.
    numClass = float(len(varDict.keys()))

    colorIndex = 0.0 # Used to iterate
    # Sorted in ascending order
    for key in sorted(varDict.iterkeys()):
        # Develop a color gradient named after variation class
        cmd.set_color(str(key), [0.00 + colorIndex / numClass, 0.00, 1.00 - colorIndex / numClass])
        colorIndex = colorIndex + 1

    # Color all the sites according to its variation class
    for key in sorted(varDict.iterkeys()):
        siteList_string = ''
        for x in varDict[key]:
            objectName = 'chain A and resi ' + str(x)
            cmd.select(x, objectName)
            cmd.color(str(key), objectName)
            cmd.deselect()

    # Capture image
    cmd.set_view ('\
          0.761710763,   -0.066203296,   -0.644522429,\
          0.641907752,   -0.058046252,    0.764584303,\
         -0.088030294,   -0.996115863,   -0.001718835,\
         -0.000290386,    0.000054881, -404.986755371,\
         76.299804688,    0.619804382,   19.037372589,\
        319.299041748,  490.685638428,  -20.000000000' )

    cmd.set('bg_rgb', '[1,1,1]') # white background
    cmd.set('antialias', '2') # Image option for clarity
    cmd.set('ray_opaque_background', 'off') # Image option for clarity
    cmd.deselect() # Do not cross object selection

    png_width = 1600
    png_height = 1200

    # Uncomment to generate a png
    cmd.ray(png_width, png_height)
    cmd.png('../Data/subsample_1_viewA.png')

    cmd.set_view ('\
          0.409883797,    0.010445972,    0.912075520,\
         -0.906124771,   -0.109993845,    0.408466846,\
          0.104589798,   -0.993877053,   -0.035619322,\
         -0.000290386,    0.000054881, -404.986755371,\
         76.299804688,    0.619804382,   19.037372589,\
        319.299041748,  490.685638428,  -20.000000000' )

    # Uncomment to generate a png
    cmd.ray(png_width, png_height)
    cmd.png('../Data/subsample_1_viewB.png')

def labelSub_2():

    # Input variables
    structure = '../Data/1rvx_trimer_sequentialnumbering.pdb'

    # Clear pymol, and get structure
    cmd.delete('all')
    cmd.load(structure) # type = 'pdb1'
    cmd.remove('chain B')
    cmd.remove('chain C')
    cmd.hide('all')
    cmd.show('cartoon')
    cmd.show('ribbon')
    cmd.color('white')
    cmd.set ("sphere_scale", 0.75)
    cmd.set('cartoon_transparency', 0.5)
    cmd.set('sphere_transparency', 0.5)
    cmd.set('label_size', 20)
    # cmd.color('grey20', structure)
    # cmd.set('cartoon_transparency', '0', structure)

    varDict = {} # maps from variability clas to a list of sites
    inputFile = '../Data/Subsample_0_PROT_variability.csv' # Reads off of variability.csv
    with open(inputFile, 'r') as f:
        for line in f:
            # Read csv, separate site and variation class information
            if 'Site' not in line:
                siteIndex, varClass = line.split(',')
                varClass = varClass[:-2]
                siteIndex = int(siteIndex)
                varClass = float(varClass)
                # Create a dictionary from variation class to a list of sites
                if varClass in varDict.keys():
                    varDict[varClass].append(siteIndex)
                else:
                    varDict[varClass] = [siteIndex]

    # The number of variation classes for this subsample.
    numClass = float(len(varDict.keys()))

    colorIndex = 0.0 # Used to iterate
    # Sorted in ascending order
    for key in sorted(varDict.iterkeys()):
        # Develop a color gradient named after variation class
        cmd.set_color(str(key), [0.00 + colorIndex / numClass, 0.00, 1.00 - colorIndex / numClass])
        colorIndex = colorIndex + 1

    # Color all the sites according to its variation class
    for key in sorted(varDict.iterkeys()):
        siteList_string = ''
        for x in varDict[key]:
            objectName = 'chain A and resi ' + str(x)
            cmd.select(x, objectName)
            cmd.color(str(key), objectName)
            cmd.deselect()

    # Capture image
    cmd.set_view ('\
          0.761710763,   -0.066203296,   -0.644522429,\
          0.641907752,   -0.058046252,    0.764584303,\
         -0.088030294,   -0.996115863,   -0.001718835,\
         -0.000290386,    0.000054881, -404.986755371,\
         76.299804688,    0.619804382,   19.037372589,\
        319.299041748,  490.685638428,  -20.000000000' )

    cmd.set('bg_rgb', '[1,1,1]') # white background
    cmd.set('antialias', '2') # Image option for clarity
    cmd.set('ray_opaque_background', 'off') # Image option for clarity
    cmd.deselect() # Do not cross object selection

    png_width = 1600
    png_height = 1200

    # Uncomment to generate a png
    cmd.ray(png_width, png_height)
    cmd.png('../Data/subsample_2_viewA.png')

    cmd.set_view ('\
          0.409883797,    0.010445972,    0.912075520,\
         -0.906124771,   -0.109993845,    0.408466846,\
          0.104589798,   -0.993877053,   -0.035619322,\
         -0.000290386,    0.000054881, -404.986755371,\
         76.299804688,    0.619804382,   19.037372589,\
        319.299041748,  490.685638428,  -20.000000000' )

    # Uncomment to generate a png
    cmd.ray(png_width, png_height)
    cmd.png('../Data/subsample_2_viewB.png')

def labelSub_3():

    # Input variables
    structure = '../Data/1rvx_trimer_sequentialnumbering.pdb'

    # Clear pymol, and get structure
    cmd.delete('all')
    cmd.load(structure) # type = 'pdb1'
    cmd.remove('chain B')
    cmd.remove('chain C')
    cmd.hide('all')
    cmd.show('cartoon')
    cmd.show('ribbon')
    cmd.color('white')
    cmd.set ("sphere_scale", 0.75)
    cmd.set('cartoon_transparency', 0.5)
    cmd.set('sphere_transparency', 0.5)
    cmd.set('label_size', 20)
    # cmd.color('grey20', structure)
    # cmd.set('cartoon_transparency', '0', structure)

    varDict = {} # maps from variability clas to a list of sites
    inputFile = '../Data/Subsample_0_PROT_variability.csv' # Reads off of variability.csv
    with open(inputFile, 'r') as f:
        for line in f:
            # Read csv, separate site and variation class information
            if 'Site' not in line:
                siteIndex, varClass = line.split(',')
                varClass = varClass[:-2]
                siteIndex = int(siteIndex)
                varClass = float(varClass)
                # Create a dictionary from variation class to a list of sites
                if varClass in varDict.keys():
                    varDict[varClass].append(siteIndex)
                else:
                    varDict[varClass] = [siteIndex]

    # The number of variation classes for this subsample.
    numClass = float(len(varDict.keys()))

    colorIndex = 0.0 # Used to iterate
    # Sorted in ascending order
    for key in sorted(varDict.iterkeys()):
        # Develop a color gradient named after variation class
        cmd.set_color(str(key), [0.00 + colorIndex / numClass, 0.00, 1.00 - colorIndex / numClass])
        colorIndex = colorIndex + 1

    # Color all the sites according to its variation class
    for key in sorted(varDict.iterkeys()):
        siteList_string = ''
        for x in varDict[key]:
            objectName = 'chain A and resi ' + str(x)
            cmd.select(x, objectName)
            cmd.color(str(key), objectName)
            cmd.deselect()

    # Capture image
    cmd.set_view ('\
          0.761710763,   -0.066203296,   -0.644522429,\
          0.641907752,   -0.058046252,    0.764584303,\
         -0.088030294,   -0.996115863,   -0.001718835,\
         -0.000290386,    0.000054881, -404.986755371,\
         76.299804688,    0.619804382,   19.037372589,\
        319.299041748,  490.685638428,  -20.000000000' )

    cmd.set('bg_rgb', '[1,1,1]') # white background
    cmd.set('antialias', '2') # Image option for clarity
    cmd.set('ray_opaque_background', 'off') # Image option for clarity
    cmd.deselect() # Do not cross object selection

    png_width = 1600
    png_height = 1200

    # Uncomment to generate a png
    cmd.ray(png_width, png_height)
    cmd.png('../Data/subsample_3_viewA.png')

    cmd.set_view ('\
          0.409883797,    0.010445972,    0.912075520,\
         -0.906124771,   -0.109993845,    0.408466846,\
          0.104589798,   -0.993877053,   -0.035619322,\
         -0.000290386,    0.000054881, -404.986755371,\
         76.299804688,    0.619804382,   19.037372589,\
        319.299041748,  490.685638428,  -20.000000000' )

    # Uncomment to generate a png
    cmd.ray(png_width, png_height)
    cmd.png('../Data/subsample_3_viewB.png')

def labelSub_4():

    # Input variables
    structure = '../Data/1rvx_trimer_sequentialnumbering.pdb'

    # Clear pymol, and get structure
    cmd.delete('all')
    cmd.load(structure) # type = 'pdb1'
    cmd.remove('chain B')
    cmd.remove('chain C')
    cmd.hide('all')
    cmd.show('cartoon')
    cmd.show('ribbon')
    cmd.color('white')
    cmd.set ("sphere_scale", 0.75)
    cmd.set('cartoon_transparency', 0.5)
    cmd.set('sphere_transparency', 0.5)
    cmd.set('label_size', 20)
    # cmd.color('grey20', structure)
    # cmd.set('cartoon_transparency', '0', structure)


    varDict = {} # maps from variability clas to a list of sites
    inputFile = '../Data/Subsample_0_PROT_variability.csv' # Reads off of variability.csv
    with open(inputFile, 'r') as f:
        for line in f:
            # Read csv, separate site and variation class information
            if 'Site' not in line:
                siteIndex, varClass = line.split(',')
                varClass = varClass[:-2]
                siteIndex = int(siteIndex)
                varClass = float(varClass)
                # Create a dictionary from variation class to a list of sites
                if varClass in varDict.keys():
                    varDict[varClass].append(siteIndex)
                else:
                    varDict[varClass] = [siteIndex]

    # The number of variation classes for this subsample.
    numClass = float(len(varDict.keys()))

    colorIndex = 0.0 # Used to iterate
    # Sorted in ascending order
    for key in sorted(varDict.iterkeys()):
        # Develop a color gradient named after variation class
        cmd.set_color(str(key), [0.00 + colorIndex / numClass, 0.00, 1.00 - colorIndex / numClass])
        colorIndex = colorIndex + 1

    # Color all the sites according to its variation class
    for key in sorted(varDict.iterkeys()):
        siteList_string = ''
        for x in varDict[key]:
            objectName = 'chain A and resi ' + str(x)
            cmd.select(x, objectName)
            cmd.color(str(key), objectName)
            cmd.deselect()

    # Capture image
    cmd.set_view ('\
          0.761710763,   -0.066203296,   -0.644522429,\
          0.641907752,   -0.058046252,    0.764584303,\
         -0.088030294,   -0.996115863,   -0.001718835,\
         -0.000290386,    0.000054881, -404.986755371,\
         76.299804688,    0.619804382,   19.037372589,\
        319.299041748,  490.685638428,  -20.000000000' )

    cmd.set('bg_rgb', '[1,1,1]') # white background
    cmd.set('antialias', '2') # Image option for clarity
    cmd.set('ray_opaque_background', 'off') # Image option for clarity
    cmd.deselect() # Do not cross object selection

    png_width = 1600
    png_height = 1200

    # Uncomment to generate a png
    cmd.ray(png_width, png_height)
    cmd.png('../Data/subsample_4_viewA.png')

    cmd.set_view ('\
          0.409883797,    0.010445972,    0.912075520,\
         -0.906124771,   -0.109993845,    0.408466846,\
          0.104589798,   -0.993877053,   -0.035619322,\
         -0.000290386,    0.000054881, -404.986755371,\
         76.299804688,    0.619804382,   19.037372589,\
        319.299041748,  490.685638428,  -20.000000000' )

    # Uncomment to generate a png
    cmd.ray(png_width, png_height)
    cmd.png('../Data/subsample_4_viewB.png')

cmd.extend("labelSub_0", labelSub_0)
cmd.extend("labelSub_1", labelSub_1)
cmd.extend("labelSub_2", labelSub_2)
cmd.extend("labelSub_3", labelSub_3)
cmd.extend("labelSub_4", labelSub_4)

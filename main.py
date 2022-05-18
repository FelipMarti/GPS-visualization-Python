from gps_class import GPSVis

import sys, getopt, os


def main(argv):
    inputfile = ''
    outputfile = ''
    inputfolder = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:f:",["ifile=","ofile=","ifolder="])
    except getopt.GetoptError:
        print ('test.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('test.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        elif opt in ("-f", "--ifolder"):
            inputfolder = arg
    if not inputfile and not inputfolder:
        print ('test.py -i <inputfile> -o <outputfile>')
        print ('or')
        print ('test.py -f <inputfolder> -o <outputfile>')
        sys.exit(2)

    if inputfile:
        print('Input file is ' + inputfile)
    elif inputfolder:
        print('Input folder is ' + inputfolder)

    if not outputfile and inputfile:
        outputfile=os.path.splitext(inputfile)[0]
        outputfile=outputfile + '.eps'
    elif not outputfile and inputfolder:
        outputfile=os.path.abspath(inputfolder) + '.eps'
    print('Output file is ' + outputfile)

    vis = GPSVis(data_path='',
            map_path='map.png',  # Path to map downloaded from the OSM.
            points=(-37.68, 144.75, -37.825, 144.86)) # Two coordinates of the map (upper left, lower right)

    if inputfile:
        vis.create_image(data_path=inputfile, color=(0, 0, 255), width=3)  # Set the color and the width of the GNSS tracks.

    elif inputfolder:
        colours = ['blue', 'green', 'red', 'teal', 'orange', 'magenta', 'yellow', 'purple', 'coral', 'cornflowerblue', 'limegreen', 'darkorchid', 'gold', 'steelblue', 'yellowgreen', 'chocolate']
        rotate_colour = 0

        for filename in os.listdir(inputfolder):
            inputfile = inputfolder + '/' + filename
            print (inputfile)
    
            vis.create_image(data_path=inputfile, color=(colours[rotate_colour]), width=3)  # Set the color and the width of the GNSS tracks.
            rotate_colour += 1

    vis.plot_map(output='show', save_as=outputfile)

    print()



if __name__ == "__main__":
    main(sys.argv[1:])


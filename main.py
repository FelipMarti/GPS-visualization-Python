from gps_class import GPSVis

import sys, getopt, os


def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
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
    if not inputfile:
        print ('test.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    print('Input file is ' + inputfile)
    if not outputfile:
        outputfile=os.path.splitext(inputfile)[0]
        outputfile=outputfile + '.png'
    print('Output file is ' + outputfile)


    vis = GPSVis(data_path=inputfile,
             map_path='map.png',  # Path to map downloaded from the OSM.
             points=(-37.71, 144.77, -37.83, 144.86)) # Two coordinates of the map (upper left, lower right)

    vis.create_image(color=(0, 0, 255), width=3)  # Set the color and the width of the GNSS tracks.
    vis.plot_map(output='save', save_as=outputfile)

    print()



if __name__ == "__main__":
    main(sys.argv[1:])


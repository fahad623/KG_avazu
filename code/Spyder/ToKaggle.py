import csv


location_input_file = "../../data/avazu.preds.txt"
location_output_file = "../../data/kaggle.submission.csv"

def to_kaggle(header=""):
    print "\nReading:",location_input_file,"\nWriting:",location_output_file
    with open(location_input_file) as infile, open(location_output_file, "wb") as outfile:
        if len(header) > 0:
            outfile.write( header + "\n" )
        reader = csv.reader(infile, delimiter=" ")
        for row in reader:
            outfile.write( row[1] + "," + row[0] + "\n" )

to_kaggle("id,click")


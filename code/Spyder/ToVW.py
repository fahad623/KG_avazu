import csv

location_train = "../../data/train.csv"
location_test = "../../data/test.csv"

location_train_vw = "../../data/avazu.train.vw" #will be created
location_test_vw = "../../data/avazu.test.vw" #will be created

#creates Vowpal Wabbit-formatted file from tsv file
def to_vw(location_input_file, location_output_file, test = False):
    print "\nReading:",location_input_file,"\nWriting:",location_output_file
    with open(location_input_file) as infile, open(location_output_file, "wb") as outfile:

        reader = csv.DictReader(infile)
        for row in reader:
            #if test set label doesnt matter/or isnt available
            if test:
                label = "1"
            else:
                try:
                    label = 1 if int(row['click']) == 1 else -1 
                except:
                    continue

            outfile.write(
              str(label) + 
              " '" + row['id'] + 
              " |C" + " C1:" + row['C1'] + " C14:" + row['C14'] + " C15:" + row['C15'] + " C16:" + row['C16'] + " C17:" + row['C17'] + 
                      " C18:" + row['C18'] + " C19:" + row['C19'] + " C20:" + row['C20'] + " C21:" + row['C21'] +
              " |O1" + " hour:" + row['hour'] + " banner_pos:" + row['banner_pos'] + 
              " |O2" + " " + row['site_id'] + " " + row['site_domain'] + 
                       " " + row['site_category'] + " " + row['app_id'] + " " + row['app_domain'] + " " + row['app_category'] + 
                       " " + row['device_id'] + " " + row['device_ip'] + " " + row['device_model'] + 
              " |O2" +  " device_type:" + row['device_type'] +" device_conn_type:" + row['device_conn_type'] + 
              "\n" )

to_vw(location_train, location_train_vw)
to_vw(location_test, location_test_vw, test=True)
import csv

location_train = "..\\..\\data\\train.csv"
location_test = "..\\..\\data\\test.csv"

location_train_vw = "..\\..\\data\\avazu.train.vw" #will be created
location_test_vw = "..\\..\\data\\avazu.test.vw" #will be created

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
                    label = str(int(row['click']))
                except:
                    continue

            outfile.write(
              label + 
              " '" + row['id'] + 
              " |C" + " C1:" + row['C1'] + " C17:" + row['C17'] + " C18:" + row['C18'] + " C19:" + row['C19'] + " C20:" + row['C20']  + " C21:" + row['C21'] +
              " |O " + " hour:" + row['hour'] + " banner_pos:" + row['banner_pos'] + " site_id:" + row['site_id'] + " site_domain:" + row['site_domain'] + 
                       " site_category:" + row['site_category'] + " app_id:" + row['app_id'] + " app_domain:" + row['app_domain'] + " app_category:" + row['app_category'] + 
                       " device_id:" + row['device_id'] + " device_ip:" + row['device_ip'] + " device_model:" + row['device_model'] + " device_type:" + row['device_type'] + 
                       " device_conn_type:" + row['device_conn_type'] + 
              "\n" )

to_vw(location_train, location_train_vw)
to_vw(location_test, location_test_vw, test=True)
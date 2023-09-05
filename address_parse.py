# address_parse.py
# Sergio Morales in collaboration with Gavin McGuire
# Contact: scmoral3s@gmail.com 
# Piru Group 2023

# scrapes the map website in order to get all addresses
# run from command line using python3 address_parse.py

# use json to load in data, csv to create csv, and requests to scrape
import json
import requests
import csv


# all the scraping and parsing is done by this function
def load_and_parse_data(url):

    # get the raw data from the API 
    response = requests.get(url)
    data = json.loads(response.text)
    operational_layers = data.get('operationalLayers', [])

    # get each dictionary object
    operational_layers_0 = operational_layers[0]
    operational_layers_1 = operational_layers[1]
    operational_layers_2 = operational_layers[2]
    operational_layers_3 = operational_layers[3]
    operational_layers_4 = operational_layers[4]
    operational_layers_5 = operational_layers[5]
    operational_layers_6 = operational_layers[6]
    operational_layers_8 = operational_layers[8]
    
    # Extracting first set of addresses
    feature_col_0 = operational_layers_0.get('featureCollection')
    layers_0 = feature_col_0.get('layers', [])
    layer_def_0 = layers_0[0]
    feature_set_0 = layer_def_0.get('featureSet')
    features_0 = feature_set_0.get('features', [])


     # Extracting second set of addresses
    feature_col_1 = operational_layers_1.get('featureCollection')
    layers_1 = feature_col_1.get('layers', [])
    layer_def_1 = layers_1[0]
    feature_set_1 = layer_def_1.get('featureSet')
    features_1 = feature_set_1.get('features', [])

    # Extracting third set of addresses
    feature_col_2 = operational_layers_2.get('featureCollection')
    layers_2 = feature_col_2.get('layers', [])
    layer_def_2 = layers_2[0]
    feature_set_2 = layer_def_2.get('featureSet')
    features_2 = feature_set_2.get('features', [])

    # Extracting fourth set of addresses
    feature_col_3 = operational_layers_3.get('featureCollection')
    layers_3 = feature_col_3.get('layers', [])
    layer_def_3 = layers_3[0]
    feature_set_3 = layer_def_3.get('featureSet')
    features_3 = feature_set_3.get('features', [])

    # Extracting fifth set of addresses
    feature_col_4 = operational_layers_4.get('featureCollection')
    layers_4 = feature_col_4.get('layers', [])
    layer_def_4 = layers_4[0]
    feature_set_4 = layer_def_4.get('featureSet')
    features_4 = feature_set_4.get('features', [])

    # Extracting sixth set of addresses
    feature_col_5 = operational_layers_5.get('featureCollection')
    layers_5 = feature_col_5.get('layers', [])
    layer_def_5 = layers_3[0]
    feature_set_5 = layer_def_5.get('featureSet')
    features_5 = feature_set_5.get('features', [])

    # Extracting seventh set of addresses
    feature_col_6 = operational_layers_6.get('featureCollection')
    layers_6 = feature_col_6.get('layers', [])
    layer_def_6 = layers_6[0]
    feature_set_6 = layer_def_6.get('featureSet')
    features_6 = feature_set_6.get('features', [])

    # eigth object contains no addresses

    # Extracting ninth and final set of addresses
    feature_col_8 = operational_layers_8.get('featureCollection')
    layers_8 = feature_col_8.get('layers', [])
    layer_def_8 = layers_8[0]
    feature_set_8 = layer_def_8.get('featureSet')
    features_8 = feature_set_8.get('features', [])

    # open the csv, write each dictionary object in each loop
    # close csv at the end
    with open('addresses.csv', 'w', newline='') as file:
        writer = csv.writer(file)

        # first set 0{}
        for house in features_0:
            attributes = house.get('attributes')
            address = attributes.get("Street_Address")
            city = attributes.get("City")
            state = attributes.get("State")
            zip_code = attributes.get("Zip")
            lien_total = attributes.get("Lien_Total")
            fid = attributes.get("FID")
 
            writer.writerow([address,city,state,zip_code,lien_total,fid])

        # second set 1{}
        for house in features_1:
            attributes = house.get('attributes')
            address = attributes.get("Street_Address")
            city = attributes.get("City")
            state = attributes.get("State")
            zip_code = attributes.get("Zip")
            lien_total = attributes.get("Lien_Total")
            fid = attributes.get("FID")

            writer.writerow([address,city,state,zip_code,lien_total,fid])

        # third set 2{}
        for house in features_2:
            attributes = house.get('attributes')
            address = attributes.get("Street_Address")
            city = attributes.get("City")
            state = attributes.get("State")
            zip_code = attributes.get("Zip")
            lien_total = attributes.get("Lien_Total")
            fid = attributes.get("FID")

            writer.writerow([address,city,state,zip_code,lien_total,fid])
        
        # fourth set 3{}
        for house in features_3:
            attributes = house.get('attributes')
            address = attributes.get("Street_Address")
            city = attributes.get("City")
            state = attributes.get("State")
            zip_code = attributes.get("Zip")
            lien_total = attributes.get("Lien_Total")
            fid = attributes.get("FID")

            writer.writerow([address,city,state,zip_code,lien_total,fid])

        # fifth set 4{}
        for house in features_4:
            attributes = house.get('attributes')
            address = attributes.get("Street_Address")
            city = attributes.get("City")
            state = attributes.get("State")
            zip_code = attributes.get("Zip")
            lien_total = attributes.get("Lien_Total")
            fid = attributes.get("FID")

            writer.writerow([address,city,state,zip_code,lien_total,fid])

        # sixth set 5{}
        for house in features_5:
            attributes = house.get('attributes')
            address = attributes.get("Street_Address")
            city = attributes.get("City")
            state = attributes.get("State")
            zip_code = attributes.get("Zip")
            lien_total = attributes.get("Lien_Total")
            fid = attributes.get("FID")

            writer.writerow([address,city,state,zip_code,lien_total,fid])

        # seventh set 6{}
        for house in features_6:
            attributes = house.get('attributes')
            address = attributes.get("Street_Address")
            city = attributes.get("City")
            state = attributes.get("State")
            zip_code = attributes.get("Zip")
            lien_total = attributes.get("Lien_Total")
            fid = attributes.get("FID")

            writer.writerow([address,city,state,zip_code,lien_total,fid])

        # ninth and final set 8{}
        for house in features_8:
            attributes = house.get('attributes')
            address = attributes.get("Street_Address")
            city = attributes.get("City")
            state = attributes.get("State")
            zip_code = attributes.get("Zip")
            lien_total = attributes.get("Lien_Total")
            fid = attributes.get("FID")

            writer.writerow([address,city,state,zip_code,lien_total,fid])

# main driver url has been hard coded.
# should url change, update will be needed
# run every couple months to recieve updated information
def main():
    url = "https://www.arcgis.com/sharing/rest/content/items/ebc9cd0f9f1c483c832562e4879e43c3/data?f=json"
    load_and_parse_data(url)

if __name__ == "__main__":
    main()

"""Functions to help Azara and Rui locate pirate treasure."""

def get_coordinate(record):
    coord = record[1]
    return coord

def convert_coordinate(coordinate):
    splited = (coordinate[0], coordinate[1])
    return splited

def compare_records(azara_record, rui_record):
    azara_converted = convert_coordinate(azara_record[1])
    return bool(azara_converted == rui_record[1])

def create_record(azara_record, rui_record):
    if(compare_records(azara_record, rui_record)):
        return azara_record + rui_record
    else:
        return "not a match"

def clean_up(combined_record_group):
    texto = ""
    for i in combined_record_group:
        cleaned = ((i[0], i[2], i[3], i[4]))
        texto += str(cleaned) + "\n"
    return texto
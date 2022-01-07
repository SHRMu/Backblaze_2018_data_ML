
def read_file_to_list(file_folder, file_path):
    input_file_path = file_folder + '/' + file_path
    out_list = []
    with open(input_file_path, 'r') as in_f:
        for line in in_f:
            out_list.append(line.strip())
    return out_list
    
def write_list_to_file(input_list, output_file_folder, output_file_name):
    output_file_path = output_file_folder + '/' + output_file_name
    with open(output_file_path, 'w+') as out_f:
        for item in input_list:
            out_f.writelines(item+"\n")


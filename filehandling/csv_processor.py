import csv


def change_delimiter(old_del, new_del, in_file_path, out_file_path):
    reader = csv.reader(open(in_file_path, 'r'), delimiter=old_del)
    writer = csv.writer(open(out_file_path, 'w'), delimiter=new_del)
    writer.writerows(reader)


def hello_world():
    print('Hello World')

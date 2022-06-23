#from lxml import etree
import csv
import logger_new


# easy-peasy
def add_record(name: str, phone: str, adress: str):
    record = [name, phone, adress]

    logger_new.logger.info('ADD NEW RECORD')
    logger_new.logger_add_record(record)

    return record


def write_record_to_file(record: list, filename: str, format_type: str):
    logger_new.logger.info('START WRITE TO FILE.{format_type}')
    with open(f'{filename}.{format_type}', 'a') as file:
        for item in record:
            file.write(f'{item}    ')
        file.write('\n')
    logger_new.logger.info(F'CREATE NEW FILE {filename}.{format_type}')


# need to place flag on first strings (or detect format unique style)
def format_to_csv(filename: str):
    with open(f'{filename}.txt', 'r') as in_file:
        logger_new.logger.info('OPEN txt FOR IMPORT TO scv')
        in_file.readline()
        stripped = (line.strip() for line in in_file)
        lines = (line.split('    ') for line in stripped if line)
        with open(f'{filename}.csv', 'w') as out_file:
            writer = csv.writer(out_file)
            writer.writerow(('name', 'phone', 'adress'))
            writer.writerows(lines)
            logger_new.logger.debug(f'CREATE scv FILE {filename}.scv')
        


def format_to_txt(record: list):
    pass

# not correct yet
# def format_to_xml(filename: str):
#     root = etree.Element('data')
#
#     rdr = csv.reader(open(f'{filename}.csv'))
#     header = rdr.__next__()
#     for row in rdr:
#         eg = etree.SubElement(root, 'eg')
#         for h, v in zip(header, row):
#             etree.SubElement(eg, h).text = v
#
#     with open(f'{filename}.xml', 'w') as f:
#         f.write(etree.tostring(root))


def read_from_file(filename: str, format_type: str):
    logger_new.logger.info(f'OPEN FILE {filename}.{format_type} FOR READING')
    str_for_log = ''
    with open(f'{filename}.{format_type}', 'r') as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            if i == 0:
                logger_new.logger.error('The file is empty')
                pass
            else:
                str_for_log += str(i) + line.strip() + '\n'
                print(f'{i}. {line.strip()}')
    logger_new.logger.info(f'FILE {filename}.{format_type} has been read')
    logger_new.logger.debug(f'result||||\n{str_for_log}')

        


# r1 = add_record("Vasya Pupkin", "8-913-555-55-11", "Tverksaya st.")
# r2 = add_record("Levi Johann", '8-333-333-22-11', 'Zimbabwe, Cannibals st.')
# r3 = add_record("Chips Craboviy", "8-113-355-44-00", "Yamskaya st.")
# r4 = add_record("Aleksandr Buynov", "8-913-776-13-45", "Plushkina st.")
# write_record_to_file(r1, 'phonebook_1', 'txt')
# write_record_to_file(r2, 'phonebook_1', 'txt')
# read_from_file("phonebook_1", "txt")
# write_record_to_file(r3, 'phonebook_2', 'txt')
# write_record_to_file(r4, 'phonebook_2', 'txt')
format_to_csv('another_file')
# format_to_xml('another_file')
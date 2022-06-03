import os

# By Aleksei Rutkovskii

def cmd_executor(cmd_to_exec, output_file):
    os.system(f'cmd /c {cmd_to_exec} > {output_file}')


def driver_filter(output_file, encoding, driver_name):
    with open(f'{output_file}', encoding=encoding) as drivers:

        # Instead of print statements can also use 'logging' module
        print("Модуль       Название               Тип драйвера  Дата ссылки\n" +
            "============ ====================== ============= ======================")
        for line in drivers:
            if driver_name in line:
                print(line.strip())


def main(cmd_to_exec,output_file, encoding='utf8', driver_name='File System'):
    cmd_executor(cmd_to_exec, output_file)
    driver_filter(output_file=output_file, encoding=encoding, driver_name=driver_name)


if __name__ == '__main__':
    cmd = 'driverquery'
    output = 'WinDrivers.txt'
    enc = 'cp866'
    driver = 'File System'

    main(cmd_to_exec=cmd, output_file=output, encoding=enc, driver_name=driver)

    # can either use encoding 'utf8' for ENG Windows machines, \
    # but because I have RUS Windows machine I needed to use 'cp866'
import os


def create_project_dir(directory):
    if not os.path.exists(directory):
        print("Create a new directory " + directory)
        os.makedirs(directory)


def create_data_files(project_name, base_URL):
    queue = os.path.join(project_name, 'queue.txt')
    crawled = os.path.join(project_name, "crawled.txt")
    if not os.path.isfile(queue):
        write_file(queue, base_URL)
    if not os.path.isfile(crawled):
        write_file(crawled, ' ')  # Needed ' ' because in the first iteration there is no data passed to crawled


def write_file(path, data):
    with open(path, 'w') as file:
        file.write(data)


def append_to_file(path, data):  # Adds content (not overwriting)
    with open(path, 'a') as file:
        file.write(data, '\n')


def delete_file_contents(path):
    open(path, 'w').close()


def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as file:
        for line in file:
            results.add(line.replace('\n', ''))
    return results


def set_to_file(links, file_name):
    with open(file_name, 'w') as file:
        for line in sorted(links):
            file.write(line + '\n')



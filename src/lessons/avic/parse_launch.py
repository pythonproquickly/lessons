import itertools
import pathlib
import subprocess


INPUT_FILE = 'athinput.turb'
OUTPUT_FILE = INPUT_FILE

PATH = "/home/avi/Desktop/athena_Gravity/inputs/hydro/"
ATHENA_PATH = "/home/avi/Desktop/athena_Gravity/bin/athena"
FILE_TYPE = '*.scenario'


# change the value from None to a list of values here so you dont have to
# enter them.
# You don't need to do that for every key; you can mix and match.
# you can use expressions too - eg list(range(1,1000, 3) or whatever

prompts = {
    'four_pi_G': {
        'prompt': "Enter four_pi_G (separate multi values with ,): ",
        'value': None,
    },
    'nH': {
        'prompt': "Enter nH (separate multi values with ,): ",
        'value': None,
    }
}

with open(INPUT_FILE) as f:
    content = []
    for line in f:
        content.append(line.strip())
number_files = 1
for key, value in prompts.items():
    if value['value'] is None:
        value['value'] = input(value['prompt']).replace(' ', '').split(',')
    number_files *= len(value['value'])


new_contents = [[] for _ in range(number_files)]

determine_combinations = []
for keyword, value_data in prompts.items():
    determine_combinations.append(value_data['value'])
combinations = list(itertools.product(*determine_combinations))
prompt_keys = [key for key in prompts]
for file_number in range(number_files):
    for index, combination in enumerate(combinations):
        new_content = [] 
        setter = {}
        for value_index, value in enumerate(combination):
            setter[prompt_keys[value_index]] = value
        for line in content:
            needs_parsing = line.find('=')
            if needs_parsing > -1:
                keyword = line[:needs_parsing].strip()
                if keyword in setter:
                    line = f"{keyword} = {setter[keyword]}"
            new_content.append(line + '\n')
        name_portion = '-'.join(combination)
        with open(f"{OUTPUT_FILE}{name_portion}.scenario", 'w') as f:
            f.writelines(new_content)
        new_contents.append(new_content)


run_files = [filepath for filepath in pathlib.Path(PATH).rglob(FILE_TYPE)]
for file in run_files:
    print(
        f'{"".join([ATHENA_PATH + " ", "-i ", PATH, file.name])}')
        subprocess.run([
            "mkdir",
            file.name,
            " && ",
            "cd",
            file.name,
            " && ",
            ATHENA_PATH,
            "-i",
            PATH + file.name
        ])

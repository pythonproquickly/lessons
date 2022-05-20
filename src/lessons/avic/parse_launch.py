#!/usr/bin/env python
# coding: utf-8

# In[1]:


import itertools
import pathlib
import subprocess


# In[2]:


INPUT_FILE = 'athinput.turb'
OUTPUT_FILE = INPUT_FILE

PATH = "/home/avi/Desktop/athena_Gravity/inputs/hydro/" #path to 
 # changed to mine
FILE_TYPE = '*.scenario' #creates new input files 


# dictionary has a key for every field that we want to create parameter for in the file. 
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


# In[3]:


#list image with new lines removed

with open(INPUT_FILE) as f:
    content = []
    for line in f:
        content.append(line.strip())


# In[4]:


# how many files we need

number_files = 1
for key, value in prompts.items():
    value['value'] = input(value['prompt']).replace(' ', '').split(',')
    number_files *= len(value['value'])


# In[5]:


#

new_contents = [[] for _ in range(number_files)]

determine_combinations = []
for keyword, value_data in prompts.items():
    determine_combinations.append(value_data['value'])
combinations = list(itertools.product(*determine_combinations))
prompt_keys = [key for key in prompts]
for file_number in range(number_files):
    for index, combination in enumerate(combinations):
        new_content = [] 
        setter = {} #dictionary
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


# In[7]:


run_files = [filepath for filepath in pathlib.Path(PATH).rglob(FILE_TYPE)]
for file in run_files:
    print(
        f'{"".join(["/home/avi/Desktop/athena_Gravity/bin/athena ", "-i ", "~/Desktop/athena_Gravity/inputs/hydro/", file.name])}')
    subprocess.run(["/home/avi/Desktop/athena_Gravity/bin/athena", "-i",
                    "~/Desktop/athena_Gravity/inputs/hydro/" + file.name])


# In[ ]:





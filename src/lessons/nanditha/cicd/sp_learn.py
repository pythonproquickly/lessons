import subprocess

result = subprocess.run(['cat', 'stuff.txt',
                         ],
                        capture_output=True,
                        encoding='UTF-8')
print(result)

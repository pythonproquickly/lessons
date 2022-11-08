import subprocess

# step 1
result = subprocess.run(['docker',
                         'build',
                         '-t',
                         'andypy',
                         '/Users/andy/ws/lessons/src/lessons/nanditha/cicd'
                         '/Dockerfile'],
                        capture_output=True,
                        encoding='UTF-8')

# step 2

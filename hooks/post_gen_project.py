import os
import shutil
import subprocess

# дополнение файла backend/.gitignore
with open(os.getcwd()+"/backend/.gitignore", "a") as f:
    f.write('\nconfig.yaml')
    f.write('\nconfig-prod.yaml')
    f.write('\n.env')
    f.write('\n.env.prod')

# удаление фронтенда
REMOVE_PATHS = [
    '{% if cookiecutter.use_frontend != "y" %} ./frontend {% endif %}',
]

for path in REMOVE_PATHS:
    path = path.strip()
    if path and os.path.exists(path):
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.unlink(path)

# инициализация гит репозитория
subprocess.call(['git', 'init'])

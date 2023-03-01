import sys
import yaml


try:
    with open('../config.yaml', encoding='utf8') as f:
        settings = yaml.load(f, Loader=yaml.FullLoader)
except FileNotFoundError:
    sys.exit('Please create config.yaml before starting!')
except yaml.YAMLError:
    f.close()
    sys.exit('Invalid syntax of config.yaml!')
except KeyError:
    f.close()
    sys.exit('One or more keys are missing!')
else:
    f.close()

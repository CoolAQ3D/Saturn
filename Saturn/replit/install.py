
#Run the setup tools everytime replit runs to check if this library exist


import subprocess, os, sys
import pkg_resources

reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
installed_packages = [r.decode().split('==')[0] for r in reqs.split()]

def find_library(
  dev_mode=False
):
  reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
  installed_packages = [r.decode().split('==')[0] for r in reqs.split()]

  for package in ['Saturn']:
    try:
        dist = pkg_resources.get_distribution(package)
        print('{} ({}) is installed!'.format(dist.key, dist.version))
    except pkg_resources.DistributionNotFound:
        #print('{} is NOT installed'.format(package))
        print('Installing Toolbox Features!')

        if dev_mode:
           os.system("pip install -e .")
        else:
           os.system("pip install .")

# Python and Shell scripts for configuring new sites

### Requirements
- Python 3
- python-dotenv `pip install python-dotenv`

### Setup
- Clone repository
- Add to path. For [Windows](https://docs.alfresco.com/4.2/tasks/fot-addpath.html). For [Mac](https://www.architectryan.com/2012/10/02/add-to-the-path-on-mac-os-x-mountain-lion/).
- Copy .env.example to .env `cp .env.example .env`
- Fill out .env
  - EMAIL: Your email address
  - HOSTS_PATH: Absolute path to your hosts file (e.g. "C:/Windows/System32/drivers/etc/hosts")
  - VHOST_PATH: Absolute path to your vhost file (e.g. "C:/xampp/apache/conf/extra/httpd-vhosts.conf")
  - PYSCRIPTS_PATH: Absolute path to this directory
  
### Usage
#### Run all for SilverStripe project
- To generate all configurations, run `genall.sh project-name` in your project directory
#### Individual configs
- To generate hosts line, run `hosts.py s project-name` for SilverStripe project, run `hosts.py l project-name` for Laravel project
  - Run `hosts.sh` to edit hosts file directly
- To generate vhost block, run `vhost.py project-name`
- To generate .env, run `env.py project-name` in project directory

# Python and Shell scripts for configuring new sites

### Requirements
- Python 3
- python-dotenv `pip install python-dotenv`
- GitHub CLI

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
- To generate all configurations, run `genall.sh project-type project-name` in your project directory.
- `genall.sh project-type project-name xampp` for xampp configuration. Configures for Homestead by default.
#### Individual configs
- To generate hosts line, run `hosts.py project-name project-location`. For XAMPP project, run `hosts.py project-name x`. For Homestead project, run `hosts.py project-name h`.
  - Script backs up hosts in py-scripts directory as "hosts.txt".
  - Run `hosts.sh` to edit hosts file directly.
- To generate vhost block, run `vhost.py project-name`
- To generate homestead blocks, run `homestead.py project-type project-name`
- To generate .env, run `env.py project-type project-name` in project directory.
- `env.py project-type project-name x` for xampp configuration. Configures for Homestead by default.
- View Teamwork project with `tw.py`. If on the branch of an existing pull request, run `tw.py task` to view the task associated with the pull request.

if "%3" == "x" goto xampp
if "%3" == "xampp" goto xampp
hosts.py %2 h
homestead.py %1 %2
env.py %1 %2 h
goto end
:xampp
hosts.py %2 x
vhost.py %2
env.py %1 %2 x
:end
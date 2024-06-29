#config file changes
file {'/etc/ssh/ssh_config':
ensure=>present,
content=>"Host ubuntu\n\tHostName 54.236.30.220\n\tIdentityFile '~/.ssh/school'\n\tpasswordAuthentication no",
}

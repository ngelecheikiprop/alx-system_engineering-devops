#config file changes
file {'~/ssh/config':
ensure=>present,
content=>"Host ubuntu\n\tHostName 54.236.30.220\n\tIdentityFile '~/.ssh/school'\n\tpasswordAuthentication no",
}

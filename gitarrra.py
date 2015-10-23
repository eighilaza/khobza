# https://github.com/FriendCode/gittle

import gittle as g

auth = g.GittleAuth(pkey='/home/ubuntu/.ssh/id_rsa')

repo_path = '/home/ubuntu/tadjriba'
repo_url = 'git://ssh://10.10.10.10:2222/root/tadjriba.git'

repo = g.Gittle.init(repo_path)
#repo = g.Gittle(repo_path)
repo.stage('README.md')
repo.commit(name='toto toto', email='titi@gg.com', message='emchiii t3iiich')

import os
from subprocess import Popen, PIPE

output_path = '/data1/chenkexing/test'

title = 'wkentaro_gdown'

owner_name = title.split('_')[0]
repo_name  = title.split('_')[1]
job = 'pulls'

new_title = os.path.join(output_path, f"{title}_repos_{job}.jsonlines")
p = Popen(f'scrapy crawl get_github_repos_info_spider -a owner_name={owner_name} -a repo_name={repo_name} -a info={job} -O {new_title}', shell=True)
p.wait()

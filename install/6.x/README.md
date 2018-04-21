## How to Install Elasticsearch 6.x on AWS EC2
Please refer to [elasticsearch 5.x install](https://github.com/tonylixu/elasticsearch/tree/master/install/5.x) for instructions. The only thing you need to change here is the content of `/etc/yum.repos.d/elasticsearch.repo` file:
```bash
[elasticsearch-6.x]
name=Elasticsearch repository for 6.x packages
baseurl=https://artifacts.elastic.co/packages/6.x/yum
gpgcheck=1
gpgkey=https://artifacts.elastic.co/GPG-KEY-elasticsearch
enabled=1
autorefresh=1
type=rpm-md
```

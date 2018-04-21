## How to Install Elasticsearch on AWS EC2

### Env Configuration
* AMI: `amzn-ami-hvm-2017.09.1.20180307-x86_64-gp2 (ami-5b55d23f)`
* Instance Type: `t2.medium`


### Installation
* Create the elasticsearch repo file: Create a file called elasticsearch.repo in the /etc/yum.repos.d/ directory, containing:
```bash
[elasticsearch-5.x]
name=Elasticsearch repository for 5.x packages
baseurl=https://artifacts.elastic.co/packages/5.x/yum
gpgcheck=1
gpgkey=https://artifacts.elastic.co/GPG-KEY-elasticsearch
enabled=1
autorefresh=1
type=rpm-md
```
* Update repository database and do a install
```bash
$ yum update
$ yum install elasticsearch
Loaded plugins: priorities, update-motd, upgrade-helper
50 packages excluded due to repository priority protections
Resolving Dependencies
--> Running transaction check
---> Package elasticsearch.noarch 0:5.6.9-1 will be installed
--> Finished Dependency Resolution

Dependencies Resolved

=======================================================================================================================================
 Package                           Arch                       Version                      Repository                             Size
=======================================================================================================================================
Installing:
 elasticsearch                     noarch                     5.6.9-1                      elasticsearch-5.x                      32 M

Transaction Summary
=======================================================================================================================================
Install  1 Package

Total download size: 32 M
Installed size: 36 M
Is this ok [y/d/N]: y
Downloading packages:
elasticsearch-5.6.9.rpm                                                                                         |  32 MB  00:00:01
Running transaction check
Running transaction test
Transaction test succeeded
Running transaction
#
Creating elasticsearch group... OK
Creating elasticsearch user... OK
  Installing : elasticsearch-5.6.9-1.noarch                                                                                        1/1
### NOT starting on installation, please execute the following statements to configure elasticsearch service to start automatically using chkconfig
 sudo chkconfig --add elasticsearch
### You can start elasticsearch service by executing
 sudo service elasticsearch start
  Verifying  : elasticsearch-5.6.9-1.noarch                                                                                        1/1

Installed:
  elasticsearch.noarch 0:5.6.9-1

Complete!
```
* Update `elasticsearch.yml` configuration file:
  * Bind to VPN IP Address or Interface: Configure Elasticsearch such that it only allows access to servers on your private network (VPN)
```bash
network.host: [_eth0_, _local_]
```
* Set Cluster Name:
```bash
cluster.name: test
```
* Set Node Name
```bash
node.name: node569-1
```
* Set Discovery Hosts
```bash
# Note: Here I only set one node for the sake of simplicity
discovery.zen.ping.unicast.hosts: ["172.31.28.171"]
```

### Fix Java version
`elasticsearch` needs Java1.8, so
```bash
$ yum install java-1.8.0
$ yum remove java-1.7.0
$ java -version
openjdk version "1.8.0_161"
OpenJDK Runtime Environment (build 1.8.0_161-b14)
OpenJDK 64-Bit Server VM (build 25.161-b14, mixed mode)
```

### Start elasticsearch
```bash
$ service elasticsearch start
Starting elasticsearch:                                    [  OK  ]
```

### Check node status
```bash
curl http://localhost:9200
{
  "name" : "node569-1",
  "cluster_name" : "test",
  "cluster_uuid" : "nRclMs_9TOi-4z50UkYMQA",
  "version" : {
    "number" : "5.6.9",
    "build_hash" : "877a590",
    "build_date" : "2018-04-12T16:25:14.838Z",
    "build_snapshot" : false,
    "lucene_version" : "6.6.1"
  },
  "tagline" : "You Know, for Search"
}
```

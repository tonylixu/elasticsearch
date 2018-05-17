## A Place Holder for ECE Python3 Scripts


### Install Elastic Cloud Enterprise on the first host to start a new installation with your first availability zone.
```bash
bash <(curl -fsSL https://download.elastic.co/cloud/elastic-cloud-enterprise.sh) install --availability-zone MY_ZONE-1 --memory-settings '{"runner":{"xms":"1G","xmx":"1G"},"allocator":{"xms":"4G","xmx":"4G"},"proxy":{"xms":"8G","xmx":"8G"},"zookeeper":{"xms":"4G","xmx":"4G"},"director":{"xms":"1G","xmx":"1G"},"constructor":{"xms":"4G","xmx":"4G"},"admin-console":{"xms":"4G","xmx":"4G"}}'
```

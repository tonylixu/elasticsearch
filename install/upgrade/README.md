## Upgrade Your Eleasticsearch Cluster from 5.6.9 To 6.2.4

### Environment
* Existing ES cluster:
```bash
$ curl http://localhost:9200/_cat/nodes?h=ip,port,v,m,j,u,n
172.31.9.216  9300 5.6.9 - 1.8.0_161  9.3m node569-2
172.31.28.171 9300 5.6.9 * 1.8.0_161 32.9m node569-1

# on node569-1
$ curl -X GET "localhost:9200/_cat/indices?v"
health status index               uuid                   pri rep docs.count docs.deleted store.size pri.store.size
green  open   logstash-2015.05.20 _2oUbio4S-SGcDUf89p5gw   5   2       4750            0     87.1mb           29mb
green  open   shakespeare         BCR_Z0yLSveI83IKsYA1Jg   5   2     111396            0     85.7mb         28.5mb
green  open   bank                5pvpcbMhSXS_UWbbuOTZAQ   5   2       1000            0      1.8mb        640.8kb
green  open   logstash-2015.05.18 9Q7GLCNeTIiHS7ZGpbl3Eg   5   2       4631            0     85.2mb         28.4mb
green  open   logstash-2015.05.19 fkTaSWPkRRWTFRwheHODjw   5   2       4624            0     86.8mb         28.9mb

# on node569-2
$ curl -X curl -X GET "localhost:9200/_cat/indices?v"
health status index               uuid                   pri rep docs.count docs.deleted store.size pri.store.size
yellow open   logstash-2015.05.20 _2oUbio4S-SGcDUf89p5gw   5   2       4750            0     58.1mb           29mb
yellow open   shakespeare         BCR_Z0yLSveI83IKsYA1Jg   5   2     111396            0     57.1mb         28.5mb
yellow open   bank                5pvpcbMhSXS_UWbbuOTZAQ   5   2       1000            0      1.2mb        640.8kb
yellow open   logstash-2015.05.18 9Q7GLCNeTIiHS7ZGpbl3Eg   5   2       4631            0     56.8mb         28.4mb
yellow open   logstash-2015.05.19 fkTaSWPkRRWTFRwheHODjw   5   2       4624            0     57.9mb         28.9mb
```

### Install and configure a 6.2.4 ES node
Please refer to 'install' directory for how to set up a new `6.x` node.

### Join the new 6.2.4 node into the existing cluster
Make sure in your `/etc/elasticsearch/elasticsearch.yml` file, the discovery host is set to the exising node:
```bash
discovery.zen.ping.unicast.hosts: ["172.31.28.171"]
```

### Start the elasticsearch process on the new node
```bash
$ service elasticsearch start
Starting elasticsearch:                                    [  OK  ]

$ curl -X GET "localhost:9200"
{
  "name" : "node624-1",
  "cluster_name" : "test",
  "cluster_uuid" : "nRclMs_9TOi-4z50UkYMQA",
  "version" : {
    "number" : "6.2.4",
    "build_hash" : "ccec39f",
    "build_date" : "2018-04-12T20:37:28.497551Z",
    "build_snapshot" : false,
    "lucene_version" : "7.2.1",
    "minimum_wire_compatibility_version" : "5.6.0",
    "minimum_index_compatibility_version" : "5.0.0"
  },
  "tagline" : "You Know, for Search"
}
```
The node should auto-join the exisitng cluster:
```bash
$ curl http://localhost:9200/_cat/nodes?h=ip,port,v,m,j,u,n
172.31.9.216  9300 5.6.9 - 1.8.0_161 46.6m node569-2
172.31.28.171 9300 5.6.9 * 1.8.0_161  1.1h node569-1
172.31.7.141  9300 6.2.4 - 1.8.0_161 43.7m node624-1
```

### Check data
```bash
$ curl -X GET "localhost:9200/_cat/indices?v"
health status index               uuid                   pri rep docs.count docs.deleted store.size pri.store.size
green  open   logstash-2015.05.20 _2oUbio4S-SGcDUf89p5gw   5   2       4750            0     87.1mb           29mb
green  open   shakespeare         BCR_Z0yLSveI83IKsYA1Jg   5   2     111396            0     85.7mb         28.5mb
green  open   bank                5pvpcbMhSXS_UWbbuOTZAQ   5   2       1000            0      1.8mb        640.8kb
green  open   logstash-2015.05.18 9Q7GLCNeTIiHS7ZGpbl3Eg   5   2       4631            0     85.2mb         28.4mb
green  open   logstash-2015.05.19 fkTaSWPkRRWTFRwheHODjw   5   2       4624            0     86.8mb         28.9mb
```

### Check query
* On node569-1
```bash
$ curl -X GET "localhost:9200/bank/_search" -H 'Content-Type: application/json' -d'
{
  "query": { "match_all": {} },
  "size": 3
}
'
{"took":21,"timed_out":false,"_shards":{"total":5,"successful":5,"skipped":0,"failed":0},"hits":{"total":1000,"max_score":1.0,"hits":[{"_index":"bank","_type":"account","_id":"25","_score":1.0,"_source":{"account_number":25,"balance":40540,"firstname":"Virginia","lastname":"Ayala","age":39,"gender":"F","address":"171 Putnam Avenue","employer":"Filodyne","email":"virginiaayala@filodyne.com","city":"Nicholson","state":"PA"}},{"_index":"bank","_type":"account","_id":"44","_score":1.0,"_source":{"account_number":44,"balance":34487,"firstname":"Aurelia","lastname":"Harding","age":37,"gender":"M","address":"502 Baycliff Terrace","employer":"Orbalix","email":"aureliaharding@orbalix.com","city":"Yardville","state":"DE"}},{"_index":"bank","_type":"account","_id":"99","_score":1.0,"_source":{"account_number":99,"balance":47159,"firstname":"Ratliff","lastname":"Heath","age":39,"gender":"F","address":"806 Rockwell Place","employer":"Zappix","email":"ratliffheath@zappix.com","city":"Shaft","state":"ND"}}]}}
```
* On node624-1
```bash
$ curl -X GET "localhost:9200/bank/_search" -H 'Content-Type: application/json' -d'
{
  "query": { "match_all": {} },
  "size": 3
}
'
{"took":18,"timed_out":false,"_shards":{"total":5,"successful":5,"skipped":0,"failed":0},"hits":{"total":1000,"max_score":1.0,"hits":[{"_index":"bank","_type":"account","_id":"25","_score":1.0,"_source":{"account_number":25,"balance":40540,"firstname":"Virginia","lastname":"Ayala","age":39,"gender":"F","address":"171 Putnam Avenue","employer":"Filodyne","email":"virginiaayala@filodyne.com","city":"Nicholson","state":"PA"}},{"_index":"bank","_type":"account","_id":"44","_score":1.0,"_source":{"account_number":44,"balance":34487,"firstname":"Aurelia","lastname":"Harding","age":37,"gender":"M","address":"502 Baycliff Terrace","employer":"Orbalix","email":"aureliaharding@orbalix.com","city":"Yardville","state":"DE"}},{"_index":"bank","_type":"account","_id":"99","_score":1.0,"_source":{"account_number":99,"balance":47159,"firstname":"Ratliff","lastname":"Heath","age":39,"gender":"F","address":"806 Rockwell Place","employer":"Zappix","email":"ratliffheath@zappix.com","city":"Shaft","state":"ND"}}]}}
```

### Next Step:
Keep adding new nodes to the cluster one by one, once all added, stop services on the old nodes one by one, remeber to update the `discovery.zen.ping.unicast.hosts` at the end!

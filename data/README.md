## Load data into ES
Let's load some data into your ES cluster!

### Set up mapping for Shakespeare data
On one of the node:
```bash
$ curl -X PUT "localhost:9200/shakespeare" -H 'Content-Type: application/json' -d'
{
 "mappings": {
  "doc": {
   "properties": {
    "speaker": {"type": "keyword"},
    "play_name": {"type": "keyword"},
    "line_id": {"type": "integer"},
    "speech_number": {"type": "integer"}
   }
  }
 }
}
'
```

### Establish geo_point mapping for the logs:
```bash
$ curl -X PUT "localhost:9200/logstash-2015.05.18" -H 'Content-Type: application/json' -d'
{
  "mappings": {
    "log": {
      "properties": {
        "geo": {
          "properties": {
            "coordinates": {
              "type": "geo_point"
            }
          }
        }
      }
    }
  }
}
'
$ curl -X PUT "localhost:9200/logstash-2015.05.19" -H 'Content-Type: application/json' -d'
{
  "mappings": {
    "log": {
      "properties": {
        "geo": {
          "properties": {
            "coordinates": {
              "type": "geo_point"
            }
          }
        }
      }
    }
  }
}
'
$ curl -X PUT "localhost:9200/logstash-2015.05.20" -H 'Content-Type: application/json' -d'
{
  "mappings": {
    "log": {
      "properties": {
        "geo": {
          "properties": {
            "coordinates": {
              "type": "geo_point"
            }
          }
        }
      }
    }
  }
}
'
```

### use the Elasticsearch bulk API to load the data sets with the following commands:
```bash
$ curl -H 'Content-Type: application/x-ndjson' -XPOST 'localhost:9200/bank/account/_bulk?pretty' --data-binary @accounts.json
$ curl -H 'Content-Type: application/x-ndjson' -XPOST 'localhost:9200/shakespeare/doc/_bulk?pretty' --data-binary @shakespeare_6.0.json
$ curl -H 'Content-Type: application/x-ndjson' -XPOST 'localhost:9200/_bulk?pretty' --data-binary @logs.jsonl
```

### Verify successful loading with the following command:
```bash
$ curl -X GET "localhost:9200/_cat/indices?v"
yellow open   logstash-2015.05.20 _2oUbio4S-SGcDUf89p5gw   5   1       4750            0       29mb           29mb
yellow open   shakespeare         BCR_Z0yLSveI83IKsYA1Jg   5   1     111396            0     28.5mb         28.5mb
yellow open   bank                5pvpcbMhSXS_UWbbuOTZAQ   5   1       1000            0    640.3kb        640.3kb
yellow open   logstash-2015.05.18 9Q7GLCNeTIiHS7ZGpbl3Eg   5   1       4631            0     28.4mb         28.4mb
yellow open   logstash-2015.05.19 fkTaSWPkRRWTFRwheHODjw   5   1       4624            0     28.9mb         28.9mb
```

### Reference:
https://www.elastic.co/guide/en/kibana/current/tutorial-load-dataset.html

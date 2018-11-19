import requests
import json
import sys
from string import Template
elastic_url="http://localhost:9200"
query_index,query_string="test", "Handbill not printed"
# "Handbill not printed"
time_interval = "3h"
alert_threshold=3
body_template = Template("""
{
	"query" : {
		"bool": {
			"must": [
				{"regexp": {"message": { "value": ".*$query_string.*"}
        			}
        		},
        		{"range": {
        			"timestamp": { 
        				"gte" : "now-$time_interval",
                		"lt" :  "now"
        			}
        		}
        		}
        		]
			}
			
		}
	}
}
""")
headers={"Content-Type": "application/json"}
request_body = body_template.substitute(query_string=query_string, time_interval=time_interval)
try:
    contents = requests.get(f"{elastic_url}/{query_index}/_count", data=request_body, headers=headers)
    response_body=json.loads(contents.text)
    count = int(response_body["count"])
    sys.stdout.write(str(1 if count >= alert_threshold else 0))
    sys.stdout.flush()
    exit(0)
except Exception as e:
    exit(-2)
import models
import json
import elasticsearch


# elasticsearch --config=/usr/local/opt/elasticsearch/config/elasticsearch.yml

es = elasticsearch.Elasticsearch()

for v in models.Venue.objects.all():
    v_dict = {}
    v_dict['name'] = v.name
    v_dict['location'] = json.loads(v.location)
    v_dict['menu'] = json.loads(v.menu)
    v_dict['stats'] = json.loads(v.stats)
    v_dict['categories'] = json.loads(v.categories)

    tips = v.tip_set.all()
    tips_dict = [t.as_dict() for t in tips]
    v_dict['tips'] = tips_dict

    es.index(index='4sreviews', doc_type='venues', id=v.venue_id, body=v_dict)

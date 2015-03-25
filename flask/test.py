import elasticsearch
import unittest


class SearchCategoryTest(unittest.TestCase):

    def setUp(self):
        self.es = elasticsearch.Elasticsearch()
        self.query = """
{
  "query": {
    "bool": {
      "should": [
        {
          "match": {
            "categories.shortName": {
                query: "malaysia",
                analyzer: "english",
                fuzziness: "auto"
            }
          }
        }
      ]
    }
  }
}
"""

    def test_category_analyzer(self):
        venue_id = '516c0f4ce4b0209bc53d2c5c'
        returned_query = self.es.search(index='4sreviews', doc_type='venues',
                                        body=self.query)
        results = returned_query['hits']['hits']
        results_id = [r['_id'] for r in results]
        self.assertIn(venue_id, results_id)

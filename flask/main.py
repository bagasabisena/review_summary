from flask import Flask, render_template, request
import json
import elasticsearch
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', name='Bagas', age='25')

# # @app.route('/bagas')
# # def hello_world():
#     return 'Hello Bagas!'


@app.route('/search')
def search():
    es = elasticsearch.Elasticsearch()
    query = request.args.get('q', '')
    body = """
{
        "query": {
            "match": {
                "name": {
                    query: "%s",
                    fuzziness: "AUTO",
                    analyzer: "simple"
                }
            }
        }
}
""" % (query,)
    returned_query = es.search(index='4sreviews', doc_type='venues',
                               body=body)
    results = returned_query['hits']['hits']
    print results[0]
    return render_template('search.html', query=query, results=results)


if __name__ == '__main__':
    app.run(debug=True)

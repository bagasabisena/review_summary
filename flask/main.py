from flask import Flask, render_template, request
from flaskext.mysql import MySQL
import elasticsearch
app = Flask(__name__)


mysql=MySQL()
app=Flask(__name__)
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Pollikan290592'
app.config['MYSQL_DATABASE_DB'] = '4sreviews'
app.config['MYSQL_DATABASE_HOST'] = 'www.pollican.com'
mysql.init_app(app)

@app.route('/')
def index():
    cursor=mysql.connect().cursor()
    cursor.execute("select distinct(region) from users")
    rows = cursor.fetchall()

    for row in rows:
        row="%s" %row
        print row
    return render_template('index.html',rows=rows)


@app.route('/search')
def search():
    es = elasticsearch.Elasticsearch()
    query = request.args.get('q', '')
    body = """
{
  "query": {
    "bool": {
      "should": [
        {
          "match": {
            "name": {
                "query": "%s",
                "analyzer": "simple",
                "fuzziness": "auto"
            }
          }
        },
        {
          "match": {
            "categories.shortName": {
                "query": "%s",
                "analyzer": "english",
                "fuzziness": "auto"
          }
            }
        },
        {
            "match": {
                "tips.text": {
                    "query":"%s",
                    "analyzer": "english",
                    "fuzziness": "auto"
                }
            }
        }
      ]
    }
  }
}
""" % (query, query, query)
    returned_query = es.search(index='4sreviews', doc_type='venues',
                               body=body)
    results = returned_query['hits']['hits']
    return render_template('search.html', query=query, results=results)


@app.route('/venue/<venue_id>')
def venue(venue_id):
    es = elasticsearch.Elasticsearch()
    venue = es.get(index='4sreviews', doc_type='venues', id=venue_id)
    cursor=mysql.connect().cursor()
    cursor.execute("select user_id,ph from venues where venue_id='"+venue_id+"'")
    data=cursor.fetchone()
    print data
    return render_template('venue.html', venue=venue)


if __name__ == '__main__':
    app.run(debug=True)

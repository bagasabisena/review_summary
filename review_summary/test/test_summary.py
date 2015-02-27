import unittest
import json
from review_summary import models


class SentenceTest(unittest.TestCase):

    def setUp(self):
        self.sentence = 'His recommendations were to try the Reuben, Fish Sandwich and Open-Faced Steak Sandwich.'

    def test_features_of_sentence(self):
        features = ['recommendations',
                    'reuben', 'fish sandwich',
                    'open-faced steak sandwich']
        s = models.Sentence(self.sentence)
        self.assertListEqual(s.features, features)


class ReviewTest(unittest.TestCase):

    def setUp(self):
        self.review = "Seen this restaurant on 25 best places in Pittsburgh with Rick Seback\nack. Went there with my girlfriend she grew up with the owner. She's very nice all employees are super nice service was excellent i had the fish sandwich my girlfriend had the Ruben more than you could possibly eat very reasonable prices. Going back to try the burgers  i heard there enormous and very tasty."

    def test_features_for_one_review(self):
        review = models.Review(self.review)

        self.assertIn('fish sandwich', review.features)
        self.assertIn('burgers', review.features)


class ReviewSetTest(unittest.TestCase):

    def setUp(self):
        with open('review_summary/test/reviews.json', 'r') as f:
            self.reviews = json.load(f)

    def test_features_of_review_set(self):
        reviewSet = models.ReviewSet(self.reviews)
        reviewSet.create_transaction_list()

        self.assertEqual(len(reviewSet.features), 10)
        self.assertIn('fish sandwich', reviewSet.features)
        self.assertIn('reuben', reviewSet.features)

import unittest
import requests
import json
from jsonpath import jsonpath

class TestStringMethods(unittest.TestCase):

# Tests for the main website

    def test1(self):
        response = requests.get('http://amdbmovie.com/api/comments/showComments?movieId=580489')
        comments = jsonpath(response.json(),'$..comment')
        commentToCompare = "I wasn't expecting that much right before the movie came out. I actually really enjoyed it! This movie features Eddie Brock interviewing Cletus Kassidy and getting him executed. Cletus bites him and gets some substance from Venom's symbiote body and while about to be executed turns into the villain Carnage. I say that Carnage might be my favorite Spider-Man villain if only because he's the most evil. He actually does manage to get some sympathetic traits as he cares about his girlfriend as her powers aren't compatible with Carnage's.That's really an interesting idea for supervillain couples. Carnage doesn't appear until a half hour in and for a superhero (or mostly supervillain) movie, that's kind of short, but I still felt it got in what it needed to be. I admit it was weird seeing how goofy Venom and Eddie were interacting. They still worked, but weren't quite on type. The best part is of course, the scene at the very end.Venom's been teleported to the MCU. ***\n"
        self.assertEqual(comments[2], commentToCompare)

    def test2(self):
        response = requests.get('http://amdbmovie.com/api/rec/getRecommendationById?movieId=580489')
        popularities = jsonpath(response.json(),'$..popularity')
        self.assertEqual(popularities[0], 422.39)

    def test3(self):
        response = requests.get('http://amdbmovie.com/api/rec/getRecommendationById?movieId=580489')
        overviews = jsonpath(response.json(),'$..overview')
        self.assertEqual(overviews[1], 'The seemingly invincible Spider-Man goes up against an all-new crop of villains\u2014including the shape-shifting Sandman. While Spider-Man\u2019s superpowers are altered by an alien organism, his alter ego, Peter Parker, deals with nemesis Eddie Brock and also gets caught up in a love triangle.')

    def test4(self):
        response = requests.get('http://amdbmovie.com/api/rec/getRecommendationById?movieId=580489')
        runtimes = jsonpath(response.json(),'$..runtime')
        self.assertEqual(runtimes[2], 120)

    def test5(self):
        response = requests.get('http://amdbmovie.com/api/comments/showComments?movieId=580489')
        userNames = jsonpath(response.json(),'$..userName')
        self.assertEqual(userNames[0], 'wxywxy')

    def test6(self):
        response = requests.get('http://amdbmovie.com/api/comments/showComments?movieId=580489')
        islockeds = jsonpath(response.json(),'$..ifBlocked')
        self.assertEqual(islockeds[0], 0)

    def test7(self):
        response = requests.get('http://amdbmovie.com/api/movieTmdb/movieTmdbReviews?movieId=580489')
        authors = jsonpath(response.json(),'$..author')
        self.assertEqual(authors[0], 'garethmb')

    def test8(self):
        response = requests.get('http://amdbmovie.com/api/movieTmdb/movieTmdbReviews?movieId=580489')
        toxicities = jsonpath(response.json(),'$..toxic')
        self.assertEqual(toxicities[0][0][0], 0.190044492)

    def test9(self):
        response = requests.get('http://amdbmovie.com/api/movieTmdb/movieTmdbReviews?movieId=580489')
        dates = jsonpath(response.json(),'$..updated_at')
        self.assertEqual(dates[0], '2021-09-30T13:48:10.279Z')

    def test10(self):
        response = requests.get('http://amdbmovie.com/api/movieImdb/movieImdbReviews?movieId=tt7097896')
        toxicities = jsonpath(response.json(),'$..toxic')
        self.assertEqual(toxicities[0][0][0], 0.326610476)

# Tests for the admin page

    def test11(self):
        result = False
        response = requests.get('http://amdbmovie.com/api/admin/userList')
        userNames = jsonpath(response.json(),'$..userName')
        for x in userNames:
            if(x == 'egowic'):
                result = True
        self.assertEqual(True, result)

    def test12(self):
        result = False
        response = requests.get('http://amdbmovie.com/api/admin/userList')
        userNames = jsonpath(response.json(),'$..userName')
        for x in userNames:
            if(x == 'Pingan Zhang'):
                result = True
        self.assertEqual(True, result)

    def test13(self):
        result = False
        response = requests.get('http://amdbmovie.com/api/admin/userList')
        userNames = jsonpath(response.json(),'$..email')
        for x in userNames:
            if(x == 'tengkaigao11@gmail.com'):
                result = True
        self.assertEqual(True, result)

    def test14(self):
        result = False
        response = requests.get('http://amdbmovie.com/api/admin/userList')
        userNames = jsonpath(response.json(),'$..overView')
        for x in userNames:
            if(x == 'Hello there.'):
                result = True
        self.assertEqual(True, result)

    def test15(self):
        result = False
        response = requests.get('http://amdbmovie.com/api/admin/commentsList')
        userNames = jsonpath(response.json(),'$..comment')
        for x in userNames:
            if(x == 'shit movie '):
                result = True
        self.assertEqual(True, result)

    def test16(self):
        result = False
        response = requests.get('http://amdbmovie.com/api/admin/commentsList')
        comments = jsonpath(response.json(),'$..comment')
        for x in comments:
            if(x == 'fuck off'):
                result = True
        self.assertEqual(True, result)

    def test17(self):
        result = False
        response = requests.get('http://amdbmovie.com/api/admin/commentsList')
        comments = jsonpath(response.json(),'$..comment')
        toxicties = jsonpath(response.json(),'$..toxic')
        counter = 0
        for x in comments:
            counter += 1
            if(x == 'fuck off' and toxicties[counter - 1] == '0.999747038'):
                result = True

        self.assertEqual(True, result)

    def test18(self):
        result = False
        response = requests.get('http://amdbmovie.com/api/admin/commentsList')
        comments = jsonpath(response.json(),'$..comment')
        toxicties = jsonpath(response.json(),'$..toxic')
        counter = 0
        for x in comments:
            counter += 1
            if(x == 'Venom: Let there be carnage - Civil War - Infinity War - Endgame - Into the Spide\u2026' and toxicties[counter - 1] == '0.184846252'):
                result = True

        self.assertEqual(True, result)

    def test19(self):
        result = False
        response = requests.get('http://amdbmovie.com/api/admin/commentsList')
        comments = jsonpath(response.json(),'$..comment')
        sentimenties = jsonpath(response.json(),'$..sentiment')
        counter = 0
        for x in comments:
            counter += 1
            if(x == 'fuck off' and sentimenties[counter - 1] == '2.0'):
                result = True

        self.assertEqual(True, result)

    def test20(self):
        result = False
        response = requests.get('http://amdbmovie.com/api/admin/commentsList')
        comments = jsonpath(response.json(),'$..comment')
        sentimenties = jsonpath(response.json(),'$..sentiment')
        counter = 0
        for x in comments:
            counter += 1
            if(x == 'I got the download of it for free months ago like during september! If you want the dowload I will give you it if I get a reply or something! 2021/12/10<br>I will make an edit or reply if someone wants it!' and sentimenties[counter - 1] == '1.0'):
                result = True

        self.assertEqual(True, result)


if __name__ == '__main__':
    unittest.main()
import tweepy
import csv

# Fill the X's with the credentials obtained by
# following the above mentioned procedure.
consumer_key = "qkBPh6AyQdEZ1HbMZyJlCWYjt"
consumer_secret = "FileFXfTA6QnLFiRgmGvkdtnf8JZ2NLlKa9jpl6wKdhB0SGEbz"
access_key = "191424283-WKGqUOZNYQslqqtjK5ryrx3hwRBwUFOn8BirdIMi"
access_secret = "VJcFczwjYpKyHjKRQQybpMw7prL1eTRqzntOyN89uRzqN"


# Function to extract tweets
def get_tweets(username):
    # OAuth process, using the keys and tokens
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)

    # Creation of the actual interface, using authentication
    api = tweepy.API(auth)

    results = api.search(username, count=500)

    csvfile = open('input.csv', 'wb')
    csvwriter = csv.writer(csvfile)

    for item in results:
        print(results)
        # write out the user, the tweet and their follower count into a file
        # the unicode bits are required to write non ASCII language bits into the file
        csvwriter.writerow([unicode(item.user.screen_name).encode("utf-8"), unicode(item.text).encode("utf-8"),
                            item.user.followers_count])
    # time.sleep(1)


# Driver code
if __name__ == '__main__':
    # Here goes the twitter handle for the user
    # whose tweets are to be extracted.
    get_tweets("mucinex")
    get_tweets("#dettol")
    # get_tweets("nurofen")
    # get_tweets("@VeetIndia")
    # get_tweets("@clearasil")
    # get_tweets("@durex")
    # get_tweets("#dettol")
    # get_tweets("@MerckCanada")
    # get_tweets("@KnowHPV")
    # get_tweets("@KnowHPVForAll")
    # get_tweets("@Merck")
    # get_tweets("@MerckCanada")
    # get_tweets("@MerckCanada_FR")
    # get_tweets("@MerckEngage")
    # get_tweets("@MerckforMothers")
    # get_tweets("@MerckIMInspired")
    # get_tweets("@MerckManualHome")
    # get_tweets("@MerckManualPet")
    # get_tweets("@MerckManualPro")
    # get_tweets("@MerckSupport")
    # get_tweets("@MerckVetManual")
    # get_tweets("@MSDBelgium")
    # get_tweets("@msdcareers")
    # get_tweets("@MSDCyprus")
    # get_tweets("@MSDCzech")
    # get_tweets("@MSDDanmark")
    # get_tweets("@msdegypt")
    # get_tweets("@MSDEspana")
    # get_tweets("@MSDFinland")
    # get_tweets("@MSDFrance")
    # get_tweets("@MSDGreece")
    # get_tweets("@MSDinnofactory")
    # get_tweets("@MSDintheUK")
    # get_tweets("@MSDInvents")
    # get_tweets("@MSDKesfediyor")
    # get_tweets("@MSDLatAm")
    # get_tweets("@MSDLebanon")
    # get_tweets("@MSDManualHome")
    # get_tweets("@MSDManualPro")
    # get_tweets("@MSDNederland")
    # get_tweets("@MSDNorge")
    # get_tweets("@MSDOncologie")
    # get_tweets("@MsdPolska")
    # get_tweets("@msdsalute")
    # get_tweets("@MSDSerbia")
    # get_tweets("@MsdSlovensko")
    # get_tweets("@MSDSverige")
    # get_tweets("@MSD_Aus")
    # get_tweets("@MSD_Austria")
    # get_tweets("@MSD_Deutschland")
    # get_tweets("@msd_es")
    # get_tweets("@MSD_JAPAN")
    # get_tweets("@MSD_jordan")
    # get_tweets("@MSDBelgium")
    # get_tweets("@msd_portugal")
    # get_tweets("@MSD_Romania")
    # get_tweets("@MSD_Slovenia")
    # get_tweets("@MSD_SouthAfrica")
    # get_tweets("@MSD_Switzerland")
    # get_tweets("@MyMSDBeLux")
    # get_tweets("@OnlyMomCan")
    # get_tweets("@vreehealth_it")
    # get_tweets("g.zarez")
    # get_tweets("msdgcc")






















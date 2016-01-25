import numpy as np
import matplotlib.pyplot as plt

def load_tweet(line):
    output = {}
    line = line.strip()
    cells = line.split(',')
    output['seconds'] = float(cells[0])
    output['length'] = int(cells[1])
    output['candidates'] = (cells[2].split('|') if cells[2] else [])
    output['retweet'] = cells[3]
    output['when'] = int(cells[4])
    output['polarity'] = float(cells[5])
    output['subjectivity'] = float(cells[6])
    output['long'] = (float(cells[7]) if cells[7] else None)
    output['lat'] = (float(cells[8]) if cells[8] else None)

    return output

def load_tweet_list(file_name):
    output = []
    with open(file_name) as file:
        header_line = file.readline()
        line = file.readline()
        while line:
            tweet = load_tweet(line)
            output.append(tweet)
            line = file.readline()

        # open will open the file name, but with open will open and automatically close and release the memory
        # readline will read one line from the file at a time
        # each time call readline will get the next line and advance the pointer

        #file takes "with open(file_name)" function as its definition

    return output

def main():
    #loading csv file into memory
    tweet_list = load_tweet_list('tweets.csv')

    #print results
    print(tweet_list[:10])

#conduct analysis on tweets

    #show no. of tweet mentions per candidate
    #plt.plot([x='candidates'][y='']



    #show no. of tweet mentions per candidate over time

    #show no. of tweet mentions per minute for candidates, only during the debate

    #stackplot of % of mentions over time

    #show polarity associated w/ candidates over time
        #could be over avg'ed polarity over 5 second intervals (divided by number of mentions?)
        #could just be averages before, during, and after debates
            #going to be limited b/c of how narrow the dataset is - just a 51 hour period and public opinion doesn't change that fast
            # but could potentially show that twitter is faster in detecting change in opinion than polls?

if __name__ == '__main__':
    main()


# code should be functional, in that constantly passing and using things that are explicitly passed in
# example as in, loadtweetlist could be a global variable and could be implicitly passed/used in all the sections, but
    # by defining it upfront as a variable means have to explicitly pass into next section

# Coronavirus - the manipulation


[Benford’s law](https://web.williams.edu/Mathematics/sjmiller/public_html/math/talks/Benford_Brown2012.pdf), in short, is a statistical test to check if a set of numbers describing some phenomenon (your tax return, a natural disaster, stock prices or traffic volume on the highway) has been manipulated.

Its power comes from a mistake humans often do when making up numbers: they distribute the digits really nicely and evenly across the interval they want.
For most normal unaltered datasets, though, this doesn’t actually happen. In fact, the leading digit of each number is much more likely to be a 1 (~30%) than a 9. There are many explanations for this behavior, and I encourage you to look it [up](https://en.wikipedia.org/wiki/Benford%27s_law), but the gist of it is that if your dataset doesn’t fit exactly in a specific order of magnitude but spills over to the next one, or just uses half of it, low numbers will be more likely to appear.

If you’ve followed me so far, you might think that Benford's law is pretty fucking awesome. That’s because it is. It has been used by the US tax bureau (the IRS) to catch [cheats](http://www.thetaxbook.com/updates/TheTaxBook/Updates/2013-06-21_Benfords_Law.pdf), in Europe to find that Greece was cooking its balance [books](https://onlinelibrary.wiley.com/doi/full/10.1111/j.1468-0475.2011.00542.x), to highlight manipulation of [elections](https://sbseminar.wordpress.com/2009/06/15/benfords-law-and-the-iranian-election/), and by your high-school science professor to know that half your class was cheating on the assignment. How awesome is that?

Now, it seems that nobody has applied Benford’s law to the latest Coronavirus outbreak yet (I’m writing in 2020, you future jetpack-powered reader).

Let’s fix that. What you’ll find is that China has been delightfully truthful about its Coronavirus numbers. 

Just kidding.

So, first things first. The assumptions to use this statistical test are (copied straight from this [fantastic blog](https://towardsdatascience.com/frawd-detection-using-benfords-law-python-code-9db8db474cf8), which you should read):

* The numbers need to be random and not assigned, with no imposed minimums or maximums.
* The numbers should cover several orders of magnitude, and the dataset should be large; recommendations in the literature call for 100 to 1,000 samples as a minimum, though Benford’s law has been shown to hold true for datasets containing as few as 50 numbers.
 
 
We’re in luck! We have datasets that satisfy those assumptions, and they come straight from Chinese websites.
I took the liberty of scraping those websites (pretty manually), and copying the numbers here.
Here’s what the Benford’s law says:

```
########################
Dataset name: dataset_qq_02_14.txt
Min value in dataset: 0
Max value in dataset: 51986
Dataset size: 281
Benford law applies (if the source of numbers is 'good', e.g., a natural phenomenon).

Chi-squared Test Statistic = 27.855
Critical value at a P-value of 0.05 is 15.51.
The data appears to have been manipulated.

########################
Dataset name: dataset_dxy_02_14.txt
Min value in dataset: 1
Max value in dataset: 51986
Dataset size: 1351
Benford law applies (if the source of numbers is 'good', e.g., a natural phenomenon).

Chi-squared Test Statistic = 33.350
Critical value at a P-value of 0.05 is 15.51.
The data appears to have been manipulated.
########################
Dataset name: dataset_qq_02_18.txt
Min value in dataset: 0
Max value in dataset: 61682
Dataset size: 312
Benford law applies (if the source of numbers is 'good', e.g., a natural phenomenon).

Chi-squared Test Statistic = 17.694
Critical value at a P-value of 0.05 is 15.51.
The data appears to have been manipulated.
########################
Dataset name: dataset_dxy_02_18.txt
Min value in dataset: 1
Max value in dataset: 75200
Dataset size: 1470
Benford law applies (if the source of numbers is 'good', e.g., a natural phenomenon).

Chi-squared Test Statistic = 34.919
Critical value at a P-value of 0.05 is 15.51.
The data appears to have been manipulated.
```

**All datasets so far appear to be manipulated**. Think about that. 

*This test is configured to give incorrect positive results in 5% of the cases at max. Datasets are sampled at random, the days that I remember to do it.*

Now, there could potentially be a bug in the code. However, if you copy-n-paste the dataset in an online Benford calculator (like [this](https://www.dcode.fr/benford-law)), the result stay the same.  Benford’s law consistently points toward manipulation.

You’ve got to the end of the post. Congrats! If you think this post is interesting and should be read by others, please share it on social media. I am terrible at that. Thanks for reading!



Edit: probably unrelated, but this github account has been flagged :)

![flagged](https://raw.githubusercontent.com/theitalianscientist/covid-19/master/Screen%20Shot%202020-02-18%20at%208.35.51%20PM.png)

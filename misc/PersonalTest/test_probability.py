import scipy.stats as stats
import math

def one_sample_ztest_pop_proportion(tail, p, pbar, n, alpha):
    #Calculate test stat

    sigma = math.sqrt((p*(1-p))/(n))
    z = round((pbar - p) / sigma, 2)

    if tail == 'lower':
        pval = round(stats.norm(p, sigma).cdf(pbar),4)
        print("Results for a lower tailed z-test: ")


    elif tail == 'upper':
        pval = round(1 - stats.norm(p, sigma).cdf(pbar),4)
        print("Results for an upper tailed z-test: ")


    elif tail == 'two':
        pval = round(stats.norm(p, sigma).cdf(pbar)*2,4)
        print("Results for a two tailed z-test: ")


    #Print test results
    print("Test statistic = {}".format(z))   
    print("P-value = {}".format(pval))
    print("Confidence = {}".format(alpha))

    #Compare p-value to confidence level
    if pval <= alpha:
        print("{} <=  {}. Reject the null hypothesis.".format(pval, alpha))
    else:
        print("{} > {}. Do not reject the null hypothesis.".format(pval, alpha))


#one_sample_ztest_pop_proportion('upper', .20, .25, 400, .05)

#one_sample_ztest_pop_proportion('two', .64, .52, 100, .05)

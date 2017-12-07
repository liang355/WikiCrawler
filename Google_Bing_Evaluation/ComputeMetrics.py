
google_query1_relevancy = [1,1,1,1,1,0,1,1,0,1,1,0,1,1,1,0,0,0,0,0]
google_query2_relevancy = [1,1,1,1,1,1,1,1,0,1,0,1,1,1,1,0,0,0,0,0]
bing_query1_relevancy = [1,1,1,0,1,1,0,1,1,1,0,1,1,1,1,0,0,0,0,0]
bing_query2_relevancy = [1,1,1,1,1,0,1,1,1,0,0,1,1,1,1,0,0,0,0,0]


def calculate_precision(relevancies):
    count = 0
    sum = 0
    precision_5 = 0
    precision_10 = 0
    precision_16 = 0
    for relevancy in relevancies:
        count += 1
        sum += relevancy
        if count == 5:
            precision_5 = sum / float(count)
        if count == 10:
            precision_10 = sum / float(count)
        if count == 16:
            precision_16 = sum / float(count)
    print 'Rank5:' + str(precision_5) + ', Rank10:' + str(precision_10) + ', Rank16:' + str(precision_16)
    return precision_5, precision_10, precision_16


print '\nGoogle Query1 Result Precisions:'
pre_g_1_rank5, pre_g_1_rank10, pre_g_1_rank16 = calculate_precision(google_query1_relevancy)

print '\nBing Query1 Result Precisions:'
pre_b_1_rank5, pre_b_1_rank10, pre_b_1_rank16 = calculate_precision(bing_query1_relevancy)

print '\nGoogle Query2 Result Precisions:'
pre_g_2_rank5, pre_g_2_rank10, pre_g_2_rank16 = calculate_precision(google_query2_relevancy)

print '\nBing Query2 Result Precisions:'
pre_b_2_rank5, pre_b_2_rank10, pre_b_2_rank16 = calculate_precision(bing_query2_relevancy)

google_mean_avg = (pre_g_1_rank10 + pre_g_2_rank10) / float(2)
bing_mean_avg = (pre_b_1_rank10 + pre_b_2_rank10) / float(2)

print ''
print 'google_mean_avg: ' + str(google_mean_avg)
print 'bing_mean_avg: ' + str(bing_mean_avg)
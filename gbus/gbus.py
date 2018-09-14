def naive(verbose):
    t_test_case_count = input()
    if verbose:
        print "T=%d (Test Case Count)" % t_test_case_count

    for test_case_index in range(0, t_test_case_count):
        n_gbus_count = input()
        if verbose:
            print "N=%d (Gbus Count for Test Case %d)" % (n_gbus_count, test_case_index)

        gbus_ranges = []

        gbus_service_range_raw_line = raw_input()
        gbus_service_range_raw_line_split = gbus_service_range_raw_line.split(' ')

        for i in range(0, n_gbus_count * 2, 2):
            gbus_ranges.append(
                [int(gbus_service_range_raw_line_split[i]), int(gbus_service_range_raw_line_split[i + 1])])

        if verbose:
            print ("Gbus service ranges for Test Case %d" % test_case_index), gbus_ranges

        p_city_count = input()

        if verbose:
            print "P=%d (City count for Test Case %d)" % (p_city_count, test_case_index)

        service_counts_for_cities_strs = []
        for i in range(0, p_city_count):
            ci_the_city_index_we_care_about = input()
            gbus_serving_this_city_count = 0
            for service_range in gbus_ranges:
                if (ci_the_city_index_we_care_about >= service_range[0]) and (
                        ci_the_city_index_we_care_about <= service_range[1]):
                    gbus_serving_this_city_count += 1

            service_counts_for_cities_strs.append(str(gbus_serving_this_city_count))

            if verbose:
                print "City Index %d is served by %d bus routes" % (
                ci_the_city_index_we_care_about, gbus_serving_this_city_count)

        print "Case #" + str(test_case_index + 1) + ": " + " ".join(service_counts_for_cities_strs)

        raw_input()


naive(False)

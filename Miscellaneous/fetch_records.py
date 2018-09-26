import csv


def get_highest_gross_movies(year: "str"):
    """
    Method prints out 2 highest gross movies
    :param year: movie released in year
    :return: void
    """

    if type(year) != str:
        year = str(year)

    with open('movies_1.csv', 'r') as csv_file:
        # create a csv reader object
        csv_reader = csv.reader(csv_file, delimiter=',')
        count = 0
        result_dict = {}

        for row in csv_reader:
            if count == 0:
                #print("Columns are {}", format(row))
                count += 1
            else:
                if row[2] == year:
                    tmp = {int(row[4]): row[1]}
                    result_dict.update(tmp)

        result_list = sorted(result_dict, reverse=True)

        print("Two highest movie profit making  movies are 1) {} and 2) {}"
              .format(result_dict[result_list[0]],
                      result_dict[result_list[1]])
              )


get_highest_gross_movies(1982)



def convert_to_dnf(expr, first_iloraz=False):
    translation_table = dict.fromkeys(map(ord, '()'), None)
    expr = expr.translate(translation_table)

    expr = simplify(expr, 0)
    outside_counter = expr[1]
    expr = expr[0]

    ors = expr.split('&')

    tmp = expr.replace('|', '&').split('&')
    # k
    for i in range(len(ors)):
        ors[i] = ors[i].translate(translation_table)

    outside_counter += len(ors)
    # wyodrebnienie wystepujacych elementow
    tmp_set = sorted(list(set(tmp)))
    number_of_occurrences = {key: 0 for key in tmp_set}

    # znalezienie liczby wystapien kazdego elementu
    for letter in tmp:
        number_of_occurrences[letter] += 1

    outside_counter += len(tmp)

    sorted_number_of_occurrences = sorted(number_of_occurrences.items(), key=lambda x: x[1], reverse=True)
    number_of_occurrences = dict(sorted_number_of_occurrences)

    next_stage_expr = ''
    index = 0

    # "wyciagniecie" zmiennych przed nawias
    # w najgorszym przypadku k^2
    custom_iterator = 0
    while len(ors) > 0:
        to_ands = ""

        # zmienna do "wyciagniecia" przed nawias
        main_letter = list(number_of_occurrences.keys())[index]

        ors_to_iterate = list(ors)
        # przeszukanie sum i usuniecie tych z ktorych udalo sie "wyciagnac"
        # zmienna przed nawias
        for one_or in ors_to_iterate:
            custom_iterator += 1
            if main_letter in one_or:
                ors.remove(one_or)
                one_or = one_or.split('|')
                # usuniecie zmiennej "wyciagnietej" przed nawias z sumy
                if len(one_or) > 1:
                    one_or.remove(main_letter)
                to_ands += '&'.join(one_or) + "&"

        # jesli udalo "wyciagnac" sie przed nawias
        if len(to_ands) > 0:
            set_of_elements = set(to_ands[:-1].split('&'))
            to_ands = "&".join(set_of_elements)
            if to_ands != main_letter:
                to_ands = main_letter + '|' + to_ands
            next_stage_expr += to_ands + '*'

        index += 1
    next_stage_expr = next_stage_expr[:-1]

    outside_counter += custom_iterator

    separated_elements = next_stage_expr.split('*')

    translation_table = dict.fromkeys(map(ord, '()'), None)

    next_stage_expr_2 = set()
    # nastepnie "wymnozenie" nawiasow
    # worst case: 2^k * k
    another_counter = 0
    if first_iloraz:
        result = ''
        for i in range(len(separated_elements)):
            one_separated_element = separated_elements[i]
            shortest_element = one_separated_element.split('|')[0]
            length_of_element = len(shortest_element)

            for j in one_separated_element.split('|'):
                another_counter += 1
                if len(j) < length_of_element:
                    length_of_element = len(j)
                    shortest_element = j

            result += shortest_element + '&'

        result = result[:-1].split('&')
        result = "&".join(sorted(set(result)))
        next_stage_expr_2.add(result)
    else:
        indexes = []
        permutations = 1
        # worst case: k
        for i in range(len(separated_elements)):
            separated_elements[i] = separated_elements[i].translate(translation_table)
            indexes.append(0)
            permutations *= len(separated_elements[i].split('|'))

        for i in range(permutations):

            result = ''

            for j in range(len(indexes)):
                result += separated_elements[j].split('|')[indexes[j]] + '&'
                another_counter += 1

            result = result[:-1].split('&')
            result = "&".join(sorted(set(result)))
            next_stage_expr_2.add(result)

            indexes[-1] += 1
            for j in range(len(indexes) - 1, 0, -1):

                if indexes[j] == len(separated_elements[j].split('|')):
                    indexes[j - 1] += 1
                    indexes[j] = 0

    outside_counter += another_counter

    next_stage_expr_2 = list(next_stage_expr_2)
    final_ands = list(next_stage_expr_2)
    # usuwanie iloczynow na podstawie zasad algebry Boole'a - a + a*b = a
    custom_iterator = 0
    custom_full = 0
    # worst case: 2^k * 2^k
    for i in range(len(next_stage_expr_2)):
        for j in range(len(next_stage_expr_2)):
            custom_full += 1
            if i == j:
                continue
            custom_iterator += 1
            first_element = set(next_stage_expr_2[i].split('&'))
            second_element = set(next_stage_expr_2[j].split('&'))
            if first_element & second_element == first_element:
                try:
                    final_ands.remove(next_stage_expr_2[j])
                finally:
                    continue

    outside_counter += custom_full

    final_ands = sorted(final_ands, key=len)
    return final_ands, outside_counter


def simplify(to_simplyfy, c):
    splitted = list(set(to_simplyfy.split('&')))
    final_ands = list(splitted)
    # worst case: k^2 [ - k]
    counter = 0
    for i in range(len(splitted)):
        for j in range(len(splitted)):
            counter += 1
            if i == j:
                continue

            first_element = set(splitted[i].split('|'))
            second_element = set(splitted[j].split('|'))
            if first_element & second_element == first_element:
                try:
                    final_ands.remove(splitted[j])
                finally:
                    continue
    c += counter

    return ('&'.join(final_ands), c)

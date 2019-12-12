initial_data = {
    "foo": {
        "bar": {
            "value": 25
        },
        "bar2": {
            "value": 36
        },
        "serhii": 15,
    }, "foo2": 30,
    "ira": 20
}

final_dict = {}


def my(diction):
    def run(val, k, name1):
        if type(val) is str or type(val) is int:
            final_dict[name1] = val
            return final_dict
        else:
            for kk, vv in val.items():
                name2 = name1 + '.' + kk
                run(vv, kk, name2)

    for k, v in diction.items():
        name1 = k
        run(v, k, name1)

    print(final_dict)
    return final_dict


dict_w_dot = my(initial_data)

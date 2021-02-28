# double, char

a_int = 1  # limited by memory, no singed/unsigned
a_float = 1.0  # float defined by dot
# no double in Python

print(1 / 2)
print(int(1 / 2))
print(1 // 2)

a_str = "test"
a_str2 = 'test'  # same as double quote
a_str3 = "t"  # no char data-type in Python

eng_abbr = "Beata's \" cat"

a_bool = False  # false for 0, [], None, False, ""
a_bool_map = bool("False")  # True for any values other than 0
print(a_bool_map)

a_list = [1, [2, 3], "test"]  # list element can be any value or data-type
print(a_list[1])
# print(a_list[3]) - exception
print(a_list[-1])

a_tuple = (1, 2, "test")  # immutable, no removal, no value change

a_dict = {
    "key": "value",
    "key2": "value2",
    "key_list": [1, 2, 3],
    "key_dict": {
        "inner_key": "inner_value"
    }
}
print(a_dict["key"])
print(a_dict["key_dict"]["inner_key"])

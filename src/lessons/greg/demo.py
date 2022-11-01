import re


def demo_re(searching, reg_exp, exp_num, assert_value):
    reg_exp_pr = repr(reg_exp)
    if assert_value:
        assert re.search(reg_exp, searching)
        print(exp_num, reg_exp_pr, re.search(reg_exp, searching))
    else:
        assert not re.search(reg_exp, searching)
        print(exp_num, reg_exp_pr, "no match")


s = "ab"
assert "a" in s

cs = "hhuihgTFlknufbkXet\nsZTkjkklk\n\n476nx(#dCjjJh"

assert "ui" in cs
assert cs.find("nufb") == 10
assert "ZTk" in cs


res = [
    {"expression": "nufb", "assert_value": True},  # 0
    {"expression": "abc", "assert_value": False},  # 1
    {"expression": "[f-i][S,T][f,F]", "assert_value": True},  # 2
    {"expression": "[0-9][0-9][0-9]n", "assert_value": True},  # 3
    {"expression": "[0-9]{3}n", "assert_value": True},  # 4
    {"expression": "\(", "assert_value": True},  # 5
    {"expression": "g.F", "assert_value": True},  # 6
    {"expression": "g.T", "assert_value": False},  # 7
    {"expression": "^hh", "assert_value": True},  # 8
    {"expression": "$Jh", "assert_value": False},  # 9
    {"expression": "Jh$", "assert_value": True},  # 10
    {"expression": "t.s", "assert_value": False},  # 11
    {"expression": "t+s", "assert_value": False},  # 12
    {"expression": "t*s", "assert_value": True},  # 13
    {"expression": "t\n+s", "assert_value": True},  # 14
    {"expression": "t\n*s", "assert_value": True},  # 15
    {"expression": "6\n+ns", "assert_value": False},  # 16
    {"expression": "6\n*n", "assert_value": True},  # 17
    {"expression": "t*k", "assert_value": True},  # 18
    {"expression": "h.*k", "assert_value": True},  # 19
]


print(f"\nFor {repr(cs)}:\n")
[demo_re(cs, re["expression"], pos, re["assert_value"]) for pos, re in enumerate(res)]

# see https://regex101.com/

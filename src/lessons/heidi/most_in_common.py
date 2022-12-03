def most_in_common(user_name, profiles):
    user_artists = profiles[user_name].keys()
    max_in_common = 0
    for user, artists in profiles.items():
        if user == user_name:
            continue
        in_common = 0
        this_user_artists = artists.keys()
        for this_users_artist in this_user_artists:
            if this_users_artist in user_artists:
                in_common += 1
        if in_common > max_in_common:
            max_in_common = in_common
            user_most_in_common = user
    return user_most_in_common


if __name__ == "__main__":
    user_profiles = {'Jed_I_Knight': {'SeaGulls!': 8, 'DJ D-Bug': 9},
                     'csNoob': {'AntsInMyPants!': 5, 'DJ D-Bug': 8,
                                'Lounge Leias...': 10},
                     'PeterTheAnteater': {'AtTheFlagpoles!': 10,
                                          'SeaGulls!': 8,
                                          'Lounge Leias...': 7},
                     'Yoda': {'AtTheFlagpoles!': 10, 'AntsInMyPants!': 5,
                              'DJ D-Bug': 9}}

    assert most_in_common('csNoob', user_profiles) in (
        'Yoda', 'PeterTheAnteater')
    assert most_in_common('Yoda', user_profiles) in (
        'PeterTheAnteater', 'csNoob')

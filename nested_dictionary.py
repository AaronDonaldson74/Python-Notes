# sports = [
#     {'hunting': {'sept': 'elk', 'oct': 'deer', 'nov': 'moose'}},
#     {'fishing': {'river': 'Trout', 'lakes': 'bluegill', 'streams': 'brookies'}},
# ]
 
# print(sports[0])


# fishing = sports[1].get('fishing', 'Sports not found')

# print(list(fishing.values())[1])

# 1.
# daily_smarty_api = [
#   {
#     "posts": [
#       {
#         "title": "Title One",
#         "url_for_api": "https://www.titleOne.com"
#       },
#       {
#         "title": "Title Two",
#         "url_for_api": "https://www.titleTwo.com"
#       },
#       {
#         "title": "Title Three",
#         "url_for_api": "https://wwww.titleThree.com"
#       },
#       {
#         "title": "Title Four",
#         "url_for_api": "https://www.titleFour.com"
#       }
#     ]
#   }
# ]

# 2.
daily_smarty_api = [
    {
        "posts": [
            {
                "title": "Title One",
                "url_for_api": "https://www.titleOne.com"
            },           
            {
                "title": "Title Two",
                "url_for_api": "https://www.titleTwo.com"
            },
            {
                "title": "Title Three",
                "url_for_api": "https://www.titleThree.com"
            },
            {
                "title": "Title Four",
                "url_for_api": "https://www.titleFour.com"
            }
        ]
    }
]

# 3.
# daily_smarty_api = [
#     {
#         "posts": [
#             {},
#             {},
#             {},
#             {}
#         ]
#     }
# ]

# 4.
# daily_smarty_api = [
#     {
#         "posts": [
#             {},
#             {},
#             {},
#             {}
#         ]
#     }
# ]

""" When finished delete all of the dictionaries except one with data """

""" print all the posts """
print(daily_smarty_api[0]['posts'])

""" print the first post """
print(daily_smarty_api[0]['posts'][0])

""" print the first posts title """
print(daily_smarty_api[0]['posts'][0]['title'])

""" print the first posts url """
print(daily_smarty_api[0]['posts'][0]['url_for_api'])

""" print the last post """
print(daily_smarty_api[0]['posts'][-1])

""" print the last posts title """
print(daily_smarty_api[0]['posts'][-1]['title'])

""" print the last posts url """
print(daily_smarty_api[0]['posts'][-1]['url_for_api'])

""" print the first two posts """
print(daily_smarty_api[0]['posts'][0:2])

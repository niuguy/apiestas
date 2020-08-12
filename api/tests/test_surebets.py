from datetime import datetime, timezone


def test_list_surebets(client, collection):
    collection.insert_one(
        {
            "sport": "basketball",
            "tournament": "test-cup",
            "tournament_nice": "Test Cup",
            "teams": [
                "Testonia Basket",
                "Real Testing"
            ],
            "commence_time": datetime(2020, 8, 13, 20, 30, 00, tzinfo=timezone.utc),
            "url": '',
            "bets": [
                {
                    "bookmaker": "testbet",
                    "bookmaker_nice": "Test Bet",
                    "bet_type": "Winner",
                    "bet_scope": "Full Time",
                    "is_back": True,
                    "url": "https://data.testingportal.com/feed/match/1-12-jRKgDPoT-2-12-abcd1.dat",
                    "odds": [
                        1.6,
                        3.6,
                    ],
                    "slug": "testonia-basket-real-testing-sport-basketball-test-cup-1597350600-testbet-winner-full-time",
                    "feed": "testfeed_1"
                },
                {
                    "bookmaker": "test-365",
                    "bookmaker_nice": "Test 365",
                    "bet_type": "Winner",
                    "bet_scope": "Full Time",
                    "is_back": True,
                    "url": "https://data.testingportal.com/feed/match/1-12-jRKgDPoT-2-12-abcd2.dat",
                    "odds": [
                        1.7,
                        3.2,
                    ],
                    "slug": "testonia-basket-real-testing-sport-basketball-test-cup-1597350600-testbet-winner-full-time",
                    "feed": "testfeed_1"
                },
            ],
            "surebets": [
                {
                    "bet_type": "Winner",
                    "bet_scope": "Full Time",
                    "is_back": True,
                    "profit": 0.0625,
                    "slug": "testonia-basket-real-testing-sport-basketball-test-cup-1597350600-testbet-test-365",
                    "created_at": datetime(2020, 8, 11, 20, 25, 58),
                    "updated_at": datetime(2020, 8, 11, 20, 25, 58),
                    "outcomes": [
                        {
                            "bookmaker": "testbet",
                            "bookmaker_nice": "Test Bet",
                            "url": "https://data.testingportal.com/feed/match/1-12-jRKgDPoT-2-12-abcd1.dat",
                            "odd": 1.6
                        },
                        {
                            "bookmaker": "test-365",
                            "bookmaker_nice": "Test 365",
                            "url": "https://data.testingportal.com/feed/match/1-12-jRKgDPoT-2-12-abcd2.dat",
                            "odd": 3.2
                        },
                    ],
                },
                {
                    "bet_type": "Winner",
                    "bet_scope": "Full Time",
                    "is_back": True,
                    "profit": 0.133986928104575,
                    "slug": "testonia-basket-real-testing-sport-basketball-test-cup-1597350600-test-365-testbet",
                    "created_at": datetime(2020, 8, 11, 20, 25, 58),
                    "updated_at": datetime(2020, 8, 11, 20, 25, 58),
                    "outcomes": [
                        {
                            "bookmaker": "test-365",
                            "bookmaker_nice": "Test 365",
                            "url": "https://data.testingportal.com/feed/match/1-12-jRKgDPoT-2-12-abcd2.dat",
                            "odd": 1.7,
                        },
                        {
                            "bookmaker": "testbet",
                            "bookmaker_nice": "Test Bet",
                            "url": "https://data.testingportal.com/feed/match/1-12-jRKgDPoT-2-12-abcd1.dat",
                            "odd": 3.6
                        }
                    ]
                }
            ],
            "slug": "testonia-basket-real-testing-sport-basketball-test-cup-1597350600",
            "feed": "testfeed_1"
        }
    )
    response = client.get("/api/matches/surebets/", params={
        "sport": "basketball",
        "commence_day": "2020-08-13",
        "min_profit": 0.1
    })
    print(response)
    assert response.status_code == 200
    data = response.json()
    assert data['surebetsCount'] == 1
    assert data['surebets'][0] == {
        "sport": "basketball",
        "tournament": "test-cup",
        "tournamentNice": "Test Cup",
        "teams": [
            "Testonia Basket",
            "Real Testing"
        ],
        "commenceTime": "2020-08-13T20:30:00Z",
        "url": '',
        "surebet": {
            "betType": "Winner",
            "betScope": "Full Time",
            "isBack": True,
            "profit": 0.133986928104575,
            "slug": "testonia-basket-real-testing-sport-basketball-test-cup-1597350600-test-365-testbet",
            "createdAt": "2020-08-11T20:25:58Z",
            "updatedAt": "2020-08-11T20:25:58Z",
            "outcomes": [
                {
                    "bookmaker": "test-365",
                    "bookmakerNice": "Test 365",
                    "url": "https://data.testingportal.com/feed/match/1-12-jRKgDPoT-2-12-abcd2.dat",
                    "odd": 1.7
                },
                {
                    "bookmaker": "testbet",
                    "bookmakerNice": "Test Bet",
                    "url": "https://data.testingportal.com/feed/match/1-12-jRKgDPoT-2-12-abcd1.dat",
                    "odd": 3.6
                }
            ]
        }
    }

from fastapi import FastAPI

app = FastAPI(
    title="Trading App"
)

fake_users = [
    {'id': 1, 'role': 'admin', 'name': 'Alex'},
    {'id': 2, 'role': 'investor', 'name': 'Boris'},
    {'id': 3, 'role': 'trader', 'name': 'Sergey'},
]


@app.get('/users{user_id}')
def get_user(user_id: int):
    return [user for user in fake_users if user.get('id') == user_id]


fake_users = [
    {
        'id': 1, 'user_id': 1, 'currently': 'TON',
        'side': 'buy', 'price': 123, "amount": 2.23
    },
    {
        'id': 2, 'user_id': 1, 'currently': 'ETH',
        'side': 'sell', 'price': 125, "amount": 2.23
    },
]


@app.get('/trades')
def get_trades(limit: int = 1, offset: int = 0):
    return fake_users[offset:][:limit]


fake_users2 = [
    {'id': 1, 'role': 'admin', 'name': 'Alex'},
    {'id': 2, 'role': 'investor', 'name': 'Boris'},
    {'id': 3, 'role': 'trader', 'name': 'Sergey'},
]


@app.post('/users{user_id}')
def change_user_name(user_id: int, new_name: str):
    current_user = list(filter(
        lambda user: user.get('id') == user_id, fake_users2))[0]
    current_user['name'] = new_name
    return {'status': 200, 'data': current_user}

import asyncio
import sys

import orm
from models import User, Blog, Comment


async def test(loop):
	await orm.create_pool(loop=loop, port=3306, user='root', password='password',
	                      db='awesome')
	u = User(name='Test', email='for_test@example.com', passwd='1234567878',
	         image='about:blank',)
	await u.save()


loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()
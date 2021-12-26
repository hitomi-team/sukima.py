import asyncio
import json
import logging

import aiohttp

from sukipy.models.requests import ModelGenRequest


class Sukima:
    def __init__(self, *,
                 addr: str):
        if addr.endswith("/"):
            addr = addr[:-1]
        self.addr = addr
        self.token = None

    # Maybe use events.
    async def authorize(self, username, password):
        r = await self.post(f"{self.addr}/api/v1/users/token", data={"username": username, "password": password})
        if r.status == 200:
            self.token = (await r.json())["access_token"]

    async def post(self, url, data, auth=None):
        headers = None
        if auth:
            headers = {"Authorization": f"Bearer {auth}"}
        async with aiohttp.ClientSession() as session:
            r = await session.post(url, json=data, headers=headers)
        return r

    async def get(self, url, auth=None):
        headers = None
        if auth:
            headers = {"Authorization": f"Bearer {auth}"}
        async with aiohttp.ClientSession() as session:
            r = await session.get(url, headers=headers)
        return r

    async def health_check(self):
        r = await self.get(f"{self.addr}/")
        if r.status == 200:
            return True
        else:
            return False

    async def get_models(self):
        r = await self.get(f"{self.addr}/api/v1/models")
        if r.status == 200:
            return list((await r.json())["models"].keys())
        else:
            raise Exception("Unable to fetch models.")  # Make use of exceptions.py...

    # There's a way to sync these endpoint locations with the backend repo, right?
    async def generate(self, args: ModelGenRequest, *, raw_output=False):
        r = await self.post(f"{self.addr}/api/v1/models/generate", data=args.json(), auth=self.token)

        if r.status == 200:
            if raw_output:
                return (await r.json())["completion"]["text"]
            else:
                return (await r.json())["completion"]["text"][len(args["prompt"]):]
        else:
            raise Exception("Unable to generate text.", r.json())

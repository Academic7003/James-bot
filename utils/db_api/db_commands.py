from typing import List

from sqlalchemy import and_

from utils.db_api.models import TruthOrDare
from utils.db_api.database import db


async def add_truth(**kwargs):
    new_item = await TruthOrDare(**kwargs).create()
    return new_item

async def add_dare(**kwargs):
    new_item = await TruthOrDare(**kwargs).create()
    return new_item

async def get_dare():
    return await TruthOrDare.query.distinct(TruthOrDare.text).where(TruthOrDare.category == "dare").gino.all()

async def get_truth():
    return await TruthOrDare.query.distinct(TruthOrDare.text).where(TruthOrDare.category == "truth").gino.all()


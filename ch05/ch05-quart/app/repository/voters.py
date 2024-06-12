
from typing import Dict, Any

from sqlalchemy import update, delete, insert
from sqlalchemy.future import select
from sqlalchemy.orm import Session
from app.model.db import Voter
from datetime import datetime


class VoterRepository: 
    
    def __init__(self, sess:Session):
        self.sess:Session = sess
    
    async def insert(self, voter: Voter) -> bool: 
        try:
            sql = insert(Voter).values(mid=voter.mid, precinct=voter.precinct, 
                                       voter_id=voter.voter_id, last_vote_date=datetime.strptime(voter.last_vote_date, '%Y-%m-%d').date())
            await self.sess.execute(sql)
            await self.sess.commit()
            await self.sess.close()
            return True
            #self.sess.add(attendance)
            #await self.sess.flush()
        except Exception as e: 
            print(e)
        return False
    
    async def update(self, id:int, details:Dict[str, Any]) -> bool: 
       try:
           sql = update(Voter).where(Voter.id == id).values(**details)
           await self.sess.execute(sql)
           await self.sess.commit()
           await self.sess.close()
           return True
       except Exception as e: 
           print(e)
       return False
   
    async def delete(self, id:int) -> bool: 
        try:
           sql = delete(Voter).where(Voter.id == id)
           await self.sess.execute(sql)
           await self.sess.commit()
           await self.sess.close()
           return True
        except Exception as e: 
            print(e)
        return False
    
    async def select_all_voter(self):
        sql = select(Voter)
        sql.execution_options(synchronize_session="fetch")
        q = await self.sess.execute(sql)
        records = q.scalars().all()
        await self.sess.close()
        return records
    
    async def select_voter(self, id:int): 
        sql = select(Voter).where(Voter.id == id)
        sql.execution_options(synchronize_session="fetch")
        q = await self.sess.execute(sql)
        record = q.scalars().all()
        await self.sess.close()
        return record

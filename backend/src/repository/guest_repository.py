from src.database.mysql import get_mysql_db
from src.database.valkey import get_valkey_db
from src.entity.guest import Guest
from typing import List

class GuestRepository:
    @staticmethod
    def save(uuid: str, nickname: str) -> None:
        """
        새로운 방문자 정보를 생성하고 DB에 저장합니다.
        """
        with get_mysql_db() as db:
            new_guest = Guest(
                uuid=uuid,
                nickname=nickname
            )

            db.add(new_guest)
            db.commit()  # 실제 DB에 반영

    @staticmethod
    def save_nicknames(nicknames: List[str]):
        """
        닉네임 5개를 valkey(redis)에 캐싱합니다.
        """
        with get_valkey_db() as db:
            db.sadd("nickname_pool", *nicknames)

    @staticmethod
    def pop_nickname():
        """
        닉네임을 1개 반환합니다.
        """
        with get_valkey_db() as db:
            return db.spop("nickname_pool")
        
    @staticmethod
    def get_nickname_count():
        """
        캐싱되어 있는 닉네임 개수를 반환합니다.
        """
        with get_valkey_db() as db:
            return db.scard("nickname_pool")
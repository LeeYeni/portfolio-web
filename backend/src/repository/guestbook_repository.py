from src.database.mysql import get_mysql_db
from src.entity.guestbook import GuestBook
from src.entity.guest import Guest

class GuestBookRepository:
    @staticmethod
    def save(uuid: str, message: str):
        """
        방명록을 저장합니다.
        """
        with get_mysql_db() as db:
            guest = db.query(Guest).filter(Guest.uuid==uuid).first()
            new_guestbook = GuestBook(
                guest_id = guest.id,
                message=message
            )

            db.add(new_guestbook)
            db.commit()
        
    @staticmethod
    def get_all():
        """
        방명록을 모두 반환합니다.
        """
        with get_mysql_db() as db:
            results = db.query(GuestBook) \
                    .join(GuestBook.guest) \
                    .with_entities(
                        Guest.nickname,
                        GuestBook.message,
                        GuestBook.created_at,
                    ) \
                    .order_by(GuestBook.created_at.asc()) \
                    .all()
            
            return [
                {
                    "nickname": r.nickname,
                    "message": r.message,
                    "created_at": r.created_at
                } for r in results
            ]
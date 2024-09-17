from sqlalchemy import text
from session import session_generator


for i in range(50):
    session = next(session_generator)

    query = """
                select *
                from test_table;
            """

    print(session.execute(text(query)).mappings().fetchall())

    session.commit()


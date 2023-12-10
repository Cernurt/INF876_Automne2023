'''
Film actors/actress recommendation based on co-occurrences
DVD Rental database https://www.postgresqltutorial.com/wp-content/uploads/2019/05/dvdrental.zip

@author yohanes.gultom@gmail.com
'''

import sqlalchemy as db
from pprint import pprint

engine = db.create_engine('postgresql://postgres:postgres@localhost/dvdrental')
connection = engine.connect()

query = db.sql.text("""select actor.actor_id, actor.first_name, actor.last_name, x.cooccurrence from (
    select film_actor2.actor_id, count(*) as cooccurrence
    from film_actor film_actor1 join film_actor film_actor2 on film_actor1.film_id = film_actor2.film_id
    where film_actor1.actor_id != film_actor2.actor_id 
    and film_actor1.actor_id = :actor_id
    group by film_actor1.actor_id, film_actor2.actor_id
) x join actor on x.actor_id = actor.actor_id
where x.cooccurrence > 2
order by x.cooccurrence desc
""")

# get actors/actress that often acted together with given input_actor_id
input_actor_id = 107
result = connection.execute(query, actor_id=input_actor_id).fetchall()
pprint(result)

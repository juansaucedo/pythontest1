from todoapp import app
from models import db
from models import Todo
db.create_all()

from models import Category
work = Category(name=u'work')
home = Category(name=u'home')

from models import Priority
prior1 = Priority(name=u'Max',value=10)
prior2 = Priority(name=u'Min',value=0)

todo1 = Todo(category_id=1,priority_id=1,description=u'This is test 1')
todo2 = Todo(category_id=1,priority_id=2,description=u'This is test 2')
todo3 = Todo(category_id=2,priority_id=1,description=u'This is test 3')
todo4 = Todo(category_id=2,priority_id=2,description=u'This is test 4')

db.session.add(work)
db.session.add(home)
db.session.add(prior1)
db.session.add(prior2)
db.session.add(todo1)
db.session.add(todo2)
db.session.add(todo3)
db.session.add(todo4)
db.session.commit()

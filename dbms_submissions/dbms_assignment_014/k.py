class DoesNotExist(Exception):
    pass
class MultipleObjectsReturned(Exception):
    pass
class InvalidField(Exception):
    pass

class Student:

    def __init__(self,name, age, score):
        self.name = name
        self.student_id = None
        self.age = age
        self.score = score
    
    @classmethod
    def avg(cls, field, **kwargs):
        if field not in ('name','age','score','student_id'):
                raise InvalidField
                
        if len(kwargs)>=1:
            k=Student.filter(**kwargs)
            q="select avg({}) from student where {} ".format(field,k)
        else:
            q="select avg({}) from student ".format(field)        
    
        ans=read_data(q)
        return ans[0][0]
    
    @classmethod
    def min(cls, field, **kwargs):
        if field not in ('name','age','score','student_id'):
                raise InvalidField
        
        if len(kwargs)>=1:
            k=Student.filter(**kwargs)
            q="select min({}) from student where {} ".format(field,k)
        else:
            q="select min({}) from student ".format(field)        
    
        #print(q)
        ans=read_data(q)
        return ans[0][0]
    
    @classmethod
    def max(cls, field, **kwargs):
        if field not in ('name','age','score','student_id'):
                raise InvalidField
        
        if len(kwargs)>=1:
            k=Student.filter(**kwargs)
            q="select max({}) from student where {} ".format(field,k)
        else:
            q="select max({}) from student ".format(field)        
    
        #print(q)
        ans=read_data(q)
        return ans[0][0]
        
    @classmethod
    def sum(cls, field, **kwargs):
        if field not in ('name','age','score','student_id'):
                raise InvalidField
        
        if len(kwargs)>=1:
            k=Student.filter(**kwargs)
            q="select sum({}) from student where {} ".format(field,k)
        else:
            q="select sum({}) from student ".format(field)        
    
        #print(q)
        ans=read_data(q)
        return ans[0][0]
        
        
    @classmethod
    def count(cls, field=None, **kwargs):
        if field == None:
            q="select count(*) from student "    
        
        elif field not in ('name','age','score','student_id'):
                raise InvalidField
    
            
        elif len(kwargs)>=1:
            k=Student.filter(**kwargs)
            q="select count({}) from student where {} ".format(field,k)
        else:
            q="select count({}) from student ".format(field)        
    
        print(q)
        ans=read_data(q)
        return ans[0][0]
        
        
    
    
    
    
    
     
    @classmethod
    def filter(cls,**kid):
        cls.li=[]
        cls.operator={'lt':'<','lte':'<=','gt':'>','gte':'>=','neq':'!=','in':'in','contain':''}
        
        
        if(len(kid))>=1:
            l=[]
            for x,y in kid.items():
                    cls.a=x
                    cls.b=y
                    
                    field=cls.a
                    field=field.split('__')
                    if field[0] not in ('name','age','score','student_id'):
                            raise InvalidField 
            
                    if(len(field))==1:
                        query=" {}='{}'".format(cls.a,cls.b)
                    elif field[1]=='contains':
                        query=" {} like '%{}%'".format(field[0],cls.b)
                    elif field[1]=='in':
                        query=" {} {} {}".format(field[0],cls.operator[field[1]],tuple(cls.b))
                    else:    
                        query="{} {} '{}'".format(field[0],cls.operator[field[1]],cls.b)
                
                    l.append(query)
                    
            x = " and ".join(l)       
            query= " "+x
            
        return query        
        
    
        

def read_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("dbms/dbms_resources/students.sqlite3")
	crsr = connection.cursor() 
	crsr.execute(sql_query) 
	ans= crsr.fetchall()  
	connection.close() 
	return ans

avg_age = Student.avg('age')
print(avg_age)
avg_age = Student.count('score',score=88)
print(avg_age)
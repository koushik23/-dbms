class InvalidField(Exception):
    pass
def read_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("dbms/dbms_resources/students.sqlite3")
	crsr = connection.cursor() 
	crsr.execute(sql_query) 
	ans= crsr.fetchall()  
	connection.close() 
	return ans

class Student:
    def __init__(self,name, age, score):
        self.name = name
        self.student_id = None
        self.age = age
        self.score = score
    
    @classmethod
    def avg(cls, field, **kwargs):
        ans=aggregation('avg',field,**kwargs)
        return ans
        
    @classmethod
    def min(cls, field, **kwargs):
        ans=aggregation('min',field,**kwargs)
        return ans
        
    @classmethod
    def max(cls, field, **kwargs):
        ans=aggregation('max',field,**kwargs)
        return ans
    
    @classmethod
    def count(cls, field=None, **kwargs):
        ans=aggregation('count',field,**kwargs)
        return ans
    
    @classmethod
    def sum(cls, field, **kwargs):
        ans=aggregation('sum',field,**kwargs)
        return ans
        
    @classmethod
    def filter(cls,**kid):
        cls.li=[]
        cls.operator={'lt':'<','lte':'<=','gt':'>','gte':'>=','neq':'!=','in':'in','contain':''}
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
        
def aggregation(method,field=None, **kwargs):
    
    if field==None:
        q= "select count(*) from student"
    elif field not in ('name','age','score','student_id'):
        raise InvalidField
    elif len(kwargs)>=1:
        k=Student.filter(**kwargs)
        q="select {}({}) from student where {} ".format(method,field,k)
    else:
        q="select {}({}) from student ".format(method,field)        
    print(q)
    ans=read_data(q)
    return ans[0][0]

#avg_age = Student.avg('age')
#print(avg_age)
        
avg_age = Student.count('age')
print(avg_age)        
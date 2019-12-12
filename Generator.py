import mem_profile
import random
import time

name = ['John', 'Corey', 'Adam','Steve','Rick', 'Thomas']
majors = ['Math','Engineering','CompSci','Arts','Business']

print("Memory (Before): {}Mb".format(mem_profile.memory_usage_resource()))

def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {'id' : i,
                  'name' : random.choice(name),
                  'major' : random.choice(major)
                  }
        result.append(person)
        return result

def people_generator(num_people):
    for i in range(num_people):
        person = {'id' : i,
                  'name' : random.choice(name),
                  'major' : random.choice(major)
                  }
        
        yield person

#Run any one at a time to calculate the time difference.
#Using List 
t1 = time.clock()
people = people_list(1000000)
t2 = time.clock()


#Using Generator
t1 = time.clock()
people = people_generator(1000000)
t2 = time.clock()


print("Memory (After): {}Mb".format(mem_profile.memory_usage_resource()))
print('Total {} seconds'.format(t2-t1))
